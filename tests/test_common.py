"""Tests for common types in the Databricks SDK."""

from datetime import datetime, timedelta, timezone

import pytest

from databricks.sdk.common import Duration, Timestamp


def test_duration_initialization():
    """Test Duration initialization and validation."""
    # Test valid initialization
    d = Duration(seconds=1, nanoseconds=500000000)
    assert d.seconds == 1
    assert d.nanoseconds == 500000000

    # Test default values
    d = Duration()
    assert d.seconds == 0
    assert d.nanoseconds == 0

    # Test validation
    with pytest.raises(TypeError):
        Duration(seconds="1")  # type: ignore
    with pytest.raises(TypeError):
        Duration(nanoseconds="500000000")  # type: ignore
    with pytest.raises(ValueError):
        Duration(nanoseconds=-1)
    with pytest.raises(ValueError):
        Duration(nanoseconds=1_000_000_000)


def test_duration_from_timedelta():
    """Test conversion from timedelta to Duration."""
    # Test with whole seconds
    td = timedelta(seconds=10)
    d = Duration.from_timedelta(td)
    assert d.seconds == 10
    assert d.nanoseconds == 0

    # Test with microseconds
    td = timedelta(microseconds=500000)
    d = Duration.from_timedelta(td)
    assert d.seconds == 0
    assert d.nanoseconds == 500000000

    # Test with both
    td = timedelta(seconds=1, microseconds=500000)
    d = Duration.from_timedelta(td)
    assert d.seconds == 1
    assert d.nanoseconds == 500000000


def test_duration_to_timedelta():
    """Test conversion from Duration to timedelta."""
    # Test with whole seconds
    d = Duration(seconds=10)
    td = d.to_timedelta()
    assert td.total_seconds() == 10.0

    # Test with nanoseconds
    d = Duration(nanoseconds=500000000)
    td = d.to_timedelta()
    assert td.total_seconds() == 0.5

    # Test with both
    d = Duration(seconds=1, nanoseconds=500000000)
    td = d.to_timedelta()
    assert td.total_seconds() == 1.5


def test_duration_parse():
    """Test parsing duration strings."""
    # Test whole seconds
    d = Duration.parse("10s")
    assert d.seconds == 10
    assert d.nanoseconds == 0

    # Test decimal seconds
    d = Duration.parse("1.5s")
    assert d.seconds == 1
    assert d.nanoseconds == 500000000

    # Test invalid formats
    with pytest.raises(ValueError):
        Duration.parse("10")  # missing 's'
    with pytest.raises(ValueError):
        Duration.parse("invalid")


def test_duration_to_string():
    """Test string representation of Duration."""
    # Test whole seconds
    d = Duration(seconds=10)
    assert d.to_string() == "10s"

    # Test decimal seconds
    d = Duration(seconds=1, nanoseconds=500000000)
    assert d.to_string() == "1.5s"

    # Test nanoseconds only
    d = Duration(nanoseconds=500000000)
    assert d.to_string() == "0.5s"


def test_timestamp_initialization():
    """Test Timestamp initialization and validation."""
    # Test valid initialization
    ts = Timestamp(seconds=1609459200, nanos=500000000)  # 2021-01-01T00:00:00.5Z
    assert ts.seconds == 1609459200
    assert ts.nanos == 500000000

    # Test default values
    ts = Timestamp()
    assert ts.seconds == 0
    assert ts.nanos == 0

    # Test validation
    with pytest.raises(TypeError):
        Timestamp(seconds="1609459200")  # type: ignore
    with pytest.raises(TypeError):
        Timestamp(nanos="500000000")  # type: ignore
    with pytest.raises(ValueError):
        Timestamp(nanos=-1)
    with pytest.raises(ValueError):
        Timestamp(nanos=1_000_000_000)


def test_timestamp_from_datetime():
    """Test conversion from datetime to Timestamp."""
    # Test UTC datetime
    dt = datetime(2021, 1, 1, 12, 0, 0, 500000, tzinfo=timezone.utc)
    ts = Timestamp.from_datetime(dt)
    assert ts.seconds == 1609502400  # 2021-01-01T12:00:00Z
    assert ts.nanos == 500000000

    # Test naive datetime (should be treated as UTC)
    dt = datetime(2021, 1, 1, 12, 0, 0, 500000)
    ts = Timestamp.from_datetime(dt)
    assert ts.seconds == 1609502400
    assert ts.nanos == 500000000

    # Test with different timezone
    dt = datetime(2021, 1, 1, 13, 0, 0, 500000, tzinfo=timezone(timedelta(hours=1)))
    ts = Timestamp.from_datetime(dt)
    assert ts.seconds == 1609502400  # Should be converted to UTC
    assert ts.nanos == 500000000


def test_timestamp_to_datetime():
    """Test conversion from Timestamp to datetime."""
    # Test with whole seconds
    ts = Timestamp(seconds=1609459200)  # 2021-01-01T00:00:00Z
    dt = ts.to_datetime()
    assert dt.year == 2021
    assert dt.month == 1
    assert dt.day == 1
    assert dt.hour == 0
    assert dt.minute == 0
    assert dt.second == 0
    assert dt.microsecond == 0
    assert dt.tzinfo == timezone.utc

    # Test with nanoseconds
    ts = Timestamp(seconds=1609459200, nanos=500000000)
    dt = ts.to_datetime()
    assert dt.microsecond == 500000


def test_timestamp_parse():
    """Test parsing RFC3339 timestamp strings."""
    # Test basic format
    ts = Timestamp.parse("2021-01-01T12:00:00Z")
    assert ts.seconds == 1609502400
    assert ts.nanos == 0

    # Test with nanoseconds
    ts = Timestamp.parse("2021-01-01T12:00:00.5Z")
    assert ts.seconds == 1609502400
    assert ts.nanos == 500000000

    # Test with timezone offset
    ts = Timestamp.parse("2021-01-01T13:00:00+01:00")
    assert ts.seconds == 1609502400  # Should be converted to UTC
    assert ts.nanos == 0

    # Test invalid formats
    with pytest.raises(ValueError):
        Timestamp.parse("2021-01-01")  # missing time
    with pytest.raises(ValueError):
        Timestamp.parse("invalid")


def test_timestamp_to_string():
    """Test string representation of Timestamp."""
    # Test with whole seconds
    ts = Timestamp(seconds=1609459200)  # 2021-01-01T00:00:00Z
    assert ts.to_string() == "2021-01-01T00:00:00Z"

    # Test with nanoseconds
    ts = Timestamp(seconds=1609459200, nanos=500000000)
    assert ts.to_string() == "2021-01-01T00:00:00.5Z"


def test_timestamp_equality():
    """Test Timestamp equality comparison."""
    ts1 = Timestamp(seconds=1609459200, nanos=500000000)
    ts2 = Timestamp(seconds=1609459200, nanos=500000000)
    ts3 = Timestamp(seconds=1609459200, nanos=0)

    assert ts1 == ts2
    assert ts1 != ts3
    assert ts1 != "not a timestamp"  # type: ignore
