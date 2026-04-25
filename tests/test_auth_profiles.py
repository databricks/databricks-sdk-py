"""Parametrized unit tests for auth types across host profiles.

Tests that each auth type resolves correctly on every applicable host profile:
- LW  = Legacy Workspace: host=workspace_url
- NW  = New Workspace:    host=workspace_url + account_id + workspace_id
- LA  = Legacy Account:   host=accounts_url + account_id
- NA  = New Account:      host=accounts_url + account_id (structurally same as LA)
- SPOGW = SPOG workspace: host=unified_url + account_id + workspace_id
- SPOGA = SPOG account:   host=unified_url + account_id
"""

import re

import pytest

from databricks.sdk.core import Config
from databricks.sdk.oauth import Cloud, HostMetadata

# -- Profile definitions -------------------------------------------------------

WORKSPACE_HOST = "https://test-workspace.cloud.databricks.com"
ACCOUNTS_HOST = "https://accounts.cloud.databricks.com"
UNIFIED_HOST = "https://db-test.cloud.databricks.com"
ACCOUNT_ID = "test-account-id"
WORKSPACE_ID = "1234567890"

# Host metadata returned for each profile type.
# LW/NW use workspace-level OIDC; LA/NA use account-level OIDC; SPOG uses account-level OIDC.
_METADATA = {
    "LW": HostMetadata(
        oidc_endpoint=f"{WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
    "NW": HostMetadata(
        oidc_endpoint=f"{WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
    "LA": HostMetadata(
        oidc_endpoint=f"{ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
    "NA": HostMetadata(
        oidc_endpoint=f"{ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
    "SPOGW": HostMetadata(
        oidc_endpoint=f"{UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
    "SPOGA": HostMetadata(
        oidc_endpoint=f"{UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AWS,
    ),
}


def _profile_config_kwargs(profile: str) -> dict:
    """Return the Config constructor kwargs for a given profile (excluding auth-specific ones)."""
    if profile == "LW":
        return {"host": WORKSPACE_HOST}
    elif profile == "NW":
        return {"host": WORKSPACE_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "LA":
        return {"host": ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "NA":
        return {"host": ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "SPOGW":
        return {"host": UNIFIED_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "SPOGA":
        return {"host": UNIFIED_HOST, "account_id": ACCOUNT_ID}
    raise ValueError(f"Unknown profile: {profile}")


def _oidc_discovery_url(profile: str) -> str:
    """Return the OIDC discovery URL for the profile."""
    meta = _METADATA[profile]
    base = meta.oidc_endpoint.replace("{account_id}", ACCOUNT_ID).rstrip("/")
    return f"{base}/.well-known/oauth-authorization-server"


def _token_endpoint(profile: str) -> str:
    """Return the token endpoint for the profile."""
    meta = _METADATA[profile]
    base = meta.oidc_endpoint.replace("{account_id}", ACCOUNT_ID).rstrip("/")
    return f"{base}/v1/token"


# -- Helpers -------------------------------------------------------------------


def _mock_metadata(mocker, profile: str):
    """Patch get_host_metadata to return the correct metadata for the given profile."""
    mocker.patch("databricks.sdk.config.get_host_metadata", return_value=_METADATA[profile])


def _mock_oidc_and_token(requests_mock, profile: str):
    """Mock the OIDC discovery and token endpoints for OAuth-based auth types."""
    discovery_url = _oidc_discovery_url(profile)
    token_url = _token_endpoint(profile)
    requests_mock.get(
        discovery_url,
        json={
            "authorization_endpoint": token_url.replace("/token", "/authorize"),
            "token_endpoint": token_url,
        },
    )
    requests_mock.post(
        token_url,
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )


# -- Auth types: simple (no OIDC mocking needed) ------------------------------

ALL_WORKSPACE_PROFILES = ["LW", "NW", "SPOGW"]
ALL_ACCOUNT_PROFILES = ["LA", "NA", "SPOGA"]
ALL_PROFILES = ALL_WORKSPACE_PROFILES + ALL_ACCOUNT_PROFILES


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_pat_auth(mocker, profile):
    _mock_metadata(mocker, profile)
    kwargs = _profile_config_kwargs(profile)
    cfg = Config(**kwargs, token="dapi1234567890abcdef")
    assert cfg.auth_type == "pat"


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_basic_auth(mocker, profile):
    _mock_metadata(mocker, profile)
    kwargs = _profile_config_kwargs(profile)
    cfg = Config(**kwargs, username="user", password="pass")
    assert cfg.auth_type == "basic"


# -- Auth types: OAuth (need OIDC + token mocking) ----------------------------


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_oauth_m2m(mocker, requests_mock, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)
    cfg = Config(**kwargs, client_id="test-client", client_secret="test-secret", auth_type="oauth-m2m")
    assert cfg.auth_type == "oauth-m2m"


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_databricks_cli(mocker, requests_mock, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)

    from databricks.sdk.oauth import Token

    mock_token = Token(access_token="test-token", token_type="Bearer")
    mock_source = mocker.Mock()
    mock_source.token.return_value = mock_token
    mocker.patch(
        "databricks.sdk.credentials_provider.DatabricksCliTokenSource",
        return_value=mock_source,
    )
    cfg = Config(**kwargs, auth_type="databricks-cli")
    assert cfg.auth_type == "databricks-cli"


# -- OIDC token auth types ----------------------------------------------------


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_env_oidc(mocker, requests_mock, monkeypatch, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)
    # env-oidc needs an OIDC token env var and a client_id
    monkeypatch.setenv("DATABRICKS_OIDC_TOKEN", "test-oidc-token")
    cfg = Config(**kwargs, client_id="test-client", auth_type="env-oidc")
    assert cfg.auth_type == "env-oidc"


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_file_oidc(mocker, requests_mock, tmp_path, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)
    # file-oidc needs an OIDC token file and a client_id
    token_file = tmp_path / "oidc_token"
    token_file.write_text("test-oidc-token")
    cfg = Config(**kwargs, client_id="test-client", oidc_token_filepath=str(token_file), auth_type="file-oidc")
    assert cfg.auth_type == "file-oidc"


@pytest.mark.parametrize("profile", ALL_PROFILES)
def test_github_oidc(mocker, requests_mock, monkeypatch, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)
    # github-oidc needs ACTIONS_ID_TOKEN_REQUEST_URL and _TOKEN env vars
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", "https://token.actions.githubusercontent.com")
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "test-github-token")
    # Mock the GitHub token request (URL gets audience appended as query param)
    requests_mock.register_uri(
        "GET",
        re.compile(r"https://token\.actions\.githubusercontent\.com.*"),
        json={"value": "test-oidc-token"},
    )
    cfg = Config(**kwargs, client_id="test-client", auth_type="github-oidc")
    assert cfg.auth_type == "github-oidc"


# -- Azure auth types ---------------------------------------------------------

AZURE_WORKSPACE_HOST = "https://adb-1234567890.12.azuredatabricks.net"
AZURE_ACCOUNTS_HOST = "https://accounts.azuredatabricks.net"
AZURE_UNIFIED_HOST = "https://db-test.azuredatabricks.net"

AZURE_WORKSPACE_PROFILES = ["AZ_LW", "AZ_NW", "AZ_SPOGW"]
AZURE_ACCOUNT_PROFILES = ["AZ_LA", "AZ_NA", "AZ_SPOGA"]
AZURE_ALL_PROFILES = AZURE_WORKSPACE_PROFILES + AZURE_ACCOUNT_PROFILES

_AZURE_METADATA = {
    "AZ_LW": HostMetadata(
        oidc_endpoint=f"{AZURE_WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
    "AZ_NW": HostMetadata(
        oidc_endpoint=f"{AZURE_WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
    "AZ_LA": HostMetadata(
        oidc_endpoint=f"{AZURE_ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
    "AZ_NA": HostMetadata(
        oidc_endpoint=f"{AZURE_ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
    "AZ_SPOGW": HostMetadata(
        oidc_endpoint=f"{AZURE_UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
    "AZ_SPOGA": HostMetadata(
        oidc_endpoint=f"{AZURE_UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.AZURE,
    ),
}


def _azure_profile_config_kwargs(profile: str) -> dict:
    if profile == "AZ_LW":
        return {"host": AZURE_WORKSPACE_HOST}
    elif profile == "AZ_NW":
        return {"host": AZURE_WORKSPACE_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "AZ_LA":
        return {"host": AZURE_ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "AZ_NA":
        return {"host": AZURE_ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "AZ_SPOGW":
        return {"host": AZURE_UNIFIED_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "AZ_SPOGA":
        return {"host": AZURE_UNIFIED_HOST, "account_id": ACCOUNT_ID}
    raise ValueError(f"Unknown profile: {profile}")


def _azure_mock_metadata(mocker, profile: str):
    mocker.patch("databricks.sdk.config.get_host_metadata", return_value=_AZURE_METADATA[profile])


def _azure_oidc_discovery_url(profile: str) -> str:
    meta = _AZURE_METADATA[profile]
    base = meta.oidc_endpoint.replace("{account_id}", ACCOUNT_ID).rstrip("/")
    return f"{base}/.well-known/oauth-authorization-server"


def _azure_token_endpoint(profile: str) -> str:
    meta = _AZURE_METADATA[profile]
    base = meta.oidc_endpoint.replace("{account_id}", ACCOUNT_ID).rstrip("/")
    return f"{base}/v1/token"


def _azure_mock_oidc_and_token(requests_mock, profile: str):
    discovery_url = _azure_oidc_discovery_url(profile)
    token_url = _azure_token_endpoint(profile)
    requests_mock.get(
        discovery_url,
        json={
            "authorization_endpoint": token_url.replace("/token", "/authorize"),
            "token_endpoint": token_url,
        },
    )
    requests_mock.post(
        token_url,
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )


def _azure_mock_tenant(requests_mock, host: str):
    requests_mock.get(
        f"{host}/aad/auth",
        status_code=302,
        headers={"Location": "https://login.microsoftonline.com/test-tenant-id/oauth2/authorize"},
    )


@pytest.mark.parametrize("profile", AZURE_ALL_PROFILES)
def test_azure_client_secret(mocker, requests_mock, profile):
    _azure_mock_metadata(mocker, profile)
    kwargs = _azure_profile_config_kwargs(profile)
    host = kwargs["host"]
    _azure_mock_tenant(requests_mock, host)
    # Mock AAD token endpoint
    requests_mock.post(
        "https://login.microsoftonline.com/test-tenant-id/oauth2/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )
    cfg = Config(
        **kwargs,
        azure_client_id="test-azure-client",
        azure_client_secret="test-azure-secret",
        azure_tenant_id="test-tenant-id",
        auth_type="azure-client-secret",
    )
    assert cfg.auth_type == "azure-client-secret"


@pytest.mark.parametrize("profile", AZURE_ALL_PROFILES)
def test_azure_cli(mocker, requests_mock, profile):
    _azure_mock_metadata(mocker, profile)
    kwargs = _azure_profile_config_kwargs(profile)
    host = kwargs["host"]
    _azure_mock_tenant(requests_mock, host)
    # Mock the AzureCliTokenSource to avoid actually calling `az`
    from databricks.sdk.oauth import Token

    mock_token = Token(access_token="test-token", token_type="Bearer")
    mock_source = mocker.Mock()
    mock_source.token.return_value = mock_token
    mocker.patch(
        "databricks.sdk.credentials_provider.AzureCliTokenSource",
        return_value=mock_source,
    )
    cfg = Config(**kwargs, auth_type="azure-cli")
    assert cfg.auth_type == "azure-cli"


@pytest.mark.parametrize("profile", AZURE_ALL_PROFILES)
def test_github_oidc_azure(mocker, requests_mock, monkeypatch, profile):
    _azure_mock_metadata(mocker, profile)
    _azure_mock_oidc_and_token(requests_mock, profile)
    kwargs = _azure_profile_config_kwargs(profile)
    host = kwargs["host"]
    _azure_mock_tenant(requests_mock, host)
    # github-oidc-azure needs GitHub OIDC env vars + Azure client ID
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_URL", "https://token.actions.githubusercontent.com")
    monkeypatch.setenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN", "test-github-token")
    requests_mock.register_uri(
        "GET",
        re.compile(r"https://token\.actions\.githubusercontent\.com.*"),
        json={"value": "test-oidc-token"},
    )
    # Mock AAD token endpoint for the OIDC federated exchange
    requests_mock.post(
        "https://login.microsoftonline.com/test-tenant-id/oauth2/v2.0/token",
        json={"access_token": "test-token", "token_type": "Bearer", "expires_in": 3600},
    )
    cfg = Config(
        **kwargs,
        azure_client_id="test-azure-client",
        azure_tenant_id="test-tenant-id",
        auth_type="github-oidc-azure",
    )
    assert cfg.auth_type == "github-oidc-azure"


@pytest.mark.parametrize("profile", AZURE_ALL_PROFILES)
def test_azure_devops_oidc(mocker, requests_mock, monkeypatch, profile):
    _azure_mock_metadata(mocker, profile)
    _azure_mock_oidc_and_token(requests_mock, profile)
    kwargs = _azure_profile_config_kwargs(profile)
    host = kwargs["host"]
    _azure_mock_tenant(requests_mock, host)
    # Mock the OIDC token supplier to avoid real Azure DevOps env vars
    mock_supplier = mocker.Mock()
    mock_supplier.get_oidc_token.return_value = "test-oidc-token"
    mocker.patch(
        "databricks.sdk.credentials_provider.oidc_token_supplier.AzureDevOpsOIDCTokenSupplier",
        return_value=mock_supplier,
    )
    cfg = Config(
        **kwargs,
        client_id="test-client",
        auth_type="azure-devops-oidc",
    )
    assert cfg.auth_type == "azure-devops-oidc"


# -- GCP auth types ------------------------------------------------------------

GCP_WORKSPACE_HOST = "https://1234567890.1.gcp.databricks.com"
GCP_ACCOUNTS_HOST = "https://accounts.gcp.databricks.com"
GCP_UNIFIED_HOST = "https://db-test.gcp.databricks.com"

GCP_WORKSPACE_PROFILES = ["GCP_LW", "GCP_NW", "GCP_SPOGW"]
GCP_ACCOUNT_PROFILES = ["GCP_LA", "GCP_NA", "GCP_SPOGA"]
GCP_ALL_PROFILES = GCP_WORKSPACE_PROFILES + GCP_ACCOUNT_PROFILES

_GCP_METADATA = {
    "GCP_LW": HostMetadata(
        oidc_endpoint=f"{GCP_WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
    "GCP_NW": HostMetadata(
        oidc_endpoint=f"{GCP_WORKSPACE_HOST}/oidc",
        workspace_id=WORKSPACE_ID,
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
    "GCP_LA": HostMetadata(
        oidc_endpoint=f"{GCP_ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
    "GCP_NA": HostMetadata(
        oidc_endpoint=f"{GCP_ACCOUNTS_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
    "GCP_SPOGW": HostMetadata(
        oidc_endpoint=f"{GCP_UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
    "GCP_SPOGA": HostMetadata(
        oidc_endpoint=f"{GCP_UNIFIED_HOST}/oidc/accounts/{{account_id}}",
        account_id=ACCOUNT_ID,
        cloud=Cloud.GCP,
    ),
}


def _gcp_profile_config_kwargs(profile: str) -> dict:
    if profile == "GCP_LW":
        return {"host": GCP_WORKSPACE_HOST}
    elif profile == "GCP_NW":
        return {"host": GCP_WORKSPACE_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "GCP_LA":
        return {"host": GCP_ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "GCP_NA":
        return {"host": GCP_ACCOUNTS_HOST, "account_id": ACCOUNT_ID}
    elif profile == "GCP_SPOGW":
        return {"host": GCP_UNIFIED_HOST, "account_id": ACCOUNT_ID, "workspace_id": WORKSPACE_ID}
    elif profile == "GCP_SPOGA":
        return {"host": GCP_UNIFIED_HOST, "account_id": ACCOUNT_ID}
    raise ValueError(f"Unknown profile: {profile}")


def _gcp_mock_metadata(mocker, profile: str):
    mocker.patch("databricks.sdk.config.get_host_metadata", return_value=_GCP_METADATA[profile])


@pytest.mark.parametrize("profile", GCP_ALL_PROFILES)
def test_google_credentials(mocker, profile):
    _gcp_mock_metadata(mocker, profile)
    kwargs = _gcp_profile_config_kwargs(profile)
    # Mock the Google library so we don't need a real service account key
    mock_creds = mocker.Mock()
    mocker.patch(
        "google.oauth2.service_account.IDTokenCredentials.from_service_account_info",
        return_value=mock_creds,
    )
    mocker.patch(
        "google.oauth2.service_account.Credentials.from_service_account_info",
        return_value=mocker.Mock(),
    )
    cfg = Config(**kwargs, google_credentials='{"type":"service_account"}', auth_type="google-credentials")
    assert cfg.auth_type == "google-credentials"


@pytest.mark.parametrize("profile", GCP_ALL_PROFILES)
def test_google_id(mocker, profile):
    _gcp_mock_metadata(mocker, profile)
    kwargs = _gcp_profile_config_kwargs(profile)
    # google-id uses default application credentials + impersonation.
    # Mock the google.auth.default call.
    mock_creds = mocker.Mock()
    mocker.patch("google.auth.default", return_value=(mock_creds, "test-project"))
    cfg = Config(**kwargs, google_service_account="test@test-project.iam.gserviceaccount.com", auth_type="google-id")
    assert cfg.auth_type == "google-id"


# -- Environment-locked auth types ---------------------------------------------


@pytest.mark.parametrize("profile", ALL_WORKSPACE_PROFILES)
def test_metadata_service(mocker, requests_mock, profile):
    _mock_metadata(mocker, profile)
    import time

    kwargs = _profile_config_kwargs(profile)
    requests_mock.get(
        "http://169.254.169.254/metadata",
        json={
            "access_token": "test-token",
            "token_type": "Bearer",
            "expires_on": time.time() + 3600,
        },
    )
    cfg = Config(
        **kwargs,
        metadata_service_url="http://169.254.169.254/metadata",
        auth_type="metadata-service",
    )
    assert cfg.auth_type == "metadata-service"


def _mock_runtime_module(mocker, monkeypatch, host):
    """Set up mocks for the runtime auth dynamic import."""
    monkeypatch.setenv("DATABRICKS_RUNTIME_VERSION", "15.0")
    mock_inner = mocker.Mock(return_value={"Authorization": "Bearer test-token"})

    def mock_init_native():
        return (host, mock_inner)

    mock_runtime = mocker.Mock()
    mock_runtime.init_runtime_native_auth = mock_init_native
    mock_runtime.init_runtime_repl_auth = None
    mock_runtime.init_runtime_legacy_auth = None
    mock_runtime.init_runtime_native_unified = None
    mocker.patch.dict("sys.modules", {"databricks.sdk.runtime": mock_runtime})


@pytest.mark.parametrize("profile", ALL_WORKSPACE_PROFILES)
def test_runtime(mocker, monkeypatch, profile):
    _mock_metadata(mocker, profile)
    kwargs = _profile_config_kwargs(profile)
    _mock_runtime_module(mocker, monkeypatch, kwargs["host"])
    cfg = Config(**kwargs, auth_type="runtime")
    assert cfg.auth_type == "runtime"


@pytest.mark.parametrize("profile", ALL_WORKSPACE_PROFILES)
def test_runtime_oauth(mocker, requests_mock, monkeypatch, profile):
    _mock_metadata(mocker, profile)
    _mock_oidc_and_token(requests_mock, profile)
    kwargs = _profile_config_kwargs(profile)
    _mock_runtime_module(mocker, monkeypatch, kwargs["host"])
    # Mock the PAT-to-OAuth token exchange
    from databricks.sdk.oauth import Token

    mock_token = Token(access_token="test-oauth-token", token_type="Bearer")
    mocker.patch(
        "databricks.sdk.oauth.PATOAuthTokenExchange.token",
        return_value=mock_token,
    )
    cfg = Config(**kwargs, auth_type="runtime-oauth", scopes=["all-apis"])
    assert cfg.auth_type == "runtime-oauth"


@pytest.mark.parametrize("profile", ALL_WORKSPACE_PROFILES)
def test_model_serving(mocker, monkeypatch, profile):
    _mock_metadata(mocker, profile)
    kwargs = _profile_config_kwargs(profile)
    monkeypatch.setenv("IS_IN_DB_MODEL_SERVING_ENV", "true")
    monkeypatch.setenv("DB_MODEL_SERVING_HOST_URL", kwargs["host"])
    # Mock ModelServingAuthProvider
    mock_provider = mocker.Mock()
    mock_provider.get_databricks_host_token.return_value = (kwargs["host"], "test-token")
    mocker.patch(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider",
        return_value=mock_provider,
    )
    mocker.patch(
        "databricks.sdk.credentials_provider.ModelServingAuthProvider.should_fetch_model_serving_environment_oauth",
        return_value=True,
    )
    cfg = Config(**kwargs, auth_type="model-serving")
    assert cfg.auth_type == "model-serving"
