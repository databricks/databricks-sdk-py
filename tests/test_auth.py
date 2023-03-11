import functools
import pytest
from databricks.sdk.client import Config, DatabricksError


def raises(msg):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with pytest.raises(DatabricksError) as excinfo:
                func(*args, **kwargs)
            assert msg in str(excinfo.value)
        return wrapper
    return inner


@raises("default auth: cannot configure default credentials. Config: host=https://x. Env: DATABRICKS_HOST")
def test_config_host_env(monkeypatch):
    monkeypatch.setenv("DATABRICKS_HOST", "x")

    cfg = Config()
    cfg.auth()
