from databricks.sdk.config import Config
import os

__tests__ = os.path.dirname(__file__)


def test_load_azure_tenant_id(requests_mock, monkeypatch):
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    mock = requests_mock.get('https://abc123.azuredatabricks.net/aad/auth', status_code=302, headers={'Location': 'https://login.microsoftonline.com/abc123xyz/oauth2/authorize'})
    cfg = Config(host="https://abc123.azuredatabricks.net")
    assert cfg.azure_tenant_id == 'abc123xyz'
    assert mock.called_once


def test_load_azure_tenant_id_tenant_id_set(requests_mock, monkeypatch):
    monkeypatch.setenv('PATH', __tests__ + '/testdata:/bin')
    mock = requests_mock.get('https://abc123.azuredatabricks.net/aad/auth', status_code=302, headers={'Location': 'https://login.microsoftonline.com/abc123xyz/oauth2/authorize'})
    cfg = Config(host="https://abc123.azuredatabricks.net", azure_tenant_id="123456789")
    assert cfg.azure_tenant_id == '123456789'
    assert mock.call_count == 0
