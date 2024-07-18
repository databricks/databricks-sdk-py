import copy
import logging
import os
import platform
import re
from typing import List, Optional, Tuple

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


def _match_alphanum(value):
    if not alphanum_pattern.match(value):
        raise ValueError(f"Invalid alphanumeric value: {value}")


def _match_semver(value):
    if not semver_pattern.match(value):
        raise ValueError(f"Invalid semantic version: {value}")


def _match_alphanum_or_semver(value):
    if not alphanum_pattern.match(value) and not semver_pattern.match(value):
        raise ValueError(f"Invalid value: {value}")


def product() -> Tuple[str, str]:
    """Return the global product name and version that will be submitted to Databricks on every request."""
    return _product_name, _product_version


def with_product(name: str, version: str):
    """Change the product name and version that will be submitted to Databricks on every request."""
    global _product_name, _product_version
    _match_alphanum(name)
    _match_semver(version)
    logger.debug(f'Changing product from {_product_name}/{_product_version} to {name}/{version}')
    _product_name = name
    _product_version = version


def _reset_product():
    """[Internal API] Reset product name and version to the default values.

    Used for testing purposes only."""
    global _product_name, _product_version
    _product_name = "unknown"
    _product_version = "0.0.0"


def with_extra(key: str, value: str):
    """Add extra metadata to all requests submitted to Databricks.

    User-specified extra metadata can be inserted into request headers to provide additional context to Databricks
    about usage of different tools in the Databricks ecosystem. This can be useful for collecting telemetry about SDK
    usage from tools that are built on top of the SDK.
    """
    global _extra
    _match_alphanum(key)
    _match_alphanum_or_semver(value)
    logger.debug(f'Adding {key}/{value} to User-Agent')
    _extra.append((key, value))


def extra() -> List[Tuple[str, str]]:
    """Returns the current extra metadata that will be submitted to Databricks on every request."""
    return copy.deepcopy(_extra)


def _reset_extra(extra: List[Tuple[str, str]]):
    """[INTERNAL API] Reset the extra metadata to a new list.

    Prefer using with_user_agent_extra instead of this method to avoid overwriting other information included in the
    user agent."""
    global _extra
    _extra = extra


def with_partner(partner: str):
    """Adds the given partner to the metadata submitted to Databricks on every request."""
    with_extra("partner", partner)


def _get_upstream_user_agent_info() -> List[Tuple[str, str]]:
    """[INTERNAL API] Return the upstream product and version if specified in the system environment."""
    product = os.getenv("DATABRICKS_SDK_UPSTREAM")
    version = os.getenv("DATABRICKS_SDK_UPSTREAM_VERSION")
    if not product or not version:
        return []
    return [("upstream", product), ("upstream-version", version)]


def _get_runtime_info() -> List[Tuple[str, str]]:
    """[INTERNAL API] Return the runtime version if running on Databricks."""
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


def to_string(alternate_product_info: Optional[Tuple[str, str]] = None,
              other_info: Optional[List[Tuple[str, str]]] = None) -> str:
    """Compute the full User-Agent header.

    The User-Agent header contains the product name, version, and other metadata that is submitted to Databricks on
    every request. There are some static components that are included by default in every request, like the SDK version,
    OS name, and Python version. Other components can be optionally overridden or augmented in DatabricksConfig, like
    the product name, product version, and extra user-defined information."""
    base = []
    if alternate_product_info:
        base.append(alternate_product_info)
    else:
        base.append((_product_name, _product_version))
    base.extend([("databricks-sdk-py", __version__), ("python", platform.python_version()),
                 ("os", platform.uname().system.lower()), ])
    if other_info:
        base.extend(other_info)
    base.extend(_extra)
    base.extend(_get_upstream_user_agent_info())
    base.extend(_get_runtime_info())
    return " ".join(f"{k}/{v}" for k, v in base)
