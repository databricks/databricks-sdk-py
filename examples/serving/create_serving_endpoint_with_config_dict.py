from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput

w = WorkspaceClient()

endpoint_config_dict = {
    "served_models": [
        {
            "model_name": "<model_name>",
            "model_version": "<model_version>",
            "scale_to_zero_enabled": True,
            "workload_size": "Small",
        },
        {
            "model_name": "<model_name>",
            "model_version": "<model_version>",
            "scale_to_zero_enabled": True,
            "workload_size": "Small",
        },
    ],
    "traffic_config": {
        "routes": [
            {"served_model_name": "<model_name>-<model_version>", "traffic_percentage": 50},
            {"served_model_name": "<model_name>-<model_version>", "traffic_percentage": 50},
        ]
    },
}

endpoint_config = EndpointCoreConfigInput.from_dict(endpoint_config_dict)
w.serving_endpoints.create_and_wait(name="endpoint-name", config=endpoint_config)