from databricks.sdk.core import Config

def test_parse_dsn():
    cfg = Config.parse_dsn('databricks://user:pass@foo.databricks.com?retry_timeout_seconds=600')

    headers = cfg.authenticate()

    assert headers['Authorization'] == 'Basic dXNlcjpwYXNz'
    assert 'basic' == cfg.auth_type
