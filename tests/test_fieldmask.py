import pytest

from databricks.sdk.common.types.fieldmask import FieldMask


def test_to_json_string_basic():
    """Test ToJsonString with basic list of paths."""
    field_mask = FieldMask()
    field_mask.paths = ["field1", "field2", "field3"]

    result = field_mask.ToJsonString()

    assert result == "field1,field2,field3"


def test_to_json_string_single_path():
    """Test ToJsonString with single path."""
    field_mask = FieldMask()
    field_mask.paths = ["single_field"]

    result = field_mask.ToJsonString()

    assert result == "single_field"


def test_to_json_string_empty_paths():
    """Test ToJsonString with empty paths list."""
    field_mask = FieldMask()
    field_mask.paths = []

    result = field_mask.ToJsonString()

    assert result == ""


def test_to_json_string_nested_paths():
    """Test ToJsonString with nested field paths."""
    field_mask = FieldMask()
    field_mask.paths = ["user.name", "user.email", "address.street"]

    result = field_mask.ToJsonString()

    assert result == "user.name,user.email,address.street"


def test_from_json_string_basic():
    """Test FromJsonString with basic comma-separated string."""
    field_mask = FieldMask()

    field_mask.FromJsonString("field1,field2,field3")

    assert field_mask.paths == ["field1", "field2", "field3"]


def test_from_json_string_single_field():
    """Test FromJsonString with single field."""
    field_mask = FieldMask()

    field_mask.FromJsonString("single_field")

    assert field_mask.paths == ["single_field"]


def test_from_json_string_empty_string():
    """Test FromJsonString with empty string."""
    field_mask = FieldMask()

    field_mask.FromJsonString("")

    assert field_mask.paths == []


def test_from_json_string_nested_paths():
    """Test FromJsonString with nested field paths."""
    field_mask = FieldMask()

    field_mask.FromJsonString("user.name,user.email,address.street")

    assert field_mask.paths == ["user.name", "user.email", "address.street"]


def test_from_json_string_with_spaces():
    """Test FromJsonString with spaces around commas."""
    field_mask = FieldMask()

    field_mask.FromJsonString("field1, field2 , field3")

    assert field_mask.paths == ["field1", " field2 ", " field3"]


def test_from_json_string_non_string_input():
    """Test FromJsonString raises ValueError for non-string input."""
    field_mask = FieldMask()

    with pytest.raises(ValueError) as exc_info:
        field_mask.FromJsonString(123)

    assert "FieldMask JSON value not a string: 123" in str(exc_info.value)


def test_from_json_string_none_input():
    """Test FromJsonString raises ValueError for None input."""
    field_mask = FieldMask()

    with pytest.raises(ValueError) as exc_info:
        field_mask.FromJsonString(None)

    assert "FieldMask JSON value not a string: None" in str(exc_info.value)


def test_from_json_string_list_input():
    """Test FromJsonString raises ValueError for list input."""
    field_mask = FieldMask()

    with pytest.raises(ValueError) as exc_info:
        field_mask.FromJsonString(["field1", "field2"])

    assert "FieldMask JSON value not a string:" in str(exc_info.value)


def test_from_json_string_dict_input():
    """Test FromJsonString raises ValueError for dict input."""
    field_mask = FieldMask()

    with pytest.raises(ValueError) as exc_info:
        field_mask.FromJsonString({"field": "value"})

    assert "FieldMask JSON value not a string:" in str(exc_info.value)


def test_roundtrip_conversion():
    """Test that ToJsonString and FromJsonString are inverse operations."""
    field_mask = FieldMask()
    original_paths = ["user.name", "user.email", "profile.settings"]
    field_mask.paths = original_paths

    # Convert to string and back.
    json_string = field_mask.ToJsonString()
    field_mask.FromJsonString(json_string)

    assert field_mask.paths == original_paths


def test_roundtrip_conversion_single_field():
    """Test roundtrip conversion with single field."""
    field_mask = FieldMask()
    original_paths = ["single_field"]
    field_mask.paths = original_paths

    # Convert to string and back.
    json_string = field_mask.ToJsonString()
    field_mask.FromJsonString(json_string)

    assert field_mask.paths == original_paths


def test_roundtrip_conversion_empty():
    """Test roundtrip conversion with empty paths."""
    field_mask = FieldMask()
    original_paths = []
    field_mask.paths = original_paths

    # Convert to string and back.
    json_string = field_mask.ToJsonString()
    field_mask.FromJsonString(json_string)

    assert field_mask.paths == original_paths
