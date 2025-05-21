"""Common types for the Databricks SDK.

This module provides common types used by different APIs.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta, timezone

_LOG = logging.getLogger("databricks.sdk")

# Python datetime library does not have nanoseconds precision. These classes below are used to work around this limitation.


class Duration:
    """Represents a duration with nanosecond precision.

    This class provides nanosecond precision for durations, which is not supported
    by Python's standard datetime.timedelta.

    Attributes:
        seconds (int): Number of seconds in the duration
        nanoseconds (int): Number of nanoseconds (0-999999999)
    """

    def __init__(self, seconds: int = 0, nanoseconds: int = 0) -> None:
        """Initialize a Duration with seconds and nanoseconds.

        Args:
            seconds: Number of seconds
            nanoseconds: Number of nanoseconds (0-999999999)

        Raises:
            TypeError: If seconds or nanoseconds are not integers
            ValueError: If nanoseconds is not between 0 and 999999999
        """
        if not isinstance(seconds, int):
            raise TypeError("seconds must be an integer")
        if not isinstance(nanoseconds, int):
            raise TypeError("nanoseconds must be an integer")
        if nanoseconds < 0 or nanoseconds >= 1_000_000_000:
            raise ValueError("nanoseconds must be between 0 and 999999999")

        self.seconds = seconds
        self.nanoseconds = nanoseconds

    @classmethod
    def from_timedelta(cls, td: timedelta) -> "Duration":
        """Convert a datetime.timedelta to Duration.

        Args:
            td: The timedelta to convert

        Returns:
            Duration: A new Duration instance with equivalent time span

        Note:
            The conversion may lose precision as timedelta only supports microsecond precision
        """
        total_seconds = int(td.total_seconds())
        # Get the microseconds part and convert to nanoseconds
        microseconds = td.microseconds
        nanoseconds = microseconds * 1000
        return cls(seconds=total_seconds, nanoseconds=nanoseconds)

    def to_timedelta(self) -> timedelta:
        """Convert Duration to datetime.timedelta.

        Returns:
            timedelta: A new timedelta instance with equivalent time span

        Note:
            The conversion may lose precision as timedelta only supports microsecond precision
        """
        # Convert nanoseconds to microseconds for timedelta
        microseconds = self.nanoseconds // 1000
        return timedelta(seconds=self.seconds, microseconds=microseconds)

    def __repr__(self) -> str:
        """Return a string representation of the Duration.

        Returns:
            str: String in the format 'Duration(seconds=X, nanoseconds=Y)'
        """
        return f"Duration(seconds={self.seconds}, nanoseconds={self.nanoseconds})"

    def __eq__(self, other: object) -> bool:
        """Compare this Duration with another object for equality.

        Args:
            other: Object to compare with

        Returns:
            bool: True if other is a Duration with same seconds and nanoseconds
        """
        if not isinstance(other, Duration):
            return NotImplemented
        return self.seconds == other.seconds and self.nanoseconds == other.nanoseconds

    @classmethod
    def parse(cls, duration_str: str) -> "Duration":
        """Parse a duration string in the format 'Xs' where X is a decimal number.

        Examples:
            "3.1s" -> Duration(seconds=3, nanoseconds=100000000)
            "1.5s" -> Duration(seconds=1, nanoseconds=500000000)
            "10s" -> Duration(seconds=10, nanoseconds=0)

        Args:
            duration_str: String in the format 'Xs' where X is a decimal number

        Returns:
            A new Duration instance

        Raises:
            ValueError: If the string format is invalid
        """
        if not duration_str.endswith("s"):
            raise ValueError("Duration string must end with 's'")

        try:
            # Remove the 's' suffix and convert to float
            value = float(duration_str[:-1])
            # Split into integer and fractional parts
            seconds = int(value)
            # Convert fractional part to nanoseconds
            nanoseconds = int((value - seconds) * 1_000_000_000)
            return cls(seconds=seconds, nanoseconds=nanoseconds)
        except ValueError as e:
            raise ValueError(f"Invalid duration format: {duration_str}") from e

    def to_string(self) -> str:
        """Convert Duration to string format 'Xs' where X is a decimal number.

        Examples:
            Duration(seconds=3, nanoseconds=100000000) -> "3.1s"
            Duration(seconds=1, nanoseconds=500000000) -> "1.5s"
            Duration(seconds=10, nanoseconds=0) -> "10s"

        Returns:
            String representation of the duration
        """
        if self.nanoseconds == 0:
            return f"{self.seconds}s"

        # Convert to decimal representation
        total_seconds = self.seconds + (self.nanoseconds / 1_000_000_000)
        # Format with up to 9 decimal places, removing trailing zeros
        return f"{total_seconds:.9f}".rstrip("0").rstrip(".") + "s"


class Timestamp:
    """Represents a timestamp with nanosecond precision.

    This class provides nanosecond precision for timestamps, which is not supported
    by Python's standard datetime. It's compatible with protobuf Timestamp format and
    supports RFC3339 string formatting.

    Attributes:
        seconds (int): Seconds since Unix epoch (1970-01-01T00:00:00Z)
        nanos (int): Nanoseconds (0-999999999)
    """

    # RFC3339 regex pattern for validation and parsing
    _RFC3339_PATTERN = re.compile(
        r"^(\d{4})-(\d{2})-(\d{2})[Tt](\d{2}):(\d{2}):(\d{2})(?:\.(\d+))?(Z|[+-]\d{2}:?\d{2})$"
    )

    def __init__(self, seconds: int = 0, nanos: int = 0) -> None:
        """Initialize a Timestamp with seconds since epoch and nanoseconds.

        Args:
            seconds: Seconds since Unix epoch (1970-01-01T00:00:00Z)
            nanos: Nanoseconds (0-999999999)

        Raises:
            TypeError: If seconds or nanos are not integers
            ValueError: If nanos is not between 0 and 999999999
        """
        if not isinstance(seconds, int):
            raise TypeError("seconds must be an integer")
        if not isinstance(nanos, int):
            raise TypeError("nanos must be an integer")
        if nanos < 0 or nanos >= 1_000_000_000:
            raise ValueError("nanos must be between 0 and 999999999")

        self.seconds = seconds
        self.nanos = nanos

    @classmethod
    def from_datetime(cls, dt: datetime) -> "Timestamp":
        """Convert a datetime.datetime to Timestamp.

        Args:
            dt: The datetime to convert. If naive, it's assumed to be UTC.

        Returns:
            Timestamp: A new Timestamp instance

        Note:
            The datetime is converted to UTC if it isn't already
        """
        # If datetime is naive (no timezone), assume UTC
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        # Convert to UTC
        utc_dt = dt.astimezone(timezone.utc)
        # Use timestamp() to get seconds since epoch
        seconds = int(utc_dt.timestamp())
        nanos = utc_dt.microsecond * 1000
        return cls(seconds=seconds, nanos=nanos)

    def to_datetime(self) -> datetime:
        """Convert Timestamp to datetime.datetime.

        Returns:
            datetime: A new datetime instance in UTC timezone

        Note:
            The returned datetime will have microsecond precision at most
        """
        # Create base datetime from seconds
        dt = datetime.fromtimestamp(self.seconds, tz=timezone.utc)
        # Add nanoseconds converted to microseconds
        microseconds = self.nanos // 1000
        return dt.replace(microsecond=microseconds)

    @classmethod
    def parse(cls, timestamp_str: str) -> "Timestamp":
        """Parse an RFC3339 formatted string into a Timestamp.

        Examples:
            >>> Timestamp.parse("2023-01-01T12:00:00Z")
            >>> Timestamp.parse("2023-01-01T12:00:00.123456789Z")
            >>> Timestamp.parse("2023-01-01T12:00:00+01:00")

        Args:
            timestamp_str: RFC3339 formatted timestamp string

        Returns:
            Timestamp: A new Timestamp instance

        Raises:
            ValueError: If the string format is invalid or not RFC3339 compliant
        """
        match = cls._RFC3339_PATTERN.match(timestamp_str)
        if not match:
            raise ValueError(f"Invalid RFC3339 format: {timestamp_str}")

        year, month, day, hour, minute, second, frac, offset = match.groups()

        # Build the datetime string with a standardized offset format
        dt_str = f"{year}-{month}-{day}T{hour}:{minute}:{second}"
        if frac:
            # Pad or truncate to 9 digits for nanoseconds
            frac = (frac + "000000000")[:9]
            dt_str += f".{frac}"

        # Handle timezone offset
        if offset == "Z":
            dt_str += "+00:00"
        elif ":" not in offset:
            # Insert colon in offset if not present (e.g., +0000 -> +00:00)
            dt_str += f"{offset[:3]}:{offset[3:]}"
        else:
            dt_str += offset

        dt = datetime.fromisoformat(dt_str)
        return cls.from_datetime(dt)

    def to_string(self) -> str:
        """Convert Timestamp to RFC3339 formatted string.

        Returns:
            str: RFC3339 formatted timestamp string in UTC timezone

        Note:
            The string will include nanosecond precision only if nanos > 0
        """
        # Convert seconds to UTC datetime for formatting
        dt = datetime.fromtimestamp(self.seconds, tz=timezone.utc)
        base = dt.strftime("%Y-%m-%dT%H:%M:%S")

        # Add nanoseconds if present
        if self.nanos == 0:
            return base + "Z"

        # Format nanoseconds, removing trailing zeros
        nanos_str = f"{self.nanos:09d}".rstrip("0")
        return f"{base}.{nanos_str}Z"

    def __repr__(self) -> str:
        """Return a string representation of the Timestamp.

        Returns:
            str: String in the format 'Timestamp(seconds=X, nanos=Y)'
        """
        return f"Timestamp(seconds={self.seconds}, nanos={self.nanos})"

    def __eq__(self, other: object) -> bool:
        """Compare this Timestamp with another object for equality.

        Args:
            other: Object to compare with

        Returns:
            bool: True if other is a Timestamp with same seconds and nanos
        """
        if not isinstance(other, Timestamp):
            return NotImplemented
        return self.seconds == other.seconds and self.nanos == other.nanos
