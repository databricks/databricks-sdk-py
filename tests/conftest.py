import functools
import os
import platform

import pytest as pytest  # type: ignore[import-not-found]
from pyfakefs.fake_filesystem_unittest import \
    Patcher  # type: ignore[import-not-found]

from databricks.sdk.core import Config
from databricks.sdk.credentials_provider import credentials_strategy

from .clock import FakeClock


@credentials_strategy("noop", [])  # type: ignore[misc]
def noop_credentials(_: any):  # type: ignore[no-untyped-def, valid-type]
    return lambda: {}


@pytest.fixture
def config():  # type: ignore[no-untyped-def]
    return Config(host="http://localhost", credentials_strategy=noop_credentials, clock=FakeClock())


@pytest.fixture
def w(config):  # type: ignore[no-untyped-def]
    from databricks.sdk import WorkspaceClient

    return WorkspaceClient(config=config)


__tests__ = os.path.dirname(__file__)


def raises(msg):  # type: ignore[no-untyped-def]

    def inner(func):  # type: ignore[no-untyped-def]

        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
            with pytest.raises(ValueError) as info:
                func(*args, **kwargs)
            exception_str = str(info.value)
            if platform.system() == "Windows":
                exception_str = exception_str.replace(__tests__ + "\\", "")
                exception_str = exception_str.replace("\\", "/")
            else:
                exception_str = exception_str.replace(__tests__ + "/", "")
            assert msg in exception_str

        return wrapper

    return inner


# When we apply this to a test, it'll use a fake file system instead of the local disk.
# Example usage: test_config_no_params under test_auth.py
@pytest.fixture
def fake_fs():  # type: ignore[no-untyped-def]
    with Patcher() as patcher:

        # Include the tests directory in the fake filesystem
        test_data_path = __tests__
        patcher.fs.add_real_directory(test_data_path)

        yield patcher.fs  # This will return a fake file system


def set_home(monkeypatch, path):  # type: ignore[no-untyped-def]
    if platform.system() == "Windows":
        monkeypatch.setenv("USERPROFILE", __tests__ + path)
    else:
        monkeypatch.setenv("HOME", __tests__ + path)


def set_az_path(monkeypatch):  # type: ignore[no-untyped-def]
    if platform.system() == "Windows":
        monkeypatch.setenv("Path", __tests__ + "\\testdata\\windows\\")
        monkeypatch.setenv(
            "COMSPEC",
            "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        )
    else:
        monkeypatch.setenv("PATH", __tests__ + "/testdata:/bin")


@pytest.fixture
def mock_tenant(requests_mock):  # type: ignore[no-untyped-def]

    def stub_tenant_request(host, tenant_id="test-tenant-id"):  # type: ignore[no-untyped-def]
        mock = requests_mock.get(
            f"https://{host}/aad/auth",
            status_code=302,
            headers={"Location": f"https://login.microsoftonline.com/{tenant_id}/oauth2/authorize"},
        )
        return mock

    return stub_tenant_request
