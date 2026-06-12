from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple

import pytest

from databricks.sdk import oauth, oidc


@dataclass
class EnvTestCase:
    name: str
    env_name: str = ""
    env_value: str = ""
    want: oidc.IdToken = None
    wantException: Exception = None


_env_id_test_cases = [
    EnvTestCase(
        name="success",
        env_name="OIDC_TEST_TOKEN_SUCCESS",
        env_value="test-token-123",
        want=oidc.IdToken(jwt="test-token-123"),
    ),
    EnvTestCase(
        name="missing_env_var",
        env_name="OIDC_TEST_TOKEN_MISSING",
        env_value="",
        wantException=ValueError,
    ),
    EnvTestCase(
        name="empty_env_var",
        env_name="OIDC_TEST_TOKEN_EMPTY",
        env_value="",
        wantException=ValueError,
    ),
    EnvTestCase(
        name="different_variable_name",
        env_name="ANOTHER_OIDC_TOKEN",
        env_value="another-token-456",
        want=oidc.IdToken(jwt="another-token-456"),
    ),
]


@pytest.mark.parametrize("test_case", _env_id_test_cases)
def test_env_id_token_source(test_case: EnvTestCase, monkeypatch):
    monkeypatch.setenv(test_case.env_name, test_case.env_value)

    source = oidc.EnvIdTokenSource(test_case.env_name)
    if test_case.wantException:
        with pytest.raises(test_case.wantException):
            source.id_token()
    else:
        assert source.id_token() == test_case.want


@dataclass
class FileTestCase:
    name: str
    file: Optional[Tuple[str, str]] = None  # (name, content)
    filepath: str = ""
    want: oidc.IdToken = None
    wantException: Exception = None


_file_id_test_cases = [
    FileTestCase(
        name="missing_filepath",
        file=("token", "content"),
        filepath="",
        wantException=ValueError,
    ),
    FileTestCase(
        name="empty_file",
        file=("token", ""),
        filepath="token",
        wantException=ValueError,
    ),
    FileTestCase(
        name="file_does_not_exist",
        filepath="nonexistent-file",
        wantException=ValueError,
    ),
    FileTestCase(
        name="file_exists",
        file=("token", "content"),
        filepath="token",
        want=oidc.IdToken(jwt="content"),
    ),
]


@pytest.mark.parametrize("test_case", _file_id_test_cases)
def test_file_id_token_source(test_case: FileTestCase, tmp_path):
    if test_case.file:
        token_file = tmp_path / test_case.file[0]
        token_file.write_text(test_case.file[1])

    fp = ""
    if test_case.filepath:
        fp = tmp_path / test_case.filepath

    source = oidc.FileIdTokenSource(fp)
    if test_case.wantException:
        with pytest.raises(test_case.wantException):
            source.id_token()
    else:
        assert source.id_token() == test_case.want


class _CountingIdTokenSource(oidc.IdTokenSource):
    """An IdTokenSource that counts how many times it is invoked and returns a
    fresh jwt each time, so we can assert ID-token rotation on refresh."""

    def __init__(self):
        self.calls = 0

    def id_token(self) -> oidc.IdToken:
        self.calls += 1
        return oidc.IdToken(jwt=f"id-token-{self.calls}")


def _make_token_source(id_token_source, exchanges, expiry):
    """Build a DatabricksOidcTokenSource whose exchange step is stubbed to record
    the ID token it received and return a token with the given expiry."""
    ts = oidc.DatabricksOidcTokenSource(
        host="https://test.cloud.databricks.com",
        token_endpoint="https://test.cloud.databricks.com/oidc/v1/token",
        id_token_source=id_token_source,
        client_id="test-client-id",
    )

    def _exchange(id_token: oidc.IdToken) -> oauth.Token:
        exchanges.append(id_token.jwt)
        return oauth.Token(access_token=f"exchanged-{id_token.jwt}", token_type="Bearer", expiry=expiry)

    ts._exchange_id_token = _exchange
    return ts


def test_databricks_oidc_token_source_caches_token():
    # A valid token (1h TTL) should be minted once and reused across calls,
    # rather than exchanging the ID token on every token() call.
    id_token_source = _CountingIdTokenSource()
    exchanges = []
    ts = _make_token_source(
        id_token_source,
        exchanges,
        expiry=datetime.now(tz=timezone.utc) + timedelta(hours=1),
    )

    first = ts.token()
    for _ in range(5):
        again = ts.token()
        assert again.access_token == first.access_token

    assert exchanges == ["id-token-1"]
    assert id_token_source.calls == 1


def test_databricks_oidc_token_source_refreshes_when_expired():
    # An already-expired token must trigger a re-exchange, and the refresh must
    # fetch a *fresh* ID token (rotation), not reuse the original jwt.
    id_token_source = _CountingIdTokenSource()
    exchanges = []
    ts = _make_token_source(
        id_token_source,
        exchanges,
        expiry=datetime.now(tz=timezone.utc) - timedelta(seconds=1),
    )

    ts.token()
    ts.token()

    assert exchanges == ["id-token-1", "id-token-2"]
    assert id_token_source.calls == 2


def test_databricks_oidc_token_source_missing_host_raises():
    ts = oidc.DatabricksOidcTokenSource(
        host="",
        token_endpoint="https://test.cloud.databricks.com/oidc/v1/token",
        id_token_source=_CountingIdTokenSource(),
        client_id="test-client-id",
    )
    with pytest.raises(ValueError, match="missing Host"):
        ts.token()
