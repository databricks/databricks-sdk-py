from dataclasses import dataclass
from enum import Enum

import pytest

from databricks.sdk.service._internal import _enum, _from_dict, _repeated_dict, _repeated_enum

class A(Enum):
    a = 'a'
    b = 'b'


def test_enum():
    assert _enum({'field': 'a'}, 'field', A) == A.a

def test_enum_unknown():
    assert _enum({'field': 'c'}, 'field', A) is None

def test_repeated_enum():
    assert _repeated_enum({'field': ['a', 'b']}, 'field', A) == [A.a, A.b]

def test_repeated_enum_unknown():
    assert _repeated_enum({'field': ['a', 'c']}, 'field', A) == [A.a]


@dataclass
class B:
    field: str

    @classmethod
    def from_dict(cls, d: dict) -> 'B':
        return cls(d['field'])

def test_from_dict():
    assert _from_dict({'x': {'field': 'a'}}, 'x', B) == B('a')

def test_repeated_dict():
    assert _repeated_dict({'x': [{'field': 'a'}, {'field': 'c'}]}, 'x', B) == [B('a'), B('c')]
