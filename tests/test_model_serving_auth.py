import time

import pytest

from databricks.sdk.core import Config

from .conftest import raises

default_auth_base_error_message = \
    "default auth: cannot configure default credentials, " \
    "please check https://docs.databricks.com/en/dev-tools/auth.html#databricks-client-unified-authentication " \
    "to configure credentials for your preferred authentication method"


@pytest.mark.parametrize("env_values, del_env_values, oauth_file_name",
                         [([
                             ('IS_IN_DB_MODEL_SERVING_ENV', 'true'), ('DB_MODEL_SERVING_HOST_URL', 'x')
                         ], ['DATABRICKS_MODEL_SERVING_HOST_URL'], "tests/testdata/model-serving-test-token"),
                          ([('IS_IN_DATABRICKS_MODEL_SERVING_ENV', 'true'),
                            ('DB_MODEL_SERVING_HOST_URL', 'x')], ['DATABRICKS_MODEL_SERVING_HOST_URL'],
                           "tests/testdata/model-serving-test-token"),
                          ([('IS_IN_DB_MODEL_SERVING_ENV', 'true'), ('DATABRICKS_MODEL_SERVING_HOST_URL', 'x')
                            ], ['DB_MODEL_SERVING_HOST_URL'], "tests/testdata/model-serving-test-token"),
                          ([('IS_IN_DATABRICKS_MODEL_SERVING_ENV', 'true'),
                            ('DATABRICKS_MODEL_SERVING_HOST_URL', 'x')
                            ], ['DB_MODEL_SERVING_HOST_URL'], "tests/testdata/model-serving-test-token"), ])
def test_model_serving_auth(env_values, del_env_values, oauth_file_name, monkeypatch, mocker):
    ## In mlflow we check for these two environment variables to return the correct config
    for (env_name, env_value) in env_values:
        monkeypatch.setenv(env_name, env_value)

    for (env_name) in del_env_values:
        monkeypatch.delenv(env_name, raising=False)

    # patch mlflow to read the file from the test directory
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        oauth_file_name)
    mocker.patch('databricks.sdk.config.Config._known_file_config_loader')

    cfg = Config()

    assert cfg.auth_type == 'model-serving'
    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    # Token defined in the test file
    assert headers.get("Authorization") == 'Bearer databricks_sdk_unit_test_token'


@pytest.mark.parametrize(
    "env_values, oauth_file_name",
    [
        ([], "invalid_file_name"), # Not in Model Serving and Invalid File Name
        ([('IS_IN_DB_MODEL_SERVING_ENV', 'true')
          ], "invalid_file_name"), # In Model Serving and Invalid File Name
        ([('IS_IN_DATABRICKS_MODEL_SERVING_ENV', 'true')
          ], "invalid_file_name"), # In Model Serving and Invalid File Name
        ([], "tests/testdata/model-serving-test-token") # Not in Model Serving and Valid File Name
    ])
@raises(default_auth_base_error_message)
def test_model_serving_auth_errors(env_values, oauth_file_name, monkeypatch):
    # Guarantee that the tests defaults to env variables rather than config file.
    #
    # TODO: this is hacky and we should find a better way to tell the config
    # that it should not read from the config file.
    monkeypatch.setenv('DATABRICKS_CONFIG_FILE', 'x')

    for (env_name, env_value) in env_values:
        monkeypatch.setenv(env_name, env_value)
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        oauth_file_name)

    Config()


def test_model_serving_auth_refresh(monkeypatch, mocker):
    ## In mlflow we check for these two environment variables to return the correct config
    monkeypatch.setenv('IS_IN_DB_MODEL_SERVING_ENV', 'true')
    monkeypatch.setenv('DB_MODEL_SERVING_HOST_URL', 'x')

    # patch mlflow to read the file from the test directory
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        "tests/testdata/model-serving-test-token")
    mocker.patch('databricks.sdk.config.Config._known_file_config_loader')

    cfg = Config()
    assert cfg.auth_type == 'model-serving'

    current_time = time.time()
    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    assert headers.get(
        "Authorization") == 'Bearer databricks_sdk_unit_test_token' # Token defined in the test file

    # Simulate refreshing the token by patching to to a new file
    monkeypatch.setattr(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider._MODEL_DEPENDENCY_OAUTH_TOKEN_FILE_PATH",
        "tests/testdata/model-serving-test-token-v2")

    monkeypatch.setattr('databricks.sdk.credentials_provider.time.time', lambda: current_time + 10)

    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    # Read from cache even though new path is set because expiry is still not hit
    assert headers.get("Authorization") == 'Bearer databricks_sdk_unit_test_token'

    # Expiry is 300 seconds so this should force an expiry and re read from the new file path
    monkeypatch.setattr('databricks.sdk.credentials_provider.time.time', lambda: current_time + 600)

    headers = cfg.authenticate()
    assert (cfg.host == 'x')
    # Read V2 now
    assert headers.get("Authorization") == 'Bearer databricks_sdk_unit_test_token_v2'
