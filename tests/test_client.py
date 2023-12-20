from unittest.mock import create_autospec

import pytest

from databricks.sdk import WorkspaceClient


def test_autospec_fails_on_unknown_service():
    w = create_autospec(WorkspaceClient)
    with pytest.raises(AttributeError):
        w.foo.bar()


def test_autospec_fails_on_setting_unknown_property():
    w = create_autospec(WorkspaceClient, spec_set=True)
    with pytest.raises(AttributeError):
        w.bar = 1
