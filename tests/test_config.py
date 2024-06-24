import platform

from databricks.sdk.config import Config, with_product, with_user_agent_extra
from databricks.sdk.version import __version__

from .conftest import noop_credentials


def test_config_copy_preserves_product_and_product_version():
    c = Config(credentials_strategy=noop_credentials, product='foo', product_version='1.2.3')
    c2 = c.copy()
    assert c2._product == 'foo'
    assert c2._product_version == '1.2.3'


def test_config_supports_legacy_credentials_provider():
    c = Config(credentials_provider=noop_credentials, product='foo', product_version='1.2.3')
    c2 = c.copy()
    assert c2._product == 'foo'
    assert c2._product_version == '1.2.3'


def test_extra_and_upstream_user_agent(monkeypatch):

    class MockUname:

        @property
        def system(self):
            return 'TestOS'

    monkeypatch.setattr(platform, 'python_version', lambda: '3.0.0')
    monkeypatch.setattr(platform, 'uname', MockUname)
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM', "upstream-product")
    monkeypatch.setenv('DATABRICKS_SDK_UPSTREAM_VERSION', "0.0.1")
    monkeypatch.setenv('DATABRICKS_RUNTIME_VERSION', "13.1 anything/else")

    config = Config(host='http://localhost', username="something", password="something", product='test',
                    product_version='0.0.0') \
        .with_user_agent_extra('test-extra-1', '1') \
        .with_user_agent_extra('test-extra-2', '2')

    assert config.user_agent == (
        f"test/0.0.0 databricks-sdk-py/{__version__} python/3.0.0 os/testos auth/basic"
        f" test-extra-1/1 test-extra-2/2 upstream/upstream-product upstream-version/0.0.1"
        " runtime/13.1-anything-else")

    with_product('some-product', '0.32.1')
    config2 = Config(host='http://localhost', token='...')
    assert config2.user_agent.startswith('some-product/0.32.1')

    config3 = Config(host='http://localhost', token='...', product='abc', product_version='1.2.3')
    assert not config3.user_agent.startswith('some-product/0.32.1')


def test_config_copy_deep_copies_user_agent_other_info(config):
    config_copy = config.copy()

    config.with_user_agent_extra("test", "test1")
    assert "test/test1" not in config_copy.user_agent
    assert "test/test1" in config.user_agent

    config_copy.with_user_agent_extra("test", "test2")
    assert "test/test2" in config_copy.user_agent
    assert "test/test2" not in config.user_agent

    with_user_agent_extra("blueprint", "0.4.6")
    assert "blueprint/0.4.6" in config.user_agent
    assert "blueprint/0.4.6" in config_copy.user_agent
