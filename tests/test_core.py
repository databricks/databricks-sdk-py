import contextlib
import functools
import os
import pathlib
import platform
import random
import string
import typing
from datetime import datetime
from http.server import BaseHTTPRequestHandler
from typing import Iterator, List

import pytest
import requests

from databricks.sdk import WorkspaceClient
from databricks.sdk.core import (ApiClient, Config, DatabricksError,
                                 StreamingResponse)
from databricks.sdk.credentials_provider import (CliTokenSource,
                                                 CredentialsProvider,
                                                 CredentialsStrategy,
                                                 DatabricksCliTokenSource,
                                                 databricks_cli)
from databricks.sdk.environments import (ENVIRONMENTS, AzureEnvironment, Cloud,
                                         DatabricksEnvironment)
from databricks.sdk.oauth import Token
from databricks.sdk.service.catalog import PermissionsChange
from databricks.sdk.service.iam import AccessControlRequest
from databricks.sdk.version import __version__

from .clock import FakeClock
from .conftest import noop_credentials


def test_parse_dsn():
    cfg = Config.parse_dsn('databricks://user:pass@foo.databricks.com?retry_timeout_seconds=600')

    headers = cfg.authenticate()

    assert headers['Authorization'] == 'Basic dXNlcjpwYXNz'
    assert 'basic' == cfg.auth_type


def test_databricks_cli_token_source_relative_path(config):
    config.databricks_cli_path = "./relative/path/to/cli"
    ts = DatabricksCliTokenSource(config)
    assert ts._cmd[0] == config.databricks_cli_path


def test_databricks_cli_token_source_absolute_path(config):
    config.databricks_cli_path = "/absolute/path/to/cli"
    ts = DatabricksCliTokenSource(config)
    assert ts._cmd[0] == config.databricks_cli_path


def test_databricks_cli_token_source_not_installed(config, monkeypatch):
    monkeypatch.setenv('PATH', 'whatever')
    with pytest.raises(FileNotFoundError, match="not installed"):
        DatabricksCliTokenSource(config)


@pytest.mark.parametrize("date_string,expected",
                         [("2023-12-01T15:19:48.007742617Z", datetime(2023, 12, 1, 15, 19, 48)),
                          ("2023-12-05T15:59:01.40081+11:00", datetime(2023, 12, 5, 15, 59, 1)),
                          ("2023-12-06 10:06:05", datetime(2023, 12, 6, 10, 6, 5))])
def test_databricks_cli_token_parse_expiry(date_string, expected):
    assert CliTokenSource._parse_expiry(date_string) == expected


def write_small_dummy_executable(path: pathlib.Path):
    if platform.system() == "Windows":
        cli = path.joinpath('databricks.exe')
        cli.touch()
        cli.write_text('@echo off\necho "hello world"\n')
    else:
        cli = path.joinpath('databricks')
        cli.write_text('#!/bin/sh\necho "hello world"\n')
        cli.chmod(0o755)
    assert cli.stat().st_size < 1024
    return cli


def test_streaming_response_read(config):
    content = b"some initial binary data: \x00\x01"
    response = StreamingResponse(DummyResponse([content]))
    assert response.read() == content


def test_streaming_response_read_partial(config):
    content = b"some initial binary data: \x00\x01"
    response = StreamingResponse(DummyResponse([content]))
    assert response.read(8) == b"some ini"


def test_streaming_response_read_full(config):
    content = b"some initial binary data: \x00\x01"
    response = StreamingResponse(DummyResponse([content, content]))
    assert response.read() == content + content


def test_streaming_response_read_closes(config):
    content = b"some initial binary data: \x00\x01"
    dummy_response = DummyResponse([content])
    with StreamingResponse(dummy_response) as response:
        assert response.read() == content
    assert dummy_response.isClosed()


def write_large_dummy_executable(path: pathlib.Path):
    cli = path.joinpath('databricks')

    # Generate a long random string to inflate the file size.
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(1024 * 1024))
    cli.write_text("""#!/bin/sh
cat <<EOF
{
"access_token": "token",
"token_type": "Bearer",
"expiry": "2023-05-22T00:00:00.000000+00:00"
}
EOF
exit 0
""" + random_string)
    cli.chmod(0o755)
    assert cli.stat().st_size >= (1024 * 1024)
    return cli


def test_databricks_cli_token_source_installed_legacy(config, monkeypatch, tmp_path):
    write_small_dummy_executable(tmp_path)
    monkeypatch.setenv('PATH', tmp_path.as_posix())
    with pytest.raises(FileNotFoundError, match="version <0.100.0 detected"):
        DatabricksCliTokenSource(config)


def test_databricks_cli_token_source_installed_legacy_with_symlink(config, monkeypatch, tmp_path):
    dir1 = tmp_path.joinpath('dir1')
    dir2 = tmp_path.joinpath('dir2')
    dir1.mkdir()
    dir2.mkdir()

    if platform.system() == 'Windows':
        (dir1 / "databricks.exe").symlink_to(write_small_dummy_executable(dir2))
    else:
        (dir1 / "databricks").symlink_to(write_small_dummy_executable(dir2))

    path = pathlib.Path(dir1)
    path = str(path)
    monkeypatch.setenv('PATH', path)

    with pytest.raises(FileNotFoundError, match="version <0.100.0 detected"):
        DatabricksCliTokenSource(config)


def test_databricks_cli_token_source_installed_new(config, monkeypatch, tmp_path):
    write_large_dummy_executable(tmp_path)
    monkeypatch.setenv('PATH', tmp_path.as_posix())
    DatabricksCliTokenSource(config)


def test_databricks_cli_token_source_installed_both(config, monkeypatch, tmp_path):
    dir1 = tmp_path.joinpath('dir1')
    dir2 = tmp_path.joinpath('dir2')
    dir1.mkdir()
    dir2.mkdir()

    write_small_dummy_executable(dir1)
    write_large_dummy_executable(dir2)

    # Resolve small before large.
    monkeypatch.setenv('PATH', str(os.pathsep).join([dir1.as_posix(), dir2.as_posix()]))
    DatabricksCliTokenSource(config)

    # Resolve large before small.
    monkeypatch.setenv('PATH', str(os.pathsep).join([dir2.as_posix(), dir1.as_posix()]))
    DatabricksCliTokenSource(config)


def test_databricks_cli_credential_provider_not_installed(config, monkeypatch):
    monkeypatch.setenv('PATH', 'whatever')
    assert databricks_cli(config) == None


def test_databricks_cli_credential_provider_installed_legacy(config, monkeypatch, tmp_path):
    write_small_dummy_executable(tmp_path)
    monkeypatch.setenv('PATH', tmp_path.as_posix())
    assert databricks_cli(config) == None


def test_databricks_cli_credential_provider_installed_new(config, monkeypatch, tmp_path, mocker):
    get_mock = mocker.patch('databricks.sdk.credentials_provider.CliTokenSource.refresh',
                            return_value=Token(access_token='token',
                                               token_type='Bearer',
                                               expiry=datetime(2023, 5, 22, 0, 0, 0)))
    write_large_dummy_executable(tmp_path)
    path = str(os.pathsep).join([tmp_path.as_posix(), os.environ['PATH']])
    path = pathlib.Path(path)
    path = str(path)
    monkeypatch.setenv('PATH', path)

    assert databricks_cli(config) is not None
    assert get_mock.call_count == 1


def test_extra_and_upstream_user_agent(monkeypatch):

    class MockUname:

        @property
        def system(self):
            return 'TestOS'

    monkeypatch.setattr(platform, 'python_version', lambda: '3.0.0')
    monkeypatch.setattr(platform, 'uname', MockUname)
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM', "upstream-product")
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM_VERSION', "0.0.1")
    monkeypatch.setenv('DATABRICKS_RUNTIME_VERSION', "13.1 anything/else")

    config = Config(host='http://localhost', username="something", password="something", product='test',
                    product_version='0.0.0') \
        .with_user_agent_extra('test-extra-1', '1') \
        .with_user_agent_extra('test-extra-2', '2')

    assert config.user_agent == (
        f"test/0.0.0 databricks-sdk-py/{__version__} python/3.0.0 os/testos auth/basic test-extra-1/1 test-extra-2/2"
        " upstream/upstream-product upstream-version/0.0.1 runtime/13.1-anything-else")


def test_config_copy_shallow_copies_credential_provider():

    class TestCredentialsStrategy(CredentialsStrategy):

        def __init__(self):
            super().__init__()
            self._token = "token1"

        def auth_type(self) -> str:
            return "test"

        def __call__(self, cfg: 'Config') -> CredentialsProvider:
            return lambda: {"token": self._token}

        def refresh(self):
            self._token = "token2"

    credentials_strategy = TestCredentialsStrategy()
    config = Config(credentials_strategy=credentials_strategy)
    config_copy = config.copy()

    assert config.authenticate()["token"] == "token1"
    assert config_copy.authenticate()["token"] == "token1"

    credentials_strategy.refresh()

    assert config.authenticate()["token"] == "token2"
    assert config_copy.authenticate()["token"] == "token2"
    assert config._credentials_strategy == config_copy._credentials_strategy


def test_config_accounts_aws_is_accounts_host(config):
    config.host = "https://accounts.cloud.databricks.com"
    assert config.is_account_client


def test_config_accounts_dod_is_accounts_host(config):
    config.host = "https://accounts-dod.cloud.databricks.us"
    assert config.is_account_client


def test_config_workspace_is_not_accounts_host(config):
    config.host = "https://westeurope.azuredatabricks.net"
    assert not config.is_account_client


# This test uses the fake file system to avoid interference from local default profile.
def test_config_can_be_subclassed(fake_fs):

    class DatabricksConfig(Config):

        def __init__(self):
            super().__init__()

    with pytest.raises(ValueError): # As opposed to `KeyError`.
        DatabricksConfig()


def test_config_parsing_non_string_env_vars(monkeypatch):
    monkeypatch.setenv('DATABRICKS_DEBUG_TRUNCATE_BYTES', '100')
    c = Config(host='http://localhost', credentials_strategy=noop_credentials)
    assert c.debug_truncate_bytes == 100


class DummyResponse(requests.Response):
    _content: Iterator[bytes]
    _closed: bool = False

    def __init__(self, content: List[bytes]) -> None:
        super().__init__()
        self._content = iter(content)

    def iter_content(self, chunk_size: int = 1, decode_unicode=False) -> Iterator[bytes]:
        return self._content

    def close(self):
        self._closed = True

    def isClosed(self):
        return self._closed


def test_api_client_do_custom_headers(config, requests_mock):
    client = ApiClient(config)
    requests_mock.get("/test",
                      json={"well": "done"},
                      request_headers={
                          "test": "test",
                          "User-Agent": config.user_agent
                      })
    res = client.do("GET", "/test", headers={"test": "test"})
    assert res == {"well": "done"}


def test_access_control_list(config, requests_mock):
    requests_mock.post("http://localhost/api/2.1/jobs/create",
                       request_headers={"User-Agent": config.user_agent})

    w = WorkspaceClient(config=config)
    res = w.jobs.create(access_control_list=[AccessControlRequest(group_name="group")])

    assert requests_mock.call_count == 1
    assert requests_mock.called
    assert requests_mock.last_request.json() == {'access_control_list': [{'group_name': 'group'}]}


def test_shares(config, requests_mock):
    requests_mock.patch("http://localhost/api/2.1/unity-catalog/shares/jobId/permissions",
                        request_headers={"User-Agent": config.user_agent})

    w = WorkspaceClient(config=config)
    res = w.shares.update_permissions(name="jobId", changes=[PermissionsChange(principal="principal")])

    assert requests_mock.call_count == 1
    assert requests_mock.called
    assert requests_mock.last_request.json() == {'changes': [{'principal': 'principal'}]}


def test_deletes(config, requests_mock):
    requests_mock.delete("http://localhost/api/2.0/sql/alerts/alertId",
                         request_headers={"User-Agent": config.user_agent},
                         text="null",
                         )

    w = WorkspaceClient(config=config)
    res = w.alerts.delete(id="alertId")

    assert requests_mock.call_count == 1
    assert requests_mock.called

    assert res is None


def test_error(config, requests_mock):
    errorJson = {
        "message":
        "errorMessage",
        "details": [{
            "type": DatabricksError._error_info_type,
            "reason": "error reason",
            "domain": "error domain",
            "metadata": {
                "etag": "error etag"
            },
        }, {
            "type": "wrong type",
            "reason": "wrong reason",
            "domain": "wrong domain",
            "metadata": {
                "etag": "wrong etag"
            }
        }],
    }

    client = ApiClient(config)
    requests_mock.get("/test", json=errorJson, status_code=400, )
    with pytest.raises(DatabricksError) as raised:
        client.do("GET", "/test", headers={"test": "test"})

    error_infos = raised.value.get_error_info()
    assert len(error_infos) == 1
    error_info = error_infos[0]
    assert error_info.reason == "error reason"
    assert error_info.domain == "error domain"
    assert error_info.metadata["etag"] == "error etag"
    assert error_info.type == DatabricksError._error_info_type


def test_error_with_scimType():
    args = {"detail": "detail", "scimType": "scim type"}
    error = DatabricksError(**args)
    assert str(error) == f"scim type detail"


@contextlib.contextmanager
def http_fixture_server(handler: typing.Callable[[BaseHTTPRequestHandler], None]):
    from http.server import HTTPServer
    from threading import Thread

    class _handler(BaseHTTPRequestHandler):

        def __init__(self, handler: typing.Callable[[BaseHTTPRequestHandler], None], *args):
            self._handler = handler
            super().__init__(*args)

        def __getattr__(self, item):
            if 'do_' != item[0:3]:
                raise AttributeError(f'method {item} not found')
            return functools.partial(self._handler, self)

    handler_factory = functools.partial(_handler, handler)
    srv = HTTPServer(('localhost', 0), handler_factory)
    t = Thread(target=srv.serve_forever)
    try:
        t.daemon = True
        t.start()
        yield 'http://{0}:{1}'.format(*srv.server_address)
    finally:
        srv.shutdown()


@pytest.mark.parametrize('status_code,include_retry_after',
                         ((429, False), (429, True), (503, False), (503, True)))
def test_http_retry_after(status_code, include_retry_after):
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(status_code)
            if include_retry_after:
                h.send_header('Retry-After', '1')
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
        else:
            h.send_response(200)
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', clock=FakeClock()))
        res = api_client.do('GET', '/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_retry_after_wrong_format():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(429)
            h.send_header('Retry-After', '1.58')
            h.end_headers()
        else:
            h.send_response(200)
            h.send_header('Content-Type', 'application/json')
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', clock=FakeClock()))
        res = api_client.do('GET', '/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_retried_exceed_limit():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        h.send_response(429)
        h.send_header('Retry-After', '1')
        h.end_headers()
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', retry_timeout_seconds=1, clock=FakeClock()))
        with pytest.raises(TimeoutError):
            api_client.do('GET', '/foo')

    assert len(requests) == 1


def test_http_retried_on_match():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(400)
            h.end_headers()
            h.wfile.write(b'{"error_code": "abc", "message": "... ClusterNotReadyException ..."}')
        else:
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', clock=FakeClock()))
        res = api_client.do('GET', '/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_http_not_retried_on_normal_errors():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) == 0:
            h.send_response(400)
            h.end_headers()
            h.wfile.write(b'{"error_code": "abc", "message": "something not found"}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', clock=FakeClock()))
        with pytest.raises(DatabricksError):
            api_client.do('GET', '/foo')

    assert len(requests) == 1


def test_http_retried_on_connection_error():
    requests = []

    def inner(h: BaseHTTPRequestHandler):
        if len(requests) > 0:
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"foo": 1}')
        requests.append(h.requestline)

    with http_fixture_server(inner) as host:
        api_client = ApiClient(Config(host=host, token='_', clock=FakeClock()))
        res = api_client.do('GET', '/foo')
        assert 'foo' in res

    assert len(requests) == 2


def test_github_oidc_flow_works_with_azure(monkeypatch):

    def inner(h: BaseHTTPRequestHandler):
        if 'audience=api://AzureADTokenExchange' in h.path:
            auth = h.headers['Authorization']
            assert 'Bearer gh-actions-token' == auth
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"value": "this_is_jwt_token"}')
            return
        if '/oidc/oauth2/v2.0/authorize' == h.path:
            h.send_response(301)
            h.send_header('Location', f'http://{h.headers["Host"]}/mocked-tenant-id/irrelevant/part')
            h.end_headers()
            return
        if '/mocked-tenant-id/oauth2/token' == h.path:
            h.send_response(200)
            h.end_headers()
            h.wfile.write(b'{"expires_in": 100, "access_token": "this-is-it", "token_type": "Taker"}')

    with http_fixture_server(inner) as host:
        monkeypatch.setenv('ACTIONS_ID_TOKEN_REQUEST_URL', f'{host}/oidc')
        monkeypatch.setenv('ACTIONS_ID_TOKEN_REQUEST_TOKEN', 'gh-actions-token')
        azure_environment = AzureEnvironment(name=host,
                                             service_management_endpoint=host + '/',
                                             resource_manager_endpoint=host + '/',
                                             active_directory_endpoint=host + '/')
        databricks_environment = DatabricksEnvironment(Cloud.AZURE,
                                                       '...',
                                                       azure_environment=azure_environment)
        cfg = Config(host=host,
                     azure_workspace_resource_id=...,
                     azure_client_id='test',
                     azure_environment=host,
                     databricks_environment=databricks_environment)
        headers = cfg.authenticate()

        assert {'Authorization': 'Taker this-is-it'} == headers


@pytest.mark.parametrize(['azure_environment', 'expected'],
                         [('PUBLIC', ENVIRONMENTS['PUBLIC']), ('USGOVERNMENT', ENVIRONMENTS['USGOVERNMENT']),
                          ('CHINA', ENVIRONMENTS['CHINA']), ('public', ENVIRONMENTS['PUBLIC']),
                          ('usgovernment', ENVIRONMENTS['USGOVERNMENT']), ('china', ENVIRONMENTS['CHINA']),
                          # Kept for historical compatibility
                          ('AzurePublicCloud', ENVIRONMENTS['PUBLIC']),
                          ('AzureUSGovernment', ENVIRONMENTS['USGOVERNMENT']),
                          ('AzureChinaCloud', ENVIRONMENTS['CHINA']), ])
def test_azure_environment(azure_environment, expected):
    c = Config(credentials_strategy=noop_credentials,
               azure_workspace_resource_id='...',
               azure_environment=azure_environment)
    assert c.arm_environment == expected
