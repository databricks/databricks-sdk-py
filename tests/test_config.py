import pytest
from databricks.sdk.config import Config

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

@pytest.mark.parametrize('host,expected', [("https://abc.def.ghi", "https://abc.def.ghi"),
                                             ("https://abc.def.ghi/", "https://abc.def.ghi"),
                                             ("abc.def.ghi", "https://abc.def.ghi"),
                                             ("abc.def.ghi/", "https://abc.def.ghi"),
                                             ("https://abc.def.ghi:443", "https://abc.def.ghi"),
                                             ("abc.def.ghi:443", "https://abc.def.ghi")])
def test_config_host_url_format_check(mocker, host, expected):
    mocker.patch('databricks.sdk.config.Config.init_auth')
    assert Config(host=host).host == expected
