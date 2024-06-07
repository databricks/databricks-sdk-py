import functools
import os

import pytest as pytest
from pyfakefs.fake_filesystem_unittest import Patcher

from databricks.sdk.core import Config
from databricks.sdk.credentials_provider import credentials_strategy

from .integration.conftest import restorable_env  # type: ignore


@credentials_strategy('noop', [])
def noop_credentials(_: any):
    return lambda: {}


@pytest.fixture
def config():
    return Config(host='http://localhost', credentials_strategy=noop_credentials)


@pytest.fixture
def w(config):
    from databricks.sdk import WorkspaceClient
    return WorkspaceClient(config=config)


__tests__ = os.path.dirname(__file__)


def raises(msg):

    def inner(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with pytest.raises(ValueError) as info:
                func(*args, **kwargs)
            exception_str = str(info.value)
            exception_str = exception_str.replace(__tests__ + '/', '')
            assert msg in exception_str

        return wrapper

    return inner


# When we apply this to a test, it'll use a fake file system instead of the local disk.
# Example usage: test_config_no_params under test_auth.py
@pytest.fixture
def fake_fs():
    with Patcher() as patcher:

        # Include the tests directory in the fake filesystem
        test_data_path = __tests__
        patcher.fs.add_real_directory(test_data_path)

        yield patcher.fs # This will return a fake file system
