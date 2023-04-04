#!env python3
from databricks.sdk import WorkspaceClient

from databricks.sdk.service.jobs import JobsAPI



if __name__ == '__main__':
    host = input('Enter Databricks host: ')

    w = WorkspaceClient(host=host, auth_type='external-browser')
    clusters = w.clusters.list()

    for cl in clusters:
        print(f' - {cl.cluster_name} is {cl.state}')
