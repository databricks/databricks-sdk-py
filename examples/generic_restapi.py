from databricks.sdk import WorkspaceClient

if __name__ == "__main__":

    w = WorkspaceClient()

    # Make a GET request to list cluster policies
    response = w.api_client.do(
        method="GET",
        path="/api/2.0/policies/clusters/list",
        headers={
            "Accept": "application/json"
        }
    )

    # Print the response
    print(response)



