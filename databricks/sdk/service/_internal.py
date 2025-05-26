import datetime
import urllib.parse
from typing import Callable, Dict, Generic, List, Optional, Type, TypeVar, Any
from databricks.sdk import common

def _from_dict(d: Dict[str, any], field: str, cls: Type) -> any:
    if field not in d or d[field] is None:
        return None
    return getattr(cls, "from_dict")(d[field])


def _repeated_dict(d: Dict[str, any], field: str, cls: Type) -> any:
    if field not in d or not d[field]:
        return []
    from_dict = getattr(cls, "from_dict")
    return [from_dict(v) for v in d[field]]


def _get_enum_value(cls: Type, value: str) -> Optional[Type]:
    return next(
        (v for v in getattr(cls, "__members__").values() if v.value == value),
        None,
    )


def _enum(d: Dict[str, any], field: str, cls: Type) -> any:
    """Unknown enum values are returned as None."""
    if field not in d or not d[field]:
        return None
    return _get_enum_value(cls, d[field])


def _repeated_enum(d: Dict[str, any], field: str, cls: Type) -> any:
    """For now, unknown enum values are not included in the response."""
    if field not in d or not d[field]:
        return None
    res = []
    for e in d[field]:
        val = _get_enum_value(cls, e)
        if val:
            res.append(val)
    return res

def _get_duration(d: Dict[str, Any], field: str) -> Optional[common.Duration]:
    if field not in d or d[field] is None:
        return None
    return common.Duration.parse(d[field])

def _repeated_duration(d: Dict[str, Any], field: str) -> Optional[List[common.Duration]]:
    if field not in d or not d[field]:
        return None
    return [common.Duration.parse(v) for v in d[field]]

def _get_timestamp(d: Dict[str, Any], field: str) -> Optional[common.Timestamp]:
    if field not in d or d[field] is None:
        return None
    return common.Timestamp.parse(d[field])

def _repeated_timestamp(d: Dict[str, Any], field: str) -> Optional[List[common.Timestamp]]:
    if field not in d or not d[field]:
        return None
    return [common.Timestamp.parse(v) for v in d[field]]

def _get_value(d: Dict[str, Any], field: str) -> Optional[Any]:
    if field not in d or d[field] is None:
        return None
    return d[field]

def _repeated_value(d: Dict[str, Any], field: str) -> Optional[List[Any]]:
    if field not in d or not d[field]:
        return None
    return d[field]

def _escape_multi_segment_path_parameter(param: str) -> str:
    return urllib.parse.quote(param)


ReturnType = TypeVar("ReturnType")


class Wait(Generic[ReturnType]):

    def __init__(self, waiter: Callable, response: any = None, **kwargs) -> None:
        self.response = response

        self._waiter = waiter
        self._bind = kwargs

    def __getattr__(self, key) -> any:
        return self._bind[key]

    def bind(self) -> dict:
        return self._bind

    def result(
        self,
        timeout: datetime.timedelta = datetime.timedelta(minutes=20),
        callback: Callable[[ReturnType], None] = None,
    ) -> ReturnType:
        kwargs = self._bind.copy()
        return self._waiter(callback=callback, timeout=timeout, **kwargs)
