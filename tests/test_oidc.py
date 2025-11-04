from dataclasses import dataclass
from typing import Optional, Tuple

import pytest  # type: ignore[import-not-found]

from databricks.sdk import oidc


@dataclass
class EnvTestCase:
    name: str
    env_name: str = ""
    env_value: str = ""
    want: oidc.IdToken = None  # type: ignore[assignment]
    wantException: Exception = None  # type: ignore[assignment]


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
        wantException=ValueError,  # type: ignore[arg-type]
    ),
    EnvTestCase(
        name="empty_env_var",
        env_name="OIDC_TEST_TOKEN_EMPTY",
        env_value="",
        wantException=ValueError,  # type: ignore[arg-type]
    ),
    EnvTestCase(
        name="different_variable_name",
        env_name="ANOTHER_OIDC_TOKEN",
        env_value="another-token-456",
        want=oidc.IdToken(jwt="another-token-456"),
    ),
]


@pytest.mark.parametrize("test_case", _env_id_test_cases)  # type: ignore[misc]
def test_env_id_token_source(test_case: EnvTestCase, monkeypatch):  # type: ignore[no-untyped-def]
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
    want: oidc.IdToken = None  # type: ignore[assignment]
    wantException: Exception = None  # type: ignore[assignment]


_file_id_test_cases = [
    FileTestCase(
        name="missing_filepath",
        file=("token", "content"),
        filepath="",
        wantException=ValueError,  # type: ignore[arg-type]
    ),
    FileTestCase(
        name="empty_file",
        file=("token", ""),
        filepath="token",
        wantException=ValueError,  # type: ignore[arg-type]
    ),
    FileTestCase(
        name="file_does_not_exist",
        filepath="nonexistent-file",
        wantException=ValueError,  # type: ignore[arg-type]
    ),
    FileTestCase(
        name="file_exists",
        file=("token", "content"),
        filepath="token",
        want=oidc.IdToken(jwt="content"),
    ),
]


@pytest.mark.parametrize("test_case", _file_id_test_cases)  # type: ignore[misc]
def test_file_id_token_source(test_case: FileTestCase, tmp_path):  # type: ignore[no-untyped-def]
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
