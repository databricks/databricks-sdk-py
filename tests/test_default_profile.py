"""Tests for [__settings__].default_profile support in config file resolution."""
import pytest

from databricks.sdk.config import Config

from .conftest import noop_credentials


def _write_cfg(tmp_path, content):
    """Write a .databrickscfg file and return a Config kwargs dict pointing to it."""
    cfg_dir = tmp_path / "home"
    cfg_dir.mkdir()
    cfg_file = cfg_dir / ".databrickscfg"
    cfg_file.write_text(content)
    return str(cfg_file)


def test_default_profile_resolves_correctly(tmp_path):
    """default_profile resolves correctly."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = my-workspace

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiXYZ
""",
    )
    cfg = Config(config_file=cfg_file, credentials_strategy=noop_credentials)
    assert cfg.host == "https://my-workspace.cloud.databricks.com"
    assert cfg.token == "dapiXYZ"
    assert cfg.profile == "my-workspace"


def test_default_profile_takes_precedence_over_default_section(tmp_path):
    """default_profile takes precedence over [DEFAULT]."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = my-workspace

[DEFAULT]
host = https://default.cloud.databricks.com
token = dapiOLD

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiXYZ
""",
    )
    cfg = Config(config_file=cfg_file, credentials_strategy=noop_credentials)
    assert cfg.host == "https://my-workspace.cloud.databricks.com"
    assert cfg.token == "dapiXYZ"


def test_legacy_fallback_when_no_settings_section(tmp_path):
    """Legacy fallback when no [__settings__] section."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[DEFAULT]
host = https://default.cloud.databricks.com
token = dapiXYZ
""",
    )
    cfg = Config(config_file=cfg_file, credentials_strategy=noop_credentials)
    assert cfg.host == "https://default.cloud.databricks.com"
    assert cfg.token == "dapiXYZ"


def test_legacy_fallback_when_default_profile_is_empty(tmp_path):
    """Legacy fallback when default_profile is empty."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]

[DEFAULT]
host = https://default.cloud.databricks.com
token = dapiXYZ
""",
    )
    cfg = Config(config_file=cfg_file, credentials_strategy=noop_credentials)
    assert cfg.host == "https://default.cloud.databricks.com"
    assert cfg.token == "dapiXYZ"


def test_settings_section_is_not_a_profile(tmp_path):
    """[__settings__] is not enumerated as a profile; requesting it raises ValueError."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = my-workspace

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiXYZ
""",
    )
    # Explicitly requesting __settings__ as a profile should fail,
    # proving the SDK excludes it from the profile map.
    with pytest.raises(ValueError, match="has no __settings__ profile configured"):
        Config(config_file=cfg_file, profile="__settings__", credentials_strategy=noop_credentials)


def test_default_profile_pointing_to_settings_section_is_rejected(tmp_path):
    """default_profile = __settings__ should fail like any other non-profile target."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = __settings__

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiXYZ
""",
    )
    with pytest.raises(ValueError, match="has no __settings__ profile configured"):
        Config(config_file=cfg_file, credentials_strategy=noop_credentials)


def test_explicit_profile_overrides_default_profile(tmp_path):
    """Explicit --profile overrides default_profile."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = my-workspace

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiABC

[other]
host = https://other.cloud.databricks.com
token = dapiOTHER
""",
    )
    cfg = Config(config_file=cfg_file, profile="other", credentials_strategy=noop_credentials)
    assert cfg.host == "https://other.cloud.databricks.com"
    assert cfg.token == "dapiOTHER"


def test_default_profile_pointing_to_nonexistent_section(tmp_path):
    """default_profile pointing to nonexistent section raises an error."""
    cfg_file = _write_cfg(
        tmp_path,
        """\
[__settings__]
default_profile = deleted-profile

[my-workspace]
host = https://my-workspace.cloud.databricks.com
token = dapiXYZ
""",
    )
    with pytest.raises(ValueError, match="has no deleted-profile profile configured"):
        Config(config_file=cfg_file, credentials_strategy=noop_credentials)
