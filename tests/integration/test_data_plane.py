from databricks.sdk.databricks.data_plane import DataPlaneTokenSource

# TODO: Re-enable this after adding data plane services to the SDK
# def test_data_plane_token_source(ucws, env_or_skip):
#     endpoint = env_or_skip("SERVING_ENDPOINT_NAME")
#     serving_endpoint = ucws.serving_endpoints.get(endpoint)
#     assert serving_endpoint.data_plane_info is not None
#     assert serving_endpoint.data_plane_info.query_info is not None

#     info = serving_endpoint.data_plane_info.query_info

#     ts = DataPlaneTokenSource(ucws.config.host, ucws._config.oauth_token)
#     dp_token = ts.token(info.endpoint_url, info.authorization_details)

#     assert dp_token.valid


# def test_model_serving_data_plane(ucws, env_or_skip):
#     endpoint = env_or_skip("SERVING_ENDPOINT_NAME")
#     serving_endpoints = ucws.serving_endpoints_data_plane
#     response = serving_endpoints.query(name=endpoint, dataframe_records=[{"col": 1.0}])
#     assert response is not None
