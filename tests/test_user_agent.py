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

    assert 'unknown/0.0.0' in default
    assert 'databricks-sdk-py/' + __version__ in default
    assert 'os/' in default
    assert 'python/' in default


@pytest.mark.xdist_group(name="user_agent")
def test_user_agent_with_product(user_agent):
    user_agent.with_product('test', '1.0.0')
    assert 'test/1.0.0' in user_agent.to_string()


@pytest.mark.xdist_group(name="user_agent")
def test_user_agent_with_partner(user_agent):
    user_agent.with_partner('test')
    user_agent.with_partner('differenttest')
    assert 'partner/test' in user_agent.to_string()
    assert 'partner/differenttest' in user_agent.to_string()
