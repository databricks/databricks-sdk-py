import datetime
from typing import Any, Callable, Dict, Generic, Optional, Type, TypeVar, Mapping


def _from_dict(d: Dict[str, Any], field: str, cls: Type) -> Any:
    if field not in d or not d[field]:
        return None
    return getattr(cls, 'from_dict')(d[field])


def _repeated(d: Dict[str, Any], field: str, cls: Type) -> Any:
    if field not in d or not d[field]:
        return None
    from_dict = getattr(cls, 'from_dict')
    return [from_dict(v) for v in d[field]]


def _enum(d: Dict[str, Any], field: str, cls: Type) -> Any:
    if field not in d or not d[field]:
        return None
    return getattr(cls, '__members__').get(d[field], None)


ReturnType = TypeVar('ReturnType')


class Wait(Generic[ReturnType]):

    def __init__(self,
                 waiter: Callable,
                 response: Any = None,
                 **kwargs: Mapping[str, Any]) -> None:
        self.response = response

        self._waiter = waiter
        self._bind = kwargs

    def __getattr__(self, key: str) -> Any:
        return self._bind[key]

    def bind(self) -> dict:
        return self._bind

    def result(self,
               timeout: Optional[datetime.timedelta] = datetime.timedelta(minutes=20),
               callback: Optional[Callable[[ReturnType], None]] = None) -> ReturnType:
        kwargs = self._bind.copy()
        return self._waiter(callback=callback, timeout=timeout, **kwargs)
