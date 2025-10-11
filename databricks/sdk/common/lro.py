from datetime import timedelta
from typing import Optional


class LroOptions:
    """LroOptions is the options for the Long Running Operations.
    DO NOT USE THIS OPTION. This option is still under development
    and can be updated in the future without notice.
    """

    def __init__(self, *, timeout: Optional[timedelta] = None):
        """
        Args:
            timeout: The timeout for the Long Running Operations.
                    If not set, the default timeout is 20 minutes.
        """
        self.timeout = timeout or timedelta(minutes=20)
