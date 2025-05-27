"""Tests for common types in the Databricks SDK."""

from datetime import datetime, timedelta, timezone

import pytest

from databricks.sdk.common import Duration, Timestamp


@pytest.mark.parametrize(
    "seconds,nanoseconds,expected_seconds,expected_nanoseconds,raises",
    [
        (1, 500000000, 1, 500000000, None),  # Valid initialization
        (0, 0, 0, 0, None),  # Default values
        ("1", 0, None, None, TypeError),  # Invalid seconds type
        (0, "500000000", None, None, TypeError),  # Invalid nanoseconds type
        (0, -1, None, None, ValueError),  # Negative nanoseconds
        (0, 1_000_000_000, None, None, ValueError),  # Nanoseconds too large
    ],
)
def test_duration_initialization(seconds, nanoseconds, expected_seconds, expected_nanoseconds, raises):
    """Test Duration initialization and validation."""
    if raises:
        with pytest.raises(raises):
            Duration(seconds=seconds, nanoseconds=nanoseconds)
    else:
        d = Duration(seconds=seconds, nanoseconds=nanoseconds)
        assert d.seconds == expected_seconds
        assert d.nanoseconds == expected_nanoseconds


@pytest.mark.parametrize(
    "td,expected_seconds,expected_nanoseconds",
    [
        (timedelta(seconds=10), 10, 0),  # Whole seconds
        (timedelta(microseconds=500000), 0, 500000000),  # Microseconds only
        (timedelta(seconds=1, microseconds=500000), 1, 500000000),  # Both
    ],
)
def test_duration_from_timedelta(td, expected_seconds, expected_nanoseconds):
    """Test conversion from timedelta to Duration."""
    d = Duration.from_timedelta(td)
    assert d.seconds == expected_seconds
    assert d.nanoseconds == expected_nanoseconds


@pytest.mark.parametrize(
    "seconds,nanoseconds,expected_total_seconds",
    [
        (10, 0, 10.0),  # Whole seconds
        (0, 500000000, 0.5),  # Nanoseconds only
        (1, 500000000, 1.5),  # Both
    ],
)
def test_duration_to_timedelta(seconds, nanoseconds, expected_total_seconds):
    """Test conversion from Duration to timedelta."""
    d = Duration(seconds=seconds, nanoseconds=nanoseconds)
    td = d.to_timedelta()
    assert td.total_seconds() == expected_total_seconds


@pytest.mark.parametrize(
    "duration_str,expected_seconds,expected_nanoseconds,raises",
    [
        ("10s", 10, 0, None),  # Whole seconds
        ("1.5s", 1, 500000000, None),  # Decimal seconds
        ("10", None, None, ValueError),  # Missing 's'
        ("invalid", None, None, ValueError),  # Invalid format
    ],
)
def test_duration_parse(duration_str, expected_seconds, expected_nanoseconds, raises):
    """Test parsing duration strings."""
    if raises:
        with pytest.raises(raises):
            Duration.parse(duration_str)
    else:
        d = Duration.parse(duration_str)
        assert d.seconds == expected_seconds
        assert d.nanoseconds == expected_nanoseconds


@pytest.mark.parametrize(
    "seconds,nanoseconds,expected_string",
    [
        (10, 0, "10s"),  # Whole seconds
        (1, 500000000, "1.5s"),  # Decimal seconds
        (0, 500000000, "0.5s"),  # Nanoseconds only
    ],
)
def test_duration_to_string(seconds, nanoseconds, expected_string):
    """Test string representation of Duration."""
    d = Duration(seconds=seconds, nanoseconds=nanoseconds)
    assert d.to_string() == expected_string


@pytest.mark.parametrize(
    "seconds,nanos,expected_seconds,expected_nanos,raises",
    [
        (1609459200, 500000000, 1609459200, 500000000, None),  # Valid initialization
        (0, 0, 0, 0, None),  # Default values
        ("1609459200", 0, None, None, TypeError),  # Invalid seconds type
        (0, "500000000", None, None, TypeError),  # Invalid nanos type
        (0, -1, None, None, ValueError),  # Negative nanos
        (0, 1_000_000_000, None, None, ValueError),  # Nanos too large
    ],
)
def test_timestamp_initialization(seconds, nanos, expected_seconds, expected_nanos, raises):
    """Test Timestamp initialization and validation."""
    if raises:
        with pytest.raises(raises):
            Timestamp(seconds=seconds, nanos=nanos)
    else:
        ts = Timestamp(seconds=seconds, nanos=nanos)
        assert ts.seconds == expected_seconds
        assert ts.nanos == expected_nanos


@pytest.mark.parametrize(
    "dt,expected_seconds,expected_nanos",
    [
        # UTC datetime
        (datetime(2021, 1, 1, 12, 0, 0, 500000, tzinfo=timezone.utc), 1609502400, 500000000),
        # Naive datetime (treated as UTC)
        (datetime(2021, 1, 1, 12, 0, 0, 500000), 1609502400, 500000000),
        # Different timezone (converted to UTC)
        (datetime(2021, 1, 1, 13, 0, 0, 500000, tzinfo=timezone(timedelta(hours=1))), 1609502400, 500000000),
    ],
)
def test_timestamp_from_datetime(dt, expected_seconds, expected_nanos):
    """Test conversion from datetime to Timestamp."""
    ts = Timestamp.from_datetime(dt)
    assert ts.seconds == expected_seconds
    assert ts.nanos == expected_nanos


@pytest.mark.parametrize(
    "seconds,nanos,expected_year,expected_month,expected_day,expected_hour,expected_minute,expected_second,expected_microsecond",
    [
        (1609459200, 0, 2021, 1, 1, 0, 0, 0, 0),  # Whole seconds
        (1609459200, 500000000, 2021, 1, 1, 0, 0, 0, 500000),  # With nanoseconds
    ],
)
def test_timestamp_to_datetime(
    seconds,
    nanos,
    expected_year,
    expected_month,
    expected_day,
    expected_hour,
    expected_minute,
    expected_second,
    expected_microsecond,
):
    """Test conversion from Timestamp to datetime."""
    ts = Timestamp(seconds=seconds, nanos=nanos)
    dt = ts.to_datetime()
    assert dt.year == expected_year
    assert dt.month == expected_month
    assert dt.day == expected_day
    assert dt.hour == expected_hour
    assert dt.minute == expected_minute
    assert dt.second == expected_second
    assert dt.microsecond == expected_microsecond
    assert dt.tzinfo == timezone.utc


@pytest.mark.parametrize(
    "timestamp_str,expected_seconds,expected_nanos,raises",
    [
        ("2021-01-01T12:00:00Z", 1609502400, 0, None),  # Basic format
        ("2021-01-01T12:00:00.5Z", 1609502400, 500000000, None),  # With nanoseconds
        ("2021-01-01T13:00:00+01:00", 1609502400, 0, None),  # With timezone offset
        ("2021-01-01", None, None, ValueError),  # Missing time
        ("invalid", None, None, ValueError),  # Invalid format
    ],
)
def test_timestamp_parse(timestamp_str, expected_seconds, expected_nanos, raises):
    """Test parsing RFC3339 timestamp strings."""
    if raises:
        with pytest.raises(raises):
            Timestamp.parse(timestamp_str)
    else:
        ts = Timestamp.parse(timestamp_str)
        assert ts.seconds == expected_seconds
        assert ts.nanos == expected_nanos


@pytest.mark.parametrize(
    "seconds,nanos,expected_string",
    [
        (1609459200, 0, "2021-01-01T00:00:00Z"),  # Whole seconds
        (1609459200, 500000000, "2021-01-01T00:00:00.5Z"),  # With nanoseconds
    ],
)
def test_timestamp_to_string(seconds, nanos, expected_string):
    """Test string representation of Timestamp."""
    ts = Timestamp(seconds=seconds, nanos=nanos)
    assert ts.to_string() == expected_string


@pytest.mark.parametrize(
    "ts1,ts2,expected_equal",
    [
        (Timestamp(1609459200, 500000000), Timestamp(1609459200, 500000000), True),  # Equal timestamps
        (Timestamp(1609459200, 500000000), Timestamp(1609459200, 0), False),  # Different nanos
        (Timestamp(1609459200, 500000000), "not a timestamp", False),  # Different type
    ],
)
def test_timestamp_equality(ts1, ts2, expected_equal):
    """Test Timestamp equality comparison."""
    assert (ts1 == ts2) == expected_equal
    assert (ts1 != ts2) != expected_equal


@pytest.mark.parametrize(
    "seconds,nanoseconds,expected_microseconds",
    [
        # Test cases with microsecond precision (timedelta limitation)
        (0, 999999999, 999999),  # Maximum nanoseconds rounds to max microseconds
        (0, 999999998, 999999),  # Rounds to max microseconds
        (0, 1, 0),  # Minimum nanoseconds rounds to 0 microseconds
        (0, 100000000, 100000),  # 0.1 seconds in nanoseconds
        (0, 333333333, 333333),  # 1/3 second in nanoseconds
        (0, 666666666, 666666),  # 2/3 second in nanoseconds
        (0, 500000000, 500000),  # Half second
        (0, 250000000, 250000),  # Quarter second
        (0, 750000000, 750000),  # Three quarters second
        (0, 125000000, 125000),  # 1/8 second
        (0, 375000000, 375000),  # 3/8 second
        (0, 625000000, 625000),  # 5/8 second
        (0, 875000000, 875000),  # 7/8 second
    ],
)
def test_duration_float_precision(seconds, nanoseconds, expected_microseconds):
    """Test Duration float precision handling with various nanosecond values.

    Note: timedelta only supports microsecond precision (6 decimal places),
    so nanosecond values are rounded to the nearest microsecond.
    """
    d = Duration(seconds=seconds, nanoseconds=nanoseconds)
    td = d.to_timedelta()
    assert td.microseconds == expected_microseconds


@pytest.mark.parametrize(
    "duration_str,expected_microseconds",
    [
        ("0.999999999s", 999999),  # Maximum precision rounds to max microseconds
        ("0.999999998s", 999999),  # Rounds to max microseconds
        ("0.000000001s", 0),  # Minimum precision rounds to 0 microseconds
        ("0.1s", 100000),  # 0.1 seconds
        ("0.333333333s", 333333),  # 1/3 second
        ("0.666666666s", 666666),  # 2/3 second
        ("0.5s", 500000),  # Half second
        ("0.25s", 250000),  # Quarter second
        ("0.75s", 750000),  # Three quarters second
        ("0.125s", 125000),  # 1/8 second
        ("0.375s", 375000),  # 3/8 second
        ("0.625s", 625000),  # 5/8 second
        ("0.875s", 875000),  # 7/8 second
    ],
)
def test_duration_parse_precision(duration_str, expected_microseconds):
    """Test Duration parsing precision with various decimal values.

    Note: timedelta only supports microsecond precision (6 decimal places),
    so nanosecond values are rounded to the nearest microsecond.
    """
    d = Duration.parse(duration_str)
    td = d.to_timedelta()
    assert td.microseconds == expected_microseconds


@pytest.mark.parametrize(
    "timestamp_str,expected_nanos",
    [
        ("2021-01-01T12:00:00.999999999Z", 999999999),  # Maximum precision
        ("2021-01-01T12:00:00.999999998Z", 999999998),
        ("2021-01-01T12:00:00.000000001Z", 1),  # Minimum precision
        ("2021-01-01T12:00:00.1Z", 100000000),
        ("2021-01-01T12:00:00.333333333Z", 333333333),  # 1/3 second
        ("2021-01-01T12:00:00.666666666Z", 666666666),  # 2/3 second
        ("2021-01-01T12:00:00.5Z", 500000000),
        ("2021-01-01T12:00:00.25Z", 250000000),
        ("2021-01-01T12:00:00.75Z", 750000000),
        ("2021-01-01T12:00:00.125Z", 125000000),
        ("2021-01-01T12:00:00.375Z", 375000000),
        ("2021-01-01T12:00:00.625Z", 625000000),
        ("2021-01-01T12:00:00.875Z", 875000000),
    ],
)
def test_timestamp_parse_precision(timestamp_str, expected_nanos):
    """Test Timestamp parsing precision with various decimal values."""
    ts = Timestamp.parse(timestamp_str)
    assert ts.nanos == expected_nanos
    # Verify round-trip conversion
    assert ts.to_string() == timestamp_str


@pytest.mark.parametrize(
    "seconds,nanos,expected_microseconds",
    [
        (0, 999999999, 999999),  # Maximum nanoseconds
        (0, 999999998, 999999),
        (0, 1, 0),  # Minimum nanoseconds (rounds to 0 microseconds)
        (0, 100000000, 100000),  # 0.1 seconds
        (0, 333333333, 333333),  # 1/3 second
        (0, 666666666, 666666),  # 2/3 second
        (0, 500000000, 500000),  # Half second
        (0, 250000000, 250000),  # Quarter second
        (0, 750000000, 750000),  # Three quarters second
        (0, 125000000, 125000),  # 1/8 second
        (0, 375000000, 375000),  # 3/8 second
        (0, 625000000, 625000),  # 5/8 second
        (0, 875000000, 875000),  # 7/8 second
    ],
)
def test_timestamp_datetime_precision(seconds, nanos, expected_microseconds):
    """Test Timestamp to datetime conversion precision."""
    ts = Timestamp(seconds=seconds, nanos=nanos)
    dt = ts.to_datetime()
    assert dt.microsecond == expected_microseconds
    # Verify round-trip conversion
    ts2 = Timestamp.from_datetime(dt)
    # Note: We can't expect exact nanos equality due to microsecond rounding
    # but we can verify the microseconds match
    assert ts2.to_datetime().microsecond == expected_microseconds
