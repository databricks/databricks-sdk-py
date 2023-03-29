import functools
import os

import pytest as pytest

from databricks.sdk.core import Config, credentials_provider


@credentials_provider('noop', [])
def noop_credentials(_: any):
    return lambda: {}


@pytest.fixture
def config():
    return Config(host='http://localhost', credentials_provider=noop_credentials)


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