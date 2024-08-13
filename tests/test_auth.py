# These are auto-generated tests for Unified Authentication
# In case of editing this file, make sure the change is propagated to all Databricks SDK codebases
from databricks.sdk.core import Config

from .conftest import __tests__, raises, set_az_path, set_home

default_auth_base_error_message = \
    "default auth: cannot configure default credentials, " \
    "please check https://docs.databricks.com/en/dev-tools/auth.html#databricks-client-unified-authentication " \
    "to configure credentials for your preferred authentication method"


# This test uses the fake file system to avoid interference from local default profile.
@raises(default_auth_base_error_message)
def test_config_no_params(fake_fs):
    Config()


@raises(f"{default_auth_base_error_message}. Config: host=https://x. Env: DATABRICKS_HOST")
def test_config_host_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    Config()


@raises(f"{default_auth_base_error_message}. Config: token=***. Env: DATABRICKS_TOKEN")
def test_config_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    Config()


def test_config_host_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://x'


def test_config_host_param_token_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    cfg = Config(host='https://x')

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://x'


@raises(
    f"{default_auth_base_error_message}. Config: username=x, password=***. Env: DATABRICKS_USERNAME, DATABRICKS_PASSWORD"
)
def test_config_user_password_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config()

    assert cfg.host == 'https://x'


def test_config_basic_auth(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config()

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'


def test_config_attribute_precedence(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config(host='y')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


def test_config_basic_auth_mix(monkeypatch):
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    cfg = Config(host='y', username='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


def test_config_basic_auth_attrs():
    cfg = Config(host='y', username='x', password='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://y'


@raises(
    "validate: more than one authorization method configured: basic and pat. Config: host=https://x, token=***, username=x, password=***. Env: DATABRICKS_HOST, DATABRICKS_TOKEN, DATABRICKS_USERNAME, DATABRICKS_PASSWORD"
)
def test_config_conflicting_envs(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    Config()


def test_config_conflicting_envs_auth_type(monkeypatch):
    monkeypatch.setenv('DATABRICKS_HOST', 'x')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'x')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    cfg = Config(auth_type='basic')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'


@raises(f"{default_auth_base_error_message}. Config: config_file=x. Env: DATABRICKS_CONFIG_FILE")
def test_config_config_file(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_FILE', 'x')
    Config()


@raises(f"{default_auth_base_error_message}. Config: host=https://x")
def test_config_config_file_skip_default_profile_if_host_specified(monkeypatch):
    set_home(monkeypatch, '/testdata')
    cfg = Config(host='x')


@raises(default_auth_base_error_message)
def test_config_config_file_with_empty_default_profile_select_default(monkeypatch):
    set_home(monkeypatch, '/testdata/empty_default')
    Config()


def test_config_config_file_with_empty_default_profile_select_abc(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'abc')
    set_home(monkeypatch, '/testdata/empty_default')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://foo'


def test_config_pat_from_databricks_cfg(monkeypatch):
    set_home(monkeypatch, '/testdata')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://dbc-XXXXXXXX-YYYY.cloud.databricks.com'


def test_config_pat_from_databricks_cfg_dot_profile(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'pat.with.dot')
    set_home(monkeypatch, '/testdata')
    cfg = Config()

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://dbc-XXXXXXXX-YYYY.cloud.databricks.com'


@raises(
    f"{default_auth_base_error_message}. Config: token=***, profile=nohost. Env: DATABRICKS_CONFIG_PROFILE")
def test_config_pat_from_databricks_cfg_nohost_profile(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    set_home(monkeypatch, '/testdata')
    Config()


@raises(
    f"{default_auth_base_error_message}. Config: token=***, profile=nohost. Env: DATABRICKS_TOKEN, DATABRICKS_CONFIG_PROFILE"
)
def test_config_config_profile_and_token(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'x')
    set_home(monkeypatch, '/testdata')
    Config()


@raises(
    "validate: more than one authorization method configured: basic and pat. Config: token=***, username=x, profile=nohost. Env: DATABRICKS_USERNAME, DATABRICKS_CONFIG_PROFILE"
)
def test_config_config_profile_and_password(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'nohost')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    set_home(monkeypatch, '/testdata')
    Config()


def test_config_azure_pat():
    cfg = Config(host='https://adb-xxx.y.azuredatabricks.net/', token='y')

    assert cfg.auth_type == 'pat'
    assert cfg.host == 'https://adb-xxx.y.azuredatabricks.net'
    assert cfg.is_azure


def test_config_azure_cli_host(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    cfg = Config(host='https://adb-123.4.azuredatabricks.net', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://adb-123.4.azuredatabricks.net'
    assert cfg.is_azure


@raises(
    "default auth: cannot configure default credentials, please check https://docs.databricks.com/en/dev-tools/auth.html#databricks-client-unified-authentication to configure credentials for your preferred authentication method. Config: azure_workspace_resource_id=/sub/rg/ws"
)
def test_config_azure_cli_host_fail(monkeypatch):
    monkeypatch.setenv('FAIL', 'yes')
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    cfg = Config(azure_workspace_resource_id='/sub/rg/ws')


@raises(f"{default_auth_base_error_message}. Config: azure_workspace_resource_id=/sub/rg/ws")
def test_config_azure_cli_host_az_not_installed(monkeypatch):
    set_home(monkeypatch, '/testdata/azure')
    monkeypatch.setenv('PATH', __tests__ + '/whatever')
    cfg = Config(azure_workspace_resource_id='/sub/rg/ws')


@raises(
    "validate: more than one authorization method configured: azure and pat. Config: token=***, azure_workspace_resource_id=/sub/rg/ws"
)
def test_config_azure_cli_host_pat_conflict_with_config_file_present_without_default_profile(monkeypatch):
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    cfg = Config(token='x', azure_workspace_resource_id='/sub/rg/ws')


def test_config_azure_cli_host_and_resource_id(monkeypatch, mock_tenant):
    set_home(monkeypatch, '/testdata')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    cfg = Config(host='https://adb-123.4.azuredatabricks.net', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://adb-123.4.azuredatabricks.net'
    assert cfg.is_azure


def test_config_azure_cli_host_and_resource_i_d_configuration_precedence(monkeypatch, mock_tenant):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'justhost')
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    mock_tenant('adb-123.4.azuredatabricks.net')
    cfg = Config(host='https://adb-123.4.azuredatabricks.net', azure_workspace_resource_id='/sub/rg/ws')

    assert cfg.auth_type == 'azure-cli'
    assert cfg.host == 'https://adb-123.4.azuredatabricks.net'
    assert cfg.is_azure


@raises(
    "validate: more than one authorization method configured: azure and basic. Config: host=https://adb-123.4.azuredatabricks.net, username=x, azure_workspace_resource_id=/sub/rg/ws. Env: DATABRICKS_USERNAME"
)
def test_config_azure_and_password_conflict(monkeypatch):
    monkeypatch.setenv('DATABRICKS_USERNAME', 'x')
    set_home(monkeypatch, '/testdata/azure')
    set_az_path(monkeypatch)
    cfg = Config(host='https://adb-123.4.azuredatabricks.net', azure_workspace_resource_id='/sub/rg/ws')


@raises(
    "resolve: testdata/corrupt/.databrickscfg has no DEFAULT profile configured. Config: profile=DEFAULT. Env: DATABRICKS_CONFIG_PROFILE"
)
def test_config_corrupt_config(monkeypatch):
    monkeypatch.setenv('DATABRICKS_CONFIG_PROFILE', 'DEFAULT')
    set_home(monkeypatch, '/testdata/corrupt')
    Config()


def test_config_auth_type_from_env(monkeypatch):
    monkeypatch.setenv('DATABRICKS_AUTH_TYPE', 'basic')
    monkeypatch.setenv('DATABRICKS_PASSWORD', 'password')
    monkeypatch.setenv('DATABRICKS_TOKEN', 'token')
    monkeypatch.setenv('DATABRICKS_USERNAME', 'user')
    cfg = Config(host='x')

    assert cfg.auth_type == 'basic'
    assert cfg.host == 'https://x'
