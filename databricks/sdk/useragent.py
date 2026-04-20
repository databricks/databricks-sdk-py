import copy
import logging
import os
import platform
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .version import __version__

# Constants
RUNTIME_KEY = "runtime"
CICD_KEY = "cicd"
AUTH_KEY = "auth"

_product_name = "unknown"
_product_version = "0.0.0"

logger = logging.getLogger("databricks.sdk.useragent")

_extra = []

# Precompiled regex patterns
alphanum_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+$")

# official https://semver.org/ recommendation: https://regex101.com/r/Ly7O1x/
# with addition of "x" wildcards for minor/patch versions. Also, patch version may be omitted.
semver_pattern = re.compile(
    r"^"
    r"(?P<major>0|[1-9]\d*)\.(?P<minor>x|0|[1-9]\d*)(\.(?P<patch>x|0|[1-9x]\d*))?"
    r"(?:-(?P<pre_release>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+(?P<build>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


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
    logger.debug(f"Changing product from {_product_name}/{_product_version} to {name}/{version}")
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
    if (key, value) in _extra:
        return
    logger.debug(f"Adding {key}/{value} to User-Agent")
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
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        runtime_version = os.environ["DATABRICKS_RUNTIME_VERSION"]
        if runtime_version != "":
            runtime_version = _sanitize_header_value(runtime_version)
            return [("runtime", runtime_version)]
    return []


def _sanitize_header_value(value: str) -> str:
    value = value.replace(" ", "-")
    value = value.replace("/", "-")
    return value


def to_string(
    alternate_product_info: Optional[Tuple[str, str]] = None,
    other_info: Optional[List[Tuple[str, str]]] = None,
) -> str:
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
    base.extend(
        [
            ("databricks-sdk-py", __version__),
            ("python", platform.python_version()),
            ("os", platform.uname().system.lower()),
        ]
    )
    if other_info:
        base.extend(other_info)
    base.extend(_extra)
    base.extend(_get_upstream_user_agent_info())
    base.extend(_get_runtime_info())
    if cicd_provider() != "":
        base.append((CICD_KEY, cicd_provider()))
    agent = agent_provider()
    if agent:
        base.append(("agent", agent))
    return " ".join(f"{k}/{v}" for k, v in base)


# List of CI/CD providers and pairs of envvar/value that are used to detect them.
_PROVIDERS = {
    "github": [("GITHUB_ACTIONS", "true")],
    "gitlab": [("GITLAB_CI", "true")],
    "jenkins": [("JENKINS_URL", "")],
    "azure-devops": [("TF_BUILD", "True")],
    "circle": [("CIRCLECI", "true")],
    "travis": [("TRAVIS", "true")],
    "bitbucket": [("BITBUCKET_BUILD_NUMBER", "")],
    "google-cloud-build": [
        ("PROJECT_ID", ""),
        ("BUILD_ID", ""),
        ("PROJECT_NUMBER", ""),
        ("LOCATION", ""),
    ],
    "aws-code-build": [("CODEBUILD_BUILD_ARN", "")],
    "tf-cloud": [("TFC_RUN_ID", "")],
}

# Private variable to store the CI/CD provider. This value is computed at
# the first invocation of cicd_providers() and is cached for subsequent calls.
_cicd_provider = None


def cicd_provider() -> str:
    """Return the CI/CD provider if detected, or an empty string otherwise."""

    # This function is safe because (i) assignation are atomic, and (ii)
    # computating the CI/CD provider is idempotent.
    global _cicd_provider
    if _cicd_provider is not None:
        return _cicd_provider

    providers = []
    for p in _PROVIDERS:
        found = True
        for envvar, value in _PROVIDERS[p]:
            v = os.getenv(envvar)
            if v is None or (value != "" and v != value):
                found = False
                break

        if found:
            providers.append(p)

    if len(providers) == 0:
        _cicd_provider = ""
    else:
        # TODO: reconsider what to do if multiple providers are detected.
        # The current mechanism as the benefit of being deterministic and
        # robust to ordering changes in _PROVIDERS.
        providers.sort()
        _cicd_provider = providers[0]

    return _cicd_provider


# Canonical list of known AI coding agents. Alphabetical by product name.
# Keep this list in sync with databricks-sdk-go and databricks-sdk-java.
#
# Each record has a product name and a list of matchers. A matcher is a
# (env_var, value) pair: an empty value means presence-only (the env var just
# needs to be set, even to an empty string), a non-empty value requires an
# exact match. An agent fires if ANY of its matchers fires. Ambiguity is
# judged by unique product (not raw matcher count), so an agent with two
# overlapping matchers set at the same time still counts as one match.
@dataclass(frozen=True)
class _AgentRecord:
    product: str
    matchers: List[Tuple[str, str]]


_KNOWN_AGENTS: List[_AgentRecord] = [
    _AgentRecord(
        "amp", [("AMP_CURRENT_THREAD_ID", "")]
    ),  # https://ampcode.com/ (also sets AGENT=amp, handled centrally)
    _AgentRecord("antigravity", [("ANTIGRAVITY_AGENT", "")]),  # Closed source (Google)
    _AgentRecord("augment", [("AUGMENT_AGENT", "")]),  # https://www.augmentcode.com/
    _AgentRecord("claude-code", [("CLAUDECODE", "")]),  # https://github.com/anthropics/claude-code
    _AgentRecord("cline", [("CLINE_ACTIVE", "")]),  # https://github.com/cline/cline (v3.24.0+)
    _AgentRecord("codex", [("CODEX_CI", "")]),  # https://github.com/openai/codex
    _AgentRecord("copilot-cli", [("COPILOT_CLI", "")]),  # https://github.com/features/copilot
    _AgentRecord(
        "copilot-vscode", [("COPILOT_MODEL", "")]
    ),  # VS Code Copilot terminal, best-effort heuristic, not officially identified
    _AgentRecord("cursor", [("CURSOR_AGENT", "")]),  # Closed source
    _AgentRecord("gemini-cli", [("GEMINI_CLI", "")]),  # https://google-gemini.github.io/gemini-cli
    _AgentRecord(
        "goose", [("GOOSE_TERMINAL", "")]
    ),  # https://block.github.io/goose/ (also sets AGENT=goose, handled centrally)
    _AgentRecord("kiro", [("KIRO", "")]),  # https://kiro.dev/ (Amazon)
    _AgentRecord("openclaw", [("OPENCLAW_SHELL", "")]),  # https://github.com/anthropics/openclaw
    _AgentRecord("opencode", [("OPENCODE", "")]),  # https://github.com/opencode-ai/opencode
    _AgentRecord("windsurf", [("WINDSURF_AGENT", "")]),  # https://codeium.com/windsurf (Codeium)
]

# Private variable to store the detected agent provider. This value is computed
# at the first invocation of agent_provider() and is cached for subsequent calls.
# Sentinel: None = not yet computed, "" = computed but no agent found.
_agent_provider = None


def _matcher_fires(env_var: str, value: str) -> bool:
    """Return True if the matcher (env_var, value) fires given the current environment.

    Empty value = presence check (env var must be set, even to an empty string).
    Non-empty value = exact match required (empty string does NOT match a non-empty expected value).
    """
    if value == "":
        return env_var in os.environ
    return os.environ.get(env_var) == value


def agent_provider() -> str:
    """Detect if running inside a known AI coding agent.

    Iterates the list of known agents. Each agent fires if ANY of its explicit,
    product-specific matchers fires. If exactly one agent fired, returns its
    product name. If more than one fired, returns empty (ambiguity).

    Explicit agent env vars (e.g. CLAUDECODE, GOOSE_TERMINAL) always take
    precedence. The agents.md-standard AGENT=<name> env var is only consulted
    as a fallback when no explicit matcher fired:
      - If AGENT matches a known product name, return that product.
      - Otherwise return "unknown".

    This means AGENT=<name> never contributes to ambiguity: if any explicit
    matcher fires, AGENT is ignored entirely, even when it names a different
    known product.

    Result is cached after first call.

    Agent env vars can be stacked (e.g. running Cline inside Cursor), so we
    only report when unambiguous across explicit matchers.
    """
    global _agent_provider
    if _agent_provider is not None:
        return _agent_provider

    detected = []
    for agent in _KNOWN_AGENTS:
        for env_var, value in agent.matchers:
            if _matcher_fires(env_var, value):
                detected.append(agent.product)
                break  # count each agent at most once

    if len(detected) == 1:
        _agent_provider = detected[0]
    elif len(detected) > 1:
        _agent_provider = ""
    else:
        # Fallback: honor the agents.md AGENT=<name> standard.
        agent_value = os.environ.get("AGENT", "")
        if agent_value:
            known_products = {a.product for a in _KNOWN_AGENTS}
            if agent_value in known_products:
                _agent_provider = agent_value
            else:
                _agent_provider = "unknown"
        else:
            _agent_provider = ""
    return _agent_provider
