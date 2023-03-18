from databricks.sdk import WorkspaceClient

if __name__ == '__main__':
    host = input('Enter Databricks host: ')

    w = WorkspaceClient(host=host, client_id='local-browser')
    clusters = w.clusters.list()

    for cl in clusters:
        print(f' - {cl.cluster_name} is {cl.state}')
