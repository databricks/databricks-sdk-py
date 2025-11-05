from dataclasses import dataclass
from enum import Enum

import pytest  # type: ignore[import-not-found]
from google.protobuf.duration_pb2 import Duration  # type: ignore[import-untyped]
from google.protobuf.timestamp_pb2 import Timestamp  # type: ignore[import-untyped]

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


@pytest.mark.parametrize(
    "input_dict,field_name,expected_timestamp,description",
    [
        (
            {"field": "2023-01-01T12:00:00Z"},
            "field",
            Timestamp(seconds=1672574400),
            "valid timestamp",
        ),
        ({}, "field", None, "missing field"),
        ({"field": None}, "field", None, "None value"),
        ({"field": ""}, "field", None, "empty value"),
    ],
)
def test_timestamp(input_dict, field_name, expected_timestamp, description):
    """Test _timestamp function with various input scenarios."""
    result = _timestamp(input_dict, field_name)

    if expected_timestamp is None:
        assert result is None
    else:
        assert isinstance(result, Timestamp)
        assert result == expected_timestamp


@pytest.mark.parametrize(
    "input_dict,field_name,expected_timestamp_list,description",
    [
        (
            {"field": ["2023-01-01T12:00:00Z", "2023-01-02T12:00:00Z"]},
            "field",
            [Timestamp(seconds=1672574400), Timestamp(seconds=1672660800)],
            "valid repeated timestamps",
        ),
        ({}, "field", [], "missing field"),
        ({"field": None}, "field", [], "None value"),
        ({"field": []}, "field", [], "empty list"),
    ],
)
def test_repeated_timestamp(input_dict, field_name, expected_timestamp_list, description):
    """Test _repeated_timestamp function with various input scenarios."""
    result = _repeated_timestamp(input_dict, field_name)

    if expected_timestamp_list is None or len(expected_timestamp_list) == 0:
        assert result is None
    else:
        assert len(result) == len(expected_timestamp_list)
        assert all(isinstance(ts, Timestamp) for ts in result)
        for i, expected_timestamp in enumerate(expected_timestamp_list):
            assert result[i] == expected_timestamp


@pytest.mark.parametrize(
    "input_dict,field_name,expected_duration,description",
    [
        ({"field": "3600s"}, "field", Duration(seconds=3600), "valid duration"),
        ({}, "field", None, "missing field"),
        ({"field": None}, "field", None, "None value"),
        ({"field": ""}, "field", None, "empty value"),
    ],
)
def test_duration(input_dict, field_name, expected_duration, description):
    """Test _duration function with various input scenarios."""
    result = _duration(input_dict, field_name)

    if expected_duration is None:
        assert result is None
    else:
        assert isinstance(result, Duration)
        assert result == expected_duration


@pytest.mark.parametrize(
    "input_dict,field_name,expected_duration_list,description",
    [
        (
            {"field": ["3600s", "7200s"]},
            "field",
            [Duration(seconds=3600), Duration(seconds=7200)],
            "valid repeated durations",
        ),
        ({}, "field", [], "missing field"),
        ({"field": None}, "field", None, "None value"),
        ({"field": []}, "field", [], "empty list"),
    ],
)
def test_repeated_duration(input_dict, field_name, expected_duration_list, description):
    """Test _repeated_duration function with various input scenarios."""
    result = _repeated_duration(input_dict, field_name)

    if expected_duration_list is None or len(expected_duration_list) == 0:
        assert result is None
    else:
        assert len(result) == len(expected_duration_list)
        assert all(isinstance(dur, Duration) for dur in result)
        for i, expected_duration in enumerate(expected_duration_list):
            assert result[i] == expected_duration


@pytest.mark.parametrize(
    "input_dict,field_name,expected_fieldmask,description",
    [
        (
            {"field": "path1,path2"},
            "field",
            FieldMask(field_mask=["path1", "path2"]),
            "valid fieldmask",
        ),
        ({}, "field", None, "missing field"),
        ({"field": None}, "field", None, "None value"),
        ({"field": ""}, "field", None, "empty value"),
    ],
)
def test_fieldmask(input_dict, field_name, expected_fieldmask, description):
    """Test _fieldmask function with various input scenarios."""
    result = _fieldmask(input_dict, field_name)

    if expected_fieldmask is None:
        assert result is None
    else:
        assert isinstance(result, FieldMask)
        assert result == expected_fieldmask


@pytest.mark.parametrize(
    "input_dict,field_name,expected_fieldmask_list,description",
    [
        (
            {"field": ["path1,path2", "path3,path4"]},
            "field",
            [FieldMask(field_mask=["path1", "path2"]), FieldMask(field_mask=["path3", "path4"])],
            "valid repeated fieldmasks",
        ),
        ({}, "field", [], "missing field"),
        ({"field": None}, "field", None, "None value"),
        ({"field": []}, "field", [], "empty list"),
    ],
)
def test_repeated_fieldmask(input_dict, field_name, expected_fieldmask_list, description):
    """Test _repeated_fieldmask function with various input scenarios."""
    result = _repeated_fieldmask(input_dict, field_name)

    if expected_fieldmask_list is None or len(expected_fieldmask_list) == 0:
        assert result is None
    else:
        assert len(result) == len(expected_fieldmask_list)
        assert all(isinstance(fm, FieldMask) for fm in result)
        for i, expected_fieldmask in enumerate(expected_fieldmask_list):
            assert result[i] == expected_fieldmask
