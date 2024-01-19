from databricks.sdk.core import Config
from databricks.sdk.environments import ALL_ENVS, Cloud


def test_environment_aws():
    c = Config(host="https://test.cloud.databricks.com", token="token")
    assert c.environment.cloud == Cloud.AWS
    assert c.environment.dns_zone == ".cloud.databricks.com"


def test_environment_azure():
    c = Config(host="https://test.dev.azuredatabricks.net", token="token")
    assert c.environment.cloud == Cloud.AZURE
    assert c.environment.dns_zone == ".dev.azuredatabricks.net"


def test_default_environment_can_be_overridden():
    c = Config(host="https://test.cloud.databricks.com", token="token", databricks_environment=ALL_ENVS[1])
    assert c.environment == ALL_ENVS[1]
