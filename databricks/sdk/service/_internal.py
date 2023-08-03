import datetime
from enum import Enum
from typing import Callable, Dict, Generic, Type, TypeVar


def _from_dict(d: Dict[str, any], field: str, cls: Type) -> any:
    if field not in d or not d[field]:
        return None
    return getattr(cls, 'from_dict')(d[field])


def _repeated(d: Dict[str, any], field: str, cls: Type) -> any:
    if field not in d or not d[field]:
        return None
    from_dict = getattr(cls, 'from_dict')
    return [from_dict(v) for v in d[field]]


def _enum(d: Dict[str, any], field: str, cls: Type) -> any:
    if field not in d or not d[field]:
        return None
    return next((v for v in getattr(cls, '__members__').values() if v.value == d[field]), None)


def _fqcn(x: any) -> str:
    return f'{x.__module__}.{x.__name__}'


def _validated(name: str, cls: Type, inst: any) -> any:
    if not isinstance(inst, cls):
        raise ValueError(f'{name} is expected to be {_fqcn(cls)}, but got {_fqcn(inst.__class__)}')
    if issubclass(cls, Enum):
        return getattr(inst, 'value')
    if hasattr(inst, 'as_dict'):
        return getattr(inst, 'as_dict')()
    return inst


ReturnType = TypeVar('ReturnType')


class Wait(Generic[ReturnType]):

    def __init__(self, waiter: Callable, response: any = None, **kwargs) -> None:
        self.response = response

        self._waiter = waiter
        self._bind = kwargs

    def __getattr__(self, key) -> any:
        return self._bind[key]

    def bind(self) -> dict:
        return self._bind

    def result(self,
               timeout: datetime.timedelta = datetime.timedelta(minutes=20),
               callback: Callable[[ReturnType], None] = None) -> ReturnType:
        kwargs = self._bind.copy()
        return self._waiter(callback=callback, timeout=timeout, **kwargs)
