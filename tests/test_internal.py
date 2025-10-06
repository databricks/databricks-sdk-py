from dataclasses import dataclass
from enum import Enum

import pytest
from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp

from databricks.sdk.common.types.fieldmask import FieldMask
from databricks.sdk.service._internal import (
    _duration, _enum, _escape_multi_segment_path_parameter, _fieldmask,
    _from_dict, _repeated_dict, _repeated_duration, _repeated_enum,
    _repeated_fieldmask, _repeated_timestamp, _timestamp)


class A(Enum):
    a = "a"
    b = "b"


def test_enum():
    assert _enum({"field": "a"}, "field", A) == A.a


def test_enum_unknown():
    assert _enum({"field": "c"}, "field", A) is None


def test_repeated_enum():
    assert _repeated_enum({"field": ["a", "b"]}, "field", A) == [A.a, A.b]


def test_repeated_enum_unknown():
    assert _repeated_enum({"field": ["a", "c"]}, "field", A) == [A.a]


@dataclass
class B:
    field: str

    @classmethod
    def from_dict(cls, d: dict) -> "B":
        return cls(d["field"])


def test_from_dict():
    assert _from_dict({"x": {"field": "a"}}, "x", B) == B("a")


def test_repeated_dict():
    assert _repeated_dict({"x": [{"field": "a"}, {"field": "c"}]}, "x", B) == [
        B("a"),
        B("c"),
    ]


def test_escape_multi_segment_path_parameter():
    assert _escape_multi_segment_path_parameter("a b") == "a%20b"
    assert _escape_multi_segment_path_parameter("a/b") == "a/b"
    assert _escape_multi_segment_path_parameter("a?b") == "a%3Fb"
    assert _escape_multi_segment_path_parameter("a#b") == "a%23b"


@pytest.mark.parametrize("input_dict,field_name,expected_result,expected_json,description", [
    ({"field": "2023-01-01T12:00:00Z"}, "field", "timestamp_object", "2023-01-01T12:00:00Z", "valid timestamp"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": ""}, "field", None, None, "empty value"),
])
def test_timestamp(input_dict, field_name, expected_result, expected_json, description):
    """Test _timestamp function with various input scenarios."""
    result = _timestamp(input_dict, field_name)
    
    if expected_result is None:
        assert result is None
    else:
        assert isinstance(result, Timestamp)
        assert result.ToJsonString() == expected_json


@pytest.mark.parametrize("input_dict,field_name,expected_length,expected_json_list,description", [
    ({"field": ["2023-01-01T12:00:00Z", "2023-01-02T12:00:00Z"]}, "field", 2, ["2023-01-01T12:00:00Z", "2023-01-02T12:00:00Z"], "valid repeated timestamps"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": []}, "field", None, None, "empty list"),
])
def test_repeated_timestamp(input_dict, field_name, expected_length, expected_json_list, description):
    """Test _repeated_timestamp function with various input scenarios."""
    result = _repeated_timestamp(input_dict, field_name)
    
    if expected_length is None:
        assert result is None
    else:
        assert len(result) == expected_length
        assert all(isinstance(ts, Timestamp) for ts in result)
        for i, expected_json in enumerate(expected_json_list):
            assert result[i].ToJsonString() == expected_json


@pytest.mark.parametrize("input_dict,field_name,expected_result,expected_json,description", [
    ({"field": "3600s"}, "field", "duration_object", "3600s", "valid duration"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": ""}, "field", None, None, "empty value"),
])
def test_duration(input_dict, field_name, expected_result, expected_json, description):
    """Test _duration function with various input scenarios."""
    result = _duration(input_dict, field_name)
    
    if expected_result is None:
        assert result is None
    else:
        assert isinstance(result, Duration)
        assert result.ToJsonString() == expected_json


@pytest.mark.parametrize("input_dict,field_name,expected_length,expected_json_list,description", [
    ({"field": ["3600s", "7200s"]}, "field", 2, ["3600s", "7200s"], "valid repeated durations"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": []}, "field", None, None, "empty list"),
])
def test_repeated_duration(input_dict, field_name, expected_length, expected_json_list, description):
    """Test _repeated_duration function with various input scenarios."""
    result = _repeated_duration(input_dict, field_name)
    
    if expected_length is None:
        assert result is None
    else:
        assert len(result) == expected_length
        assert all(isinstance(dur, Duration) for dur in result)
        for i, expected_json in enumerate(expected_json_list):
            assert result[i].ToJsonString() == expected_json


@pytest.mark.parametrize("input_dict,field_name,expected_result,expected_json,description", [
    ({"field": "path1,path2"}, "field", "fieldmask_object", "path1,path2", "valid fieldmask"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": ""}, "field", None, None, "empty value"),
])
def test_fieldmask(input_dict, field_name, expected_result, expected_json, description):
    """Test _fieldmask function with various input scenarios."""
    result = _fieldmask(input_dict, field_name)
    
    if expected_result is None:
        assert result is None
    else:
        assert isinstance(result, FieldMask)
        assert result.ToJsonString() == expected_json


@pytest.mark.parametrize("input_dict,field_name,expected_length,expected_json_list,description", [
    ({"field": ["path1,path2", "path3,path4"]}, "field", 2, ["path1,path2", "path3,path4"], "valid repeated fieldmasks"),
    ({}, "field", None, None, "missing field"),
    ({"field": None}, "field", None, None, "None value"),
    ({"field": []}, "field", None, None, "empty list"),
])
def test_repeated_fieldmask(input_dict, field_name, expected_length, expected_json_list, description):
    """Test _repeated_fieldmask function with various input scenarios."""
    result = _repeated_fieldmask(input_dict, field_name)
    
    if expected_length is None:
        assert result is None
    else:
        assert len(result) == expected_length
        assert all(isinstance(fm, FieldMask) for fm in result)
        for i, expected_json in enumerate(expected_json_list):
            assert result[i].ToJsonString() == expected_json
