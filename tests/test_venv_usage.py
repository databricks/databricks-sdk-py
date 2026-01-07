"""Test to verify that tests are running from within the project's virtual environment.

This test exists to catch Makefile issues where the venv is created but not actually used.
If this test fails in CI, it means `make test` is using system Python instead of .venv/bin/python.
"""

import sys


def test_running_in_venv():
    """Verify pytest is running from the project's .venv, not system Python."""
    # Log the Python paths being used for visibility in CI output
    print(f"\n=== Python Environment Info ===")
    print(f"sys.executable: {sys.executable}")
    print(f"sys.prefix:     {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")
    print(f"================================\n")

    # sys.prefix points to the Python installation being used
    # If we're in the venv, it should contain '.venv'
    assert ".venv" in sys.prefix, (
        f"Tests are NOT running from the project venv!\n"
        f"sys.prefix = {sys.prefix}\n"
        f"sys.executable = {sys.executable}\n"
        f"This likely means the Makefile is not correctly using the venv it creates."
    )
