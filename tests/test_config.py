from databricks.sdk.config import Config

from .conftest import noop_credentials


def test_config_supports_legacy_credentials_provider():
    c = Config(credentials_provider=noop_credentials, product='foo', product_version='1.2.3')
    c2 = c.copy()
    assert c2._product == 'foo'
    assert c2._product_version == '1.2.3'
