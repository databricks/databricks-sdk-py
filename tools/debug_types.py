#!/usr/bin/env python3
"""Debug script to check type annotations."""

import sys
import inspect
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from databricks.sdk.service import tags

# Get the API class
api_class = tags.TagPoliciesAPI

# Get create_tag_policy method
method = getattr(api_class, 'create_tag_policy')

# Get signature
sig = inspect.signature(method)

print("Method signature:", sig)
print("\nParameters:")
for param_name, param in sig.parameters.items():
    print(f"  {param_name}:")
    print(f"    annotation: {param.annotation}")
    print(f"    annotation type: {type(param.annotation)}")
    print(f"    has __name__: {hasattr(param.annotation, '__name__')}")
    if hasattr(param.annotation, '__name__'):
        print(f"    __name__: {param.annotation.__name__}")
    print(f"    has __dataclass_fields__: {hasattr(param.annotation, '__dataclass_fields__')}")

print("\nReturn annotation:")
print(f"  {sig.return_annotation}")
print(f"  type: {type(sig.return_annotation)}")
print(f"  has __name__: {hasattr(sig.return_annotation, '__name__')}")
if hasattr(sig.return_annotation, '__name__'):
    print(f"  __name__: {sig.return_annotation.__name__}")

# Test get_type_hints
print("\n\nUsing get_type_hints:")
try:
    from typing import get_type_hints
    type_hints = get_type_hints(method)
    print("Type hints:")
    for name, hint in type_hints.items():
        print(f"  {name}:")
        print(f"    hint: {hint}")
        print(f"    type: {type(hint)}")
        print(f"    has __name__: {hasattr(hint, '__name__')}")
        if hasattr(hint, '__name__'):
            print(f"    __name__: {hint.__name__}")
        print(f"    has __dataclass_fields__: {hasattr(hint, '__dataclass_fields__')}")
except Exception as e:
    print(f"Error getting type hints: {e}")
    import traceback
    traceback.print_exc()
