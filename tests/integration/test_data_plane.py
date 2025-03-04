from databricks.sdk.data_plane import DataPlaneTokenSource


def test_data_plane_token_source(ucws, env_or_skip):
    endpoint = env_or_skip("SERVING_ENDPOINT_NAME")
    serving_endpoint = ucws.serving_endpoints.get(endpoint)
    assert serving_endpoint.data_plane_info is not None
    assert serving_endpoint.data_plane_info.query_info is not None

    info = serving_endpoint.data_plane_info.query_info

    ts = DataPlaneTokenSource(ucws.config.host, ucws._config.oauth_token)
    dp_token = ts.token(info.endpoint_url, info.authorization_details)

    assert dp_token.valid
