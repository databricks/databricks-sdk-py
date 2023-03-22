from typing import Dict, Type


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
    return getattr(cls, '__members__').get(d[field], None)
