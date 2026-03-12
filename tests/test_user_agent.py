import os

import pytest

from databricks.sdk.version import __version__


@pytest.fixture(scope="function")
def user_agent():
    from databricks.sdk import useragent

    orig_product_name = useragent._product_name
    orig_product_version = useragent._product_version
    orig_extra = useragent._extra

    yield useragent

    useragent._product_name = orig_product_name
    useragent._product_version = orig_product_version
    useragent._extra = orig_extra


@pytest.mark.xdist_group(name="user_agent")
def test_user_agent(user_agent):
    user_agent._reset_product()
    default = user_agent.to_string()

    assert "unknown/0.0.0" in default
    assert "databricks-sdk-py/" + __version__ in default
    assert "os/" in default
    assert "python/" in default


@pytest.mark.xdist_group(name="user_agent")
def test_user_agent_with_product(user_agent):
    user_agent.with_product("test", "1.0.0")
    assert "test/1.0.0" in user_agent.to_string()


@pytest.mark.xdist_group(name="user_agent")
def test_user_agent_with_partner(user_agent):
    user_agent.with_partner("test")
    user_agent.with_partner("differenttest")
    assert "partner/test" in user_agent.to_string()
    assert "partner/differenttest" in user_agent.to_string()


@pytest.mark.xdist_group(name="user_agent")
def test_with_extra_is_idempotent(user_agent):
    user_agent.with_extra("foo", "bar")
    user_agent.with_extra("foo", "bar")
    user_agent.with_extra("foo", "bar")
    assert user_agent.to_string().count("foo/bar") == 1


@pytest.mark.xdist_group(name="user_agent")
def test_with_extra_different_values_still_allowed(user_agent):
    user_agent.with_extra("foo", "bar")
    user_agent.with_extra("foo", "wiz")
    ua = user_agent.to_string()
    assert "foo/bar" in ua
    assert "foo/wiz" in ua


@pytest.fixture(scope="function")
def clean_useragent_env():
    # Save and clear env vars.
    original_env = os.environ.copy()
    os.environ.clear()

    # Clear cached CICD and agent providers.
    from databricks.sdk import useragent

    useragent._cicd_provider = None
    useragent._agent_provider = None

    yield

    # Restore env vars and reset caches.
    os.environ.clear()
    os.environ.update(original_env)
    useragent._cicd_provider = None
    useragent._agent_provider = None


def test_user_agent_cicd_no_provider(clean_useragent_env):
    from databricks.sdk import useragent

    user_agent = useragent.to_string()

    assert "cicd" not in user_agent


def test_user_agent_cicd_one_provider(clean_useragent_env):
    os.environ["GITHUB_ACTIONS"] = "true"

    from databricks.sdk import useragent

    user_agent = useragent.to_string()

    assert "cicd/github" in user_agent


def test_user_agent_cicd_two_provider(clean_useragent_env):
    os.environ["GITHUB_ACTIONS"] = "true"
    os.environ["GITLAB_CI"] = "true"

    from databricks.sdk import useragent

    user_agent = useragent.to_string()

    assert "cicd/github" in user_agent


def test_agent_provider_no_agent(clean_useragent_env):
    from databricks.sdk import useragent

    assert useragent.agent_provider() == ""


def test_agent_provider_antigravity(clean_useragent_env):
    os.environ["ANTIGRAVITY_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "antigravity"


def test_agent_provider_claude_code(clean_useragent_env):
    os.environ["CLAUDECODE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "claude-code"


def test_agent_provider_cline(clean_useragent_env):
    os.environ["CLINE_ACTIVE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "cline"


def test_agent_provider_codex(clean_useragent_env):
    os.environ["CODEX_CI"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "codex"


def test_agent_provider_copilot_cli(clean_useragent_env):
    os.environ["COPILOT_CLI"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "copilot-cli"


def test_agent_provider_cursor(clean_useragent_env):
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "cursor"


def test_agent_provider_gemini_cli(clean_useragent_env):
    os.environ["GEMINI_CLI"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "gemini-cli"


def test_agent_provider_opencode(clean_useragent_env):
    os.environ["OPENCODE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "opencode"


def test_agent_provider_multiple_agents(clean_useragent_env):
    os.environ["CLAUDECODE"] = "1"
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == ""


def test_agent_provider_empty_value(clean_useragent_env):
    os.environ["CLAUDECODE"] = ""
    from databricks.sdk import useragent

    assert useragent.agent_provider() == ""


def test_user_agent_string_includes_agent(clean_useragent_env):
    os.environ["CLAUDECODE"] = "1"
    from databricks.sdk import useragent

    ua = useragent.to_string()
    assert "agent/claude-code" in ua


def test_user_agent_string_no_agent(clean_useragent_env):
    from databricks.sdk import useragent

    ua = useragent.to_string()
    assert "agent/" not in ua


def test_user_agent_string_multiple_agents(clean_useragent_env):
    os.environ["CLAUDECODE"] = "1"
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    ua = useragent.to_string()
    assert "agent/" not in ua


def test_agent_provider_cached(clean_useragent_env):
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "cursor"

    # Change the environment: the cached result should persist.
    del os.environ["CURSOR_AGENT"]
    os.environ["CLAUDECODE"] = "1"

    assert useragent.agent_provider() == "cursor"
