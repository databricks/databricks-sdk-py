import hashlib
import pathlib
import subprocess
import sys
import textwrap
from typing import List

import pytest

# databricks/__init__.py lives one directory above this test, regardless
# of where pytest was invoked from.
_INIT_FILE = pathlib.Path(__file__).parent.parent / "databricks" / "__init__.py"


def test_init_file_contents():
    """
    Micro test to confirm the contents of `databricks/__init__.py` does not change.

    Also see https://github.com/databricks/databricks-sdk-py/issues/343#issuecomment-1866029118.
    """
    with open(_INIT_FILE) as f:
        init_file_contents = f.read()

    # This hash is the expected hash of the contents of `src/databricks/__init__.py`.
    # It must not change, or else parallel package installation may lead to clobbered and invalid files.
    expected_sha1 = "2772edbf52e517542acf8c039479c4b57b6ca2cd"
    actual_sha1 = hashlib.sha1(init_file_contents.encode("utf-8")).hexdigest()
    assert expected_sha1 == actual_sha1


def _run_python(code: str, sys_path: List[str]):
    """Runs `code` in a fresh interpreter, so imports start from an empty `sys.modules`."""
    prelude = f"import sys\nsys.path[:] = {sys_path!r}\n"
    result = subprocess.run(
        [sys.executable, "-c", prelude + textwrap.dedent(code)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"


def _install_other_library_packages(root: pathlib.Path):
    """Lays out packages the way another library's wheel installs them under `databricks.sdk`:
    only `databricks/sdk/<api>/v1/`, with no `databricks/__init__.py`, `databricks/sdk/__init__.py` or
    `databricks/sdk/<api>/__init__.py`."""
    for api in ("fakeapi", "oauth", "environments"):
        package = root / "databricks" / "sdk" / api / "v1"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text(f"API = {api!r}\n")


@pytest.mark.parametrize("other_library_first", [True, False], ids=["other-library-first", "other-library-last"])
def test_packages_import_from_another_sys_path_entry(tmp_path, other_library_first):
    _install_other_library_packages(tmp_path)
    sys_path = [str(tmp_path), *sys.path] if other_library_first else [*sys.path, str(tmp_path)]
    _run_python(
        """
        import databricks.sdk.fakeapi.v1
        from databricks.sdk import WorkspaceClient

        assert databricks.sdk.fakeapi.v1.API == "fakeapi"

        import databricks.sdk.environments.v1
        import databricks.sdk.oauth.v1
        from databricks.sdk.environments import Cloud
        from databricks.sdk.oauth import Consent

        assert databricks.sdk.oauth.v1.API == "oauth"
        assert databricks.sdk.environments.v1.API == "environments"
        """,
        sys_path,
    )


def test_sdk_modules_win_over_another_sdk_installation(tmp_path):
    other_sdk = tmp_path / "databricks" / "sdk"
    (other_sdk / "common" / "types").mkdir(parents=True)
    (other_sdk / "__init__.py").write_text("")
    (other_sdk / "version.py").write_text("__version__ = '0.0.0'\n")
    (other_sdk / "common" / "__init__.py").write_text("FROM_OTHER_SDK = True\n")
    (other_sdk / "common" / "types" / "__init__.py").write_text("")
    _run_python(
        """
        import databricks.sdk.common
        from databricks.sdk import version
        from databricks.sdk.common.types.fieldmask import FieldMask

        assert version.__version__ != "0.0.0"
        assert not hasattr(databricks.sdk.common, "FROM_OTHER_SDK")
        """,
        [*sys.path, str(tmp_path)],
    )
