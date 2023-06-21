Connections
===========
.. py:class:: ConnectionsAPI

    Connections allow for creating a connection to an external data source.
    
    A connection is an abstraction of an external data source that can be connected from Databricks Compute.
    Creating a connection object is the first step to managing external data sources within Unity Catalog,
    with the second step being creating a data object (catalog, schema, or table) using the connection. Data
    objects derived from a connection can be written to or read from similar to other Unity Catalog data
    objects based on cloud storage. Users may create different types of connections with each connection
    having a unique set of configuration options to support credential management and other settings.

    .. py:method:: create(name, connection_type, options_kvpairs [, comment, owner, properties_kvpairs, read_only])

        Create a connection.
        
        Creates a new connection
        
        Creates a new connection to an external data source. It allows users to specify connection details and
        configurations for interaction with the external server.
        
        :param name: str
          Name of the connection.
        :param connection_type: :class:`ConnectionType`
          The type of connection.
        :param options_kvpairs: :class:`OptionsKvPairs`
          Object properties as map of string key-value pairs.
        :param comment: str (optional)
          User-provided free-form text description.
        :param owner: str (optional)
          Username of current owner of the connection.
        :param properties_kvpairs: Dict[str,str] (optional)
          An object containing map of key-value properties attached to the connection.
        :param read_only: bool (optional)
          If the connection is read only.
        
        :returns: :class:`ConnectionInfo`
        

    .. py:method:: delete(name_arg)

        Delete a connection.
        
        Deletes the connection that matches the supplied name.
        
        :param name_arg: str
          The name of the connection to be deleted.
        
        
        

    .. py:method:: get(name_arg)

        Get a connection.
        
        Gets a connection from it's name.
        
        :param name_arg: str
          Name of the connection.
        
        :returns: :class:`ConnectionInfo`
        

    .. py:method:: list()

        List connections.
        
        List all connections.
        
        :returns: Iterator over :class:`ConnectionInfo`
        

    .. py:method:: update(name, options_kvpairs, name_arg)

        Update a connection.
        
        Updates the connection that matches the supplied name.
        
        :param name: str
          Name of the connection.
        :param options_kvpairs: :class:`OptionsKvPairs`
          Object properties as map of string key-value pairs.
        :param name_arg: str
          Name of the connection.
        
        :returns: :class:`ConnectionInfo`
        