from dataclasses import dataclass
from enum import Enum

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


def test_timestamp():
    # Test valid timestamp
    result = _timestamp({"field": "2023-01-01T12:00:00Z"}, "field")
    assert isinstance(result, Timestamp)
    assert result.ToJsonString() == "2023-01-01T12:00:00Z"


def test_timestamp_missing_field():
    # Test missing field
    assert _timestamp({}, "field") is None


def test_timestamp_none_value():
    # Test None value
    assert _timestamp({"field": None}, "field") is None


def test_timestamp_empty_value():
    # Test empty value
    assert _timestamp({"field": ""}, "field") is None


def test_repeated_timestamp():
    # Test valid repeated timestamps
    result = _repeated_timestamp({"field": ["2023-01-01T12:00:00Z", "2023-01-02T12:00:00Z"]}, "field")
    assert len(result) == 2
    assert all(isinstance(ts, Timestamp) for ts in result)
    assert result[0].ToJsonString() == "2023-01-01T12:00:00Z"
    assert result[1].ToJsonString() == "2023-01-02T12:00:00Z"


def test_repeated_timestamp_missing_field():
    # Test missing field
    assert _repeated_timestamp({}, "field") is None


def test_repeated_timestamp_none_value():
    # Test None value
    assert _repeated_timestamp({"field": None}, "field") is None


def test_repeated_timestamp_empty_list():
    # Test empty list
    assert _repeated_timestamp({"field": []}, "field") is None


def test_duration():
    # Test valid duration
    result = _duration({"field": "3600s"}, "field")
    assert isinstance(result, Duration)
    assert result.ToJsonString() == "3600s"


def test_duration_missing_field():
    # Test missing field
    assert _duration({}, "field") is None


def test_duration_none_value():
    # Test None value
    assert _duration({"field": None}, "field") is None


def test_duration_empty_value():
    # Test empty value
    assert _duration({"field": ""}, "field") is None


def test_repeated_duration():
    # Test valid repeated durations
    result = _repeated_duration({"field": ["3600s", "7200s"]}, "field")
    assert len(result) == 2
    assert all(isinstance(dur, Duration) for dur in result)
    assert result[0].ToJsonString() == "3600s"
    assert result[1].ToJsonString() == "7200s"


def test_repeated_duration_missing_field():
    # Test missing field
    assert _repeated_duration({}, "field") is None


def test_repeated_duration_none_value():
    # Test None value
    assert _repeated_duration({"field": None}, "field") is None


def test_repeated_duration_empty_list():
    # Test empty list
    assert _repeated_duration({"field": []}, "field") is None


def test_fieldmask():
    # Test valid fieldmask
    result = _fieldmask({"field": "path1,path2"}, "field")
    assert isinstance(result, FieldMask)
    assert result.ToJsonString() == "path1,path2"


def test_fieldmask_missing_field():
    # Test missing field
    assert _fieldmask({}, "field") is None


def test_fieldmask_none_value():
    # Test None value
    assert _fieldmask({"field": None}, "field") is None


def test_fieldmask_empty_value():
    # Test empty value
    assert _fieldmask({"field": ""}, "field") is None


def test_repeated_fieldmask():
    # Test valid repeated fieldmasks
    result = _repeated_fieldmask({"field": ["path1,path2", "path3,path4"]}, "field")
    assert len(result) == 2
    assert all(isinstance(fm, FieldMask) for fm in result)
    assert result[0].ToJsonString() == "path1,path2"
    assert result[1].ToJsonString() == "path3,path4"


def test_repeated_fieldmask_missing_field():
    # Test missing field
    assert _repeated_fieldmask({}, "field") is None


def test_repeated_fieldmask_none_value():
    # Test None value
    assert _repeated_fieldmask({"field": None}, "field") is None


def test_repeated_fieldmask_empty_list():
    # Test empty list
    assert _repeated_fieldmask({"field": []}, "field") is None
