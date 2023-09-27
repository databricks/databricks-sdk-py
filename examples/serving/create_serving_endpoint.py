from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import (EndpointCoreConfigInput, Route, ServedModelInput, TrafficConfig)

w = WorkspaceClient()

served_model_1 = ServedModelInput(model_name="model_name",
                                  model_version="model_version",
                                  workload_size="Small",
                                  scale_to_zero_enabled=True)
served_model_2 = ServedModelInput(model_name="model_name",
                                  model_version="model_version",
                                  workload_size="Small",
                                  scale_to_zero_enabled=True)

route_1 = Route(served_model_name=f"{served_model_1.model_name}-{served_model_1.model_version}",
                traffic_percentage=50)
route_2 = Route(served_model_name=f"{served_model_2.model_name}-{served_model_2.model_version}",
                traffic_percentage=50)

traffic_config = TrafficConfig(routes=[route_1, route_2])

endpoint_config = EndpointCoreConfigInput(served_models=[served_model_1, served_model_2],
                                          traffic_config=traffic_config)

w.serving_endpoints.create_and_wait(name="endpoint-name", config=endpoint_config)
