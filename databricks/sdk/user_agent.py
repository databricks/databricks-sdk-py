import os
import platform
import re

from .version import __version__

# Constants
RUNTIME_KEY = 'runtime'
CICD_KEY = 'cicd'
AUTH_KEY = 'auth'

product_name = "unknown"
product_version = "0.0.0"

_extra = []

# Precompiled regex patterns
alphanum_pattern = re.compile(r'^[a-zA-Z0-9]+$')
semver_pattern = re.compile(r'^v?(\d+\.)?(\d+\.)?(\*|\d+)$')


def match_alphanum(value):
    if not alphanum_pattern.match(value):
        raise ValueError(f"Invalid alphanumeric value: {value}")


def match_semver(value):
    if not semver_pattern.match(value):
        raise ValueError(f"Invalid semantic version: {value}")


def _match_alphanum_or_semver(value):
    if not alphanum_pattern.match(value) and not semver_pattern.match(value):
        raise ValueError(f"Invalid value: {value}")


def with_product(name, version):
    global product_name, product_version
    match_alphanum(name)
    match_semver(version)
    product_name = name
    product_version = version


def with_user_agent_extra(key, value):
    global _extra
    match_alphanum(key)
    _match_alphanum_or_semver(value)
    _extra.append((key, value))


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


def to_string():
    base = [(product_name, product_version), ("databricks-sdk-py", __version__),
            ("python", platform.python_version()), ("os", platform.uname().system.lower())]
    base.extend(_extra)
    base.extend(get_upstream_user_agent_info())
    base.extend(_get_runtime_info())
    return " ".join(f"{k}/{v}" for k, v in base)


