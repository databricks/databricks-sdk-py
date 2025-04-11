from databricks.sdk import WorkspaceClient
import logging
logging.basicConfig(level=logging.DEBUG)

w = WorkspaceClient()


# Make a GET request to list users
response = w.api_client.do(
    method="GET",
    path="/api/2.0/account/scim/v2/Users",
    headers={
        "Accept": "application/json"
    }
)

# Print the response
print(response)



