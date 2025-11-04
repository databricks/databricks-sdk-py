import pytest  # type: ignore[import-not-found]

from databricks.sdk.common.types.fieldmask import FieldMask


@pytest.mark.parametrize(
    "input_paths,expected_result,description",
    [
        (["field1", "field2", "field3"], "field1,field2,field3", "basic list of paths"),
        (["single_field"], "single_field", "single path"),
        ([], "", "empty paths list"),
        (["user.name", "user.email", "address.street"], "user.name,user.email,address.street", "nested field paths"),
    ],
)
def test_to_json_string(input_paths, expected_result, description):  # type: ignore[no-untyped-def]
    """Test ToJsonString with various path configurations."""
    field_mask = FieldMask()  # type: ignore[no-untyped-call]
    field_mask.paths = input_paths

    result = field_mask.ToJsonString()

    assert result == expected_result


@pytest.mark.parametrize(
    "input_string,expected_paths,description",
    [
        ("field1,field2,field3", ["field1", "field2", "field3"], "basic comma-separated string"),
        ("single_field", ["single_field"], "single field"),
        ("", [], "empty string"),
        ("user.name,user.email,address.street", ["user.name", "user.email", "address.street"], "nested field paths"),
        ("field1, field2 , field3", ["field1", " field2 ", " field3"], "spaces around commas"),
    ],
)
def test_from_json_string_success_cases(input_string, expected_paths, description):  # type: ignore[no-untyped-def]
    """Test FromJsonString with various valid input strings."""
    field_mask = FieldMask()  # type: ignore[no-untyped-call]

    field_mask.FromJsonString(input_string)

    assert field_mask.paths == expected_paths


@pytest.mark.parametrize(
    "invalid_input,expected_error_substring,description",
    [
        (123, "FieldMask JSON value not a string: 123", "non-string integer input"),
        (None, "FieldMask JSON value not a string: None", "None input"),
        (["field1", "field2"], "FieldMask JSON value not a string:", "list input"),
        ({"field": "value"}, "FieldMask JSON value not a string:", "dict input"),
    ],
)
def test_from_json_string_error_cases(invalid_input, expected_error_substring, description):  # type: ignore[no-untyped-def]
    """Test FromJsonString raises ValueError for invalid input types."""
    field_mask = FieldMask()  # type: ignore[no-untyped-call]

    with pytest.raises(ValueError) as exc_info:
        field_mask.FromJsonString(invalid_input)

    assert expected_error_substring in str(exc_info.value)


@pytest.mark.parametrize(
    "original_paths,description",
    [
        (["user.name", "user.email", "profile.settings"], "multiple nested fields"),
        (["single_field"], "single field"),
        ([], "empty paths"),
    ],
)
def test_roundtrip_conversion(original_paths, description):  # type: ignore[no-untyped-def]
    """Test that ToJsonString and FromJsonString are inverse operations."""
    field_mask = FieldMask()  # type: ignore[no-untyped-call]
    field_mask.paths = original_paths

    # Convert to string and back.
    json_string = field_mask.ToJsonString()
    field_mask.FromJsonString(json_string)

    assert field_mask.paths == original_paths
