from databricks.sdk.clock import Clock


class FakeClock(Clock):
    """
    A simple clock that can be used to mock time in tests.
    """

    def __init__(self, start_time: float = 0.0):
        self._start_time = start_time

    def time(self) -> float:
        return self._start_time

    def sleep(self, seconds: float) -> None:
        self._start_time += seconds
