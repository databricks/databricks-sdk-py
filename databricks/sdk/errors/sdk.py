__all__ = ['OperationFailed', 'OperationTimeout']


class OperationFailed(RuntimeError):
    pass


class OperationTimeout(RuntimeError, TimeoutError):
    pass
