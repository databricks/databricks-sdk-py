import os
import pathlib
import platform
import random
import string

import pytest

from databricks.sdk.core import (Config, CredentialsProvider,
                                 DatabricksCliTokenSource, HeaderFactory,
                                 databricks_cli)
from databricks.sdk.version import __version__


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


def write_small_dummy_executable(path: pathlib.Path):
    cli = path.joinpath('databricks')
    cli.write_text('#!/bin/sh\necho "hello world"\n')
    cli.chmod(0o755)
    assert cli.stat().st_size < 1024
    return cli


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

    (dir1 / "databricks").symlink_to(write_small_dummy_executable(dir2))

    monkeypatch.setenv('PATH', dir1.as_posix())
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


def test_databricks_cli_credential_provider_installed_new(config, monkeypatch, tmp_path):
    write_large_dummy_executable(tmp_path)
    monkeypatch.setenv('PATH', str(os.pathsep).join([tmp_path.as_posix(), os.environ['PATH']]))
    assert databricks_cli(config) is not None


def test_extra_and_upstream_user_agent(monkeypatch):

    class MockUname:

        @property
        def system(self):
            return 'TestOS'

    monkeypatch.setattr(platform, 'python_version', lambda: '3.0.0')
    monkeypatch.setattr(platform, 'uname', MockUname)
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM', "upstream-product")
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM_VERSION', "0.0.1")

    config = Config(host='http://localhost', username="something", password="something", product='test',
                    product_version='0.0.0') \
        .with_user_agent_extra('test-extra-1', '1') \
        .with_user_agent_extra('test-extra-2', '2')

    assert config.user_agent == (
        f"test/0.0.0 databricks-sdk-py/{__version__} python/3.0.0 os/testos auth/basic"
        f" test-extra-1/1 test-extra-2/2 upstream/upstream-product upstream-version/0.0.1")


def test_config_copy_shallow_copies_credential_provider():

    class TestCredentialsProvider(CredentialsProvider):

        def __init__(self):
            super().__init__()
            self._token = "token1"

        def auth_type(self) -> str:
            return "test"

        def __call__(self, cfg: 'Config') -> HeaderFactory:
            return lambda: {"token": self._token}

        def refresh(self):
            self._token = "token2"

    credential_provider = TestCredentialsProvider()
    config = Config(credentials_provider=credential_provider)
    config_copy = config.copy()

    assert config.authenticate()["token"] == "token1"
    assert config_copy.authenticate()["token"] == "token1"

    credential_provider.refresh()

    assert config.authenticate()["token"] == "token2"
    assert config_copy.authenticate()["token"] == "token2"
    assert config._credentials_provider == config_copy._credentials_provider


def test_config_copy_deep_copies_user_agent_other_info(config):
    config_copy = config.copy()

    config.with_user_agent_extra("test", "test1")
    assert "test/test1" not in config_copy.user_agent
    assert "test/test1" in config.user_agent

    config_copy.with_user_agent_extra("test", "test2")
    assert "test/test2" in config_copy.user_agent
    assert "test/test2" not in config.user_agent


def test_config_accounts_aws_is_accounts_host(config):
    config.host = "https://accounts.cloud.databricks.com"
    assert config.is_account_client


def test_config_accounts_dod_is_accounts_host(config):
    config.host = "https://accounts-dod.cloud.databricks.us"
    assert config.is_account_client


def test_config_workspace_is_not_accounts_host(config):
    config.host = "https://westeurope.azuredatabricks.net"
    assert not config.is_account_client
