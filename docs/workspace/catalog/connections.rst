``w.connections``: Connections
==============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: ConnectionsAPI

    Connections allow for creating a connection to an external data source.

    A connection is an abstraction of an external data source that can be connected from Databricks Compute.
    Creating a connection object is the first step to managing external data sources within Unity Catalog,
    with the second step being creating a data object (catalog, schema, or table) using the connection. Data
    objects derived from a connection can be written to or read from similar to other Unity Catalog data
    objects based on cloud storage. Users may create different types of connections with each connection
    having a unique set of configuration options to support credential management and other settings.

    .. py:method:: create(name: str, connection_type: ConnectionType, options: Dict[str, str] [, comment: Optional[str], properties: Optional[Dict[str, str]], read_only: Optional[bool]]) -> ConnectionInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            conn_create = w.connections.create(
                comment="Go SDK Acceptance Test Connection",
                connection_type=catalog.ConnectionType.DATABRICKS,
                name=f"sdk-{time.time_ns()}",
                options={
                    "host": "%s-fake-workspace.cloud.databricks.com" % (f"sdk-{time.time_ns()}"),
                    "httpPath": "/sql/1.0/warehouses/%s" % (f"sdk-{time.time_ns()}"),
                    "personalAccessToken": f"sdk-{time.time_ns()}",
                },
            )
            
            # cleanup
            w.connections.delete(name=conn_create.name)

        Creates a new connection

        Creates a new connection to an external data source. It allows users to specify connection details and
        configurations for interaction with the external server.

        :param name: str
          Name of the connection.
        :param connection_type: :class:`ConnectionType`
          The type of connection.
        :param options: Dict[str,str]
          A map of key-value properties attached to the securable.
        :param comment: str (optional)
          User-provided free-form text description.
        :param properties: Dict[str,str] (optional)
          A map of key-value properties attached to the securable.
        :param read_only: bool (optional)
          If the connection is read only.

        :returns: :class:`ConnectionInfo`
        

    .. py:method:: delete(name: str)

        Deletes the connection that matches the supplied name.

        :param name: str
          The name of the connection to be deleted.


        

    .. py:method:: get(name: str) -> ConnectionInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            conn_create = w.connections.create(
                comment="Go SDK Acceptance Test Connection",
                connection_type=catalog.ConnectionType.DATABRICKS,
                name=f"sdk-{time.time_ns()}",
                options={
                    "host": "%s-fake-workspace.cloud.databricks.com" % (f"sdk-{time.time_ns()}"),
                    "httpPath": "/sql/1.0/warehouses/%s" % (f"sdk-{time.time_ns()}"),
                    "personalAccessToken": f"sdk-{time.time_ns()}",
                },
            )
            
            conn_update = w.connections.update(
                name=conn_create.name,
                options={
                    "host": "%s-fake-workspace.cloud.databricks.com" % (f"sdk-{time.time_ns()}"),
                    "httpPath": "/sql/1.0/warehouses/%s" % (f"sdk-{time.time_ns()}"),
                    "personalAccessToken": f"sdk-{time.time_ns()}",
                },
            )
            
            conn = w.connections.get(name=conn_update.name)
            
            # cleanup
            w.connections.delete(name=conn_create.name)

        Gets a connection from it's name.

        :param name: str
          Name of the connection.

        :returns: :class:`ConnectionInfo`
        

    .. py:method:: list( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[ConnectionInfo]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            conn_list = w.connections.list(catalog.ListConnectionsRequest())

        List all connections.

        :param max_results: int (optional)
          Maximum number of connections to return. - If not set, all connections are returned (not
          recommended). - when set to a value greater than 0, the page length is the minimum of this value and
          a server configured value; - when set to 0, the page length is set to a server configured value
          (recommended); - when set to a value less than 0, an invalid parameter error is returned;
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`ConnectionInfo`
        

    .. py:method:: update(name: str, options: Dict[str, str] [, new_name: Optional[str], owner: Optional[str]]) -> ConnectionInfo


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import catalog
            
            w = WorkspaceClient()
            
            conn_create = w.connections.create(
                comment="Go SDK Acceptance Test Connection",
                connection_type=catalog.ConnectionType.DATABRICKS,
                name=f"sdk-{time.time_ns()}",
                options={
                    "host": "%s-fake-workspace.cloud.databricks.com" % (f"sdk-{time.time_ns()}"),
                    "httpPath": "/sql/1.0/warehouses/%s" % (f"sdk-{time.time_ns()}"),
                    "personalAccessToken": f"sdk-{time.time_ns()}",
                },
            )
            
            conn_update = w.connections.update(
                name=conn_create.name,
                options={
                    "host": "%s-fake-workspace.cloud.databricks.com" % (f"sdk-{time.time_ns()}"),
                    "httpPath": "/sql/1.0/warehouses/%s" % (f"sdk-{time.time_ns()}"),
                    "personalAccessToken": f"sdk-{time.time_ns()}",
                },
            )
            
            # cleanup
            w.connections.delete(name=conn_create.name)

        Updates the connection that matches the supplied name.

        :param name: str
          Name of the connection.
        :param options: Dict[str,str]
          A map of key-value properties attached to the securable.
        :param new_name: str (optional)
          New name for the connection.
        :param owner: str (optional)
          Username of current owner of the connection.

        :returns: :class:`ConnectionInfo`
        