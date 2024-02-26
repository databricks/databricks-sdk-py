from contextlib import contextmanager

import pytest

DBCONNECT_DBR_CLIENT = {
    "13.3": "13.3.3",
    "14.3": "14.3.1",
}

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

@pytest.fixture()
def setup_dbconnect_test(dbr: str, env_or_skip, restorable_env):
    assert dbr in DBCONNECT_DBR_CLIENT, f"Unsupported Databricks Runtime version {dbr}. Please update DBCONNECT_DBR_CLIENT."

    import os
    os.environ["DATABRICKS_CLUSTER_ID"] = env_or_skip(f"TEST_DBR_{dbr.replace('.', '_')}_DBCONNECT_CLUSTER_ID")
    
    import sys
    import subprocess
    lib = f"databricks-dbconnect=={DBCONNECT_DBR_CLIENT[dbr]}"
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    yield

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", lib])
    

@pytest.mark.parametrize("dbr", DBCONNECT_DBR_CLIENT.keys(), indirect=True)
def test_dbconnect_initialisation(w, setup_dbconnect_test):
    from databricks.connect import DatabricksSession
    spark = DatabricksSession.builder.getOrCreate()
    assert spark.sql("SELECT 1").collect()[0][0] == 1

@pytest.mark.parametrize("dbr", DBCONNECT_DBR_CLIENT.keys(), indirect=True)
def test_dbconnect_runtime_import(w, setup_dbconnect_test):
    from databricks.sdk.runtime import *
    assert spark.sql("SELECT 1").collect()[0][0] == 1

