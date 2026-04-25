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


def test_agent_provider_openclaw(clean_useragent_env):
    os.environ["OPENCLAW_SHELL"] = "exec"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "openclaw"


def test_agent_provider_goose_env_var(clean_useragent_env):
    os.environ["GOOSE_TERMINAL"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "goose"


def test_agent_provider_goose_via_agent_standard(clean_useragent_env):
    os.environ["AGENT"] = "goose"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "goose"


def test_agent_provider_goose_both_signals(clean_useragent_env):
    # Both the dedicated env var and the AGENT=goose standard are set.
    # This should NOT be ambiguous - it's still a single agent (goose).
    os.environ["GOOSE_TERMINAL"] = "1"
    os.environ["AGENT"] = "goose"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "goose"


def test_agent_provider_amp_env_var(clean_useragent_env):
    os.environ["AMP_CURRENT_THREAD_ID"] = "thread-123"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "amp"


def test_agent_provider_amp_via_agent_standard(clean_useragent_env):
    os.environ["AGENT"] = "amp"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "amp"


def test_agent_provider_amp_both_signals(clean_useragent_env):
    # Both AMP_CURRENT_THREAD_ID and AGENT=amp set - still single agent.
    os.environ["AMP_CURRENT_THREAD_ID"] = "thread-123"
    os.environ["AGENT"] = "amp"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "amp"


def test_agent_provider_augment(clean_useragent_env):
    os.environ["AUGMENT_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "augment"


def test_agent_provider_copilot_vscode(clean_useragent_env):
    os.environ["COPILOT_MODEL"] = "gpt-4"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "copilot-vscode"


def test_agent_provider_kiro(clean_useragent_env):
    os.environ["KIRO"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "kiro"


def test_agent_provider_windsurf(clean_useragent_env):
    os.environ["WINDSURF_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "windsurf"


def test_agent_provider_unknown_agent_fallback(clean_useragent_env):
    # AGENT set to a value that doesn't match any known agent
    # should fall back to "unknown".
    os.environ["AGENT"] = "someweirdthing"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "unknown"


def test_agent_provider_agent_known_product_name_fallback(clean_useragent_env):
    # AGENT=<known product name> with no other matchers set should resolve
    # to the matching product (e.g. cursor is only identified by CURSOR_AGENT;
    # AGENT=cursor is a reasonable implicit signal to attribute it).
    os.environ["AGENT"] = "cursor"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "cursor"


def test_agent_provider_known_matcher_wins_over_agent_fallback(clean_useragent_env):
    # When a known matcher fires, it wins even if AGENT is set to an
    # unrelated value. The AGENT fallback only applies when nothing else hits.
    os.environ["AGENT"] = "somethingweird"
    os.environ["CLAUDECODE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "claude-code"


def test_agent_provider_agent_empty_string(clean_useragent_env):
    # AGENT="" (empty) should NOT trigger the fallback.
    os.environ["AGENT"] = ""
    from databricks.sdk import useragent

    assert useragent.agent_provider() == ""


def test_agent_provider_multiple_agents(clean_useragent_env):
    # Nested agents (e.g. Claude Code spawning a Cursor CLI subagent) set
    # multiple explicit matchers on the same process.
    os.environ["CLAUDECODE"] = "1"
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "multiple"


def test_agent_provider_three_stacked_agents(clean_useragent_env):
    os.environ["CLAUDECODE"] = "1"
    os.environ["CURSOR_AGENT"] = "1"
    os.environ["AUGMENT_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "multiple"


def test_agent_provider_explicit_wins_over_agent_naming_different_product(clean_useragent_env):
    # Explicit env vars always win over the generic AGENT=<name> signal.
    # AGENT=goose names a different known product, but CLAUDECODE is explicit,
    # so claude-code wins. AGENT is ignored entirely when any explicit
    # matcher fires.
    os.environ["AGENT"] = "goose"
    os.environ["CLAUDECODE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "claude-code"


def test_agent_provider_explicit_goose_wins_over_agent_cursor(clean_useragent_env):
    # Mirror of the above: GOOSE_TERMINAL is explicit, AGENT=cursor names a
    # different known product. Explicit wins; AGENT is ignored.
    os.environ["GOOSE_TERMINAL"] = "1"
    os.environ["AGENT"] = "cursor"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "goose"


def test_agent_provider_copilot_cli_and_vscode_collapses_to_copilot_cli(clean_useragent_env):
    # Copilot CLI users (BYOK mode) often set COPILOT_MODEL alongside
    # COPILOT_CLI. Treat the pair as a single copilot-cli signal rather than
    # a stacked multi-agent setup.
    os.environ["COPILOT_CLI"] = "1"
    os.environ["COPILOT_MODEL"] = "gpt-4"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "copilot-cli"


def test_agent_provider_copilot_byok_collapse_then_still_multiple(clean_useragent_env):
    # The Copilot BYOK collapse only removes the copilot-vscode match. If
    # another agent is also present, the result is still "multiple".
    os.environ["COPILOT_CLI"] = "1"
    os.environ["COPILOT_MODEL"] = "gpt-4"
    os.environ["CLAUDECODE"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "multiple"


def test_agent_provider_empty_value_still_counts_as_set(clean_useragent_env):
    # Presence-only matchers fire even when the env var is set to an empty
    # string. Parity with Go (os.LookupEnv) and Java (env.get != null).
    os.environ["CLAUDECODE"] = ""
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "claude-code"


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
    assert "agent/multiple" in ua


def test_agent_provider_cached(clean_useragent_env):
    os.environ["CURSOR_AGENT"] = "1"
    from databricks.sdk import useragent

    assert useragent.agent_provider() == "cursor"

    # Change the environment: the cached result should persist.
    del os.environ["CURSOR_AGENT"]
    os.environ["CLAUDECODE"] = "1"

    assert useragent.agent_provider() == "cursor"
