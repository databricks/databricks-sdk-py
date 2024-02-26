import pytest

DBCONNECT_DBR_CLIENT = {"13.3": "13.3.3", "14.3": "14.3.1", }


@pytest.fixture(scope="function")
def reload_modules():
    """
    Returns a function that can be used to reload modules. This is useful when testing
    Databricks Connect, since both the `databricks.connect` and `databricks.sdk.runtime` modules
    are stateful, and we need to reload these modules to reset the state cache between test runs.
    """
    import importlib
    import sys

    def reload(name: str):
        v = sys.modules.get(name)
        if v is None:
            return
        try:
            print(f"Reloading {name}")
            importlib.reload(v)
        except Exception as e:
            print(f"Failed to reload {name}: {e}")

    return reload


@pytest.fixture(scope="function")
def restorable_env():
    import os
    current_env = os.environ.copy()
    yield
    for k, v in os.environ.items():
        if k not in current_env:
            del os.environ[k]
        elif v != current_env[k]:
            os.environ[k] = current_env[k]


@pytest.fixture(params=list(DBCONNECT_DBR_CLIENT.keys()))
def setup_dbconnect_test(request, env_or_skip, restorable_env):
    dbr = request.param
    assert dbr in DBCONNECT_DBR_CLIENT, f"Unsupported Databricks Runtime version {dbr}. Please update DBCONNECT_DBR_CLIENT."

    import os
    os.environ["DATABRICKS_CLUSTER_ID"] = env_or_skip(
        f"TEST_DBR_{dbr.replace('.', '_')}_DBCONNECT_CLUSTER_ID")

    import subprocess
    import sys
    lib = f"databricks-connect=={DBCONNECT_DBR_CLIENT[dbr]}"
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    yield

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "databricks-connect"])


@pytest.mark.xdist_group(name="databricks-connect")
def test_dbconnect_initialisation(w, setup_dbconnect_test, reload_modules):
    reload_modules("databricks.connect")
    from databricks.connect import DatabricksSession
    reload_modules("databricks.connect")

    spark = DatabricksSession.builder.getOrCreate()
    assert spark.sql("SELECT 1").collect()[0][0] == 1


@pytest.mark.xdist_group(name="databricks-connect")
def test_dbconnect_runtime_import(w, setup_dbconnect_test, reload_modules):
    reload_modules("databricks.sdk.runtime")
    from databricks.sdk.runtime import spark

    assert spark.sql("SELECT 1").collect()[0][0] == 1


@pytest.mark.xdist_group(name="databricks-connect")
def test_dbconnect_runtime_import_no_error_if_doesnt_exist(w, reload_modules):
    reload_modules("databricks.sdk.runtime")
    from databricks.sdk.runtime import spark

    assert spark is None
