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


def test_config_host_url_format_check(mocker):
    mocker.patch('databricks.sdk.config.Config.init_auth')

    c1 = Config(host="abc.def.ghi/")
    c2 = Config(host="https://abc.def.ghi/")
    c3 = Config(host="https://abc.def.ghi")
    c4 = Config(host="abc.def.ghi")

    assert c1.host == "https://abc.def.ghi"
    assert c2.host == "https://abc.def.ghi"
    assert c3.host == "https://abc.def.ghi"
    assert c4.host == "https://abc.def.ghi"
