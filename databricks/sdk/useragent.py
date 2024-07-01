import logging
import os
import platform
import re
import copy
from typing import Optional, Tuple, List

from .version import __version__

# Constants
RUNTIME_KEY = 'runtime'
CICD_KEY = 'cicd'
AUTH_KEY = 'auth'

_product_name = "unknown"
_product_version = "0.0.0"

logger = logging.getLogger("databricks.sdk.useragent")

_extra = []

# Precompiled regex patterns
alphanum_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+$')
semver_pattern = re.compile(r'^v?(\d+\.)?(\d+\.)?(\*|\d+)$')


def _reset_product():
    """[Internal API] Reset product name and version to the default values.

    Used for testing purposes only."""
    global _product_name, _product_version
    _product_name = "unknown"
    _product_version = "0.0.0"


def match_alphanum(value):
    if not alphanum_pattern.match(value):
        raise ValueError(f"Invalid alphanumeric value: {value}")


def match_semver(value):
    if not semver_pattern.match(value):
        raise ValueError(f"Invalid semantic version: {value}")


def _match_alphanum_or_semver(value):
    if not alphanum_pattern.match(value) and not semver_pattern.match(value):
        raise ValueError(f"Invalid value: {value}")


def product():
    return _product_name, _product_version


def with_product(name: str, version: str):
    """Change the product name and version used in the User-Agent header."""
    global _product_name, _product_version
    match_alphanum(name)
    match_semver(version)
    logger.debug(f'Changing product from {_product_name}/{_product_version} to {name}/{version}')
    _product_name = name
    _product_version = version


def with_user_agent_extra(key: str, value: str):
    """Add extra metadata to the User-Agent header when developing a library."""
    global _extra
    match_alphanum(key)
    _match_alphanum_or_semver(value)
    logger.debug(f'Adding {key}/{value} to User-Agent')
    _extra.append((key, value))


def extra() -> List[Tuple[str, str]]:
    return copy.deepcopy(_extra)


def reset_extra(extra: List[Tuple[str, str]]):
    """Reset the extra metadata to a new list.

    Prefer using with_user_agent_extra instead of this method to avoid overwriting other information included in the
    user agent."""
    global _extra
    _extra = extra


def with_partner(partner):
    with_user_agent_extra("partner", partner)


def get_upstream_user_agent_info():
    product = os.getenv("DATABRICKS_SDK_UPSTREAM")
    version = os.getenv("DATABRICKS_SDK_UPSTREAM_VERSION")
    if not product or not version:
        return []
    return [("upstream", product), ("upstream-version", version)]


def _get_runtime_info():
    if 'DATABRICKS_RUNTIME_VERSION' in os.environ:
        runtime_version = os.environ['DATABRICKS_RUNTIME_VERSION']
        if runtime_version != '':
            runtime_version = _sanitize_header_value(runtime_version)
            return [('runtime', runtime_version)]
    return []


def _sanitize_header_value(value: str) -> str:
    value = value.replace(' ', '-')
    value = value.replace('/', '-')
    return value


def to_string(alternate_product_info: Optional[Tuple[str, str]] = None, other_info: Optional[List[Tuple[str, str]]] = None) -> str:
    base = []
    if alternate_product_info:
        base.append(alternate_product_info)
    else:
        base.append((_product_name, _product_version))
    base.extend([
        ("databricks-sdk-py", __version__),
        ("python", platform.python_version()),
        ("os", platform.uname().system.lower()),
    ])
    if other_info:
        base.extend(other_info)
    base.extend(_extra)
    base.extend(get_upstream_user_agent_info())
    base.extend(_get_runtime_info())
    return " ".join(f"{k}/{v}" for k, v in base)
