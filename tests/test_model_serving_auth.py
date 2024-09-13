from databricks.sdk.core import Config


def test_model_serving_auth(monkeypatch):
    ## In mlflow we check for these two environment variables to return the correct config
    monkeypatch.setenv('IS_IN_DB_MODEL_SERVING_ENV', 'true')
    monkeypatch.setenv('DB_MODEL_SERVING_HOST_URL', 'x')
    # patch mlflow to read the file from the test directory
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        "tests/testdata/model-serving-test-token")

    cfg = Config()

    assert cfg.auth_type == 'model-serving'
    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    # Token defined in the test file
    assert headers.get("Authorization") == 'Bearer databricks_sdk_unit_test_token'


def test_model_serving_auth_refresh(monkeypatch):
    ## In mlflow we check for these two environment variables to return the correct config
    monkeypatch.setenv('IS_IN_DB_MODEL_SERVING_ENV', 'true')
    monkeypatch.setenv('DB_MODEL_SERVING_HOST_URL', 'x')

    # patch mlflow to read the file from the test directory
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        "tests/testdata/model-serving-test-token")

    cfg = Config()
    assert cfg.auth_type == 'model-serving'

    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    assert headers.get(
        "Authorization") == 'Bearer databricks_sdk_unit_test_token' # Token defined in the test file

    # Simulate refreshing the token by patching to to a new file
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        "tests/testdata/model-serving-test-token-v2")

    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    assert headers.get("Authorization") == 'Bearer databricks_sdk_unit_test_token_v2' # Read V2 now
