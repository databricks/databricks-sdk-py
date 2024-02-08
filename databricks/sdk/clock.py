import abc
import time


class Clock(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def time(self) -> float:
        """
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

        :return: The current time in seconds since the Epoch.
        """
        pass

    @abc.abstractmethod
    def sleep(self, seconds: float) -> None:
        """
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

        :param seconds: The duration to sleep in seconds.
        :return:
        """
        pass


class RealClock(Clock):
    """
    A real clock that uses the ``time`` module to get the current time and sleep.
    """

    def time(self) -> float:
        """
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

        :return: The current time in seconds since the Epoch.
        """
        return time.time()

    def sleep(self, seconds: float) -> None:
        """
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

        :param seconds: The duration to sleep in seconds.
        :return:
        """
        time.sleep(seconds)
