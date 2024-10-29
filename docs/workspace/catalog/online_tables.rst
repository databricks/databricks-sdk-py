``w.online_tables``: Online Tables
==================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: OnlineTablesAPI

    Online tables provide lower latency and higher QPS access to data from Delta tables.

    .. py:method:: create( [, name: Optional[str], spec: Optional[OnlineTableSpec]]) -> OnlineTable

        Create an Online Table.

Create a new Online Table.

:param name: str (optional)
  Full three-part (catalog, schema, table) name of the table.
:param spec: :class:`OnlineTableSpec` (optional)
  Specification of the online table.

:returns: :class:`OnlineTable`


    .. py:method:: delete(name: str)

        Delete an Online Table.

Delete an online table. Warning: This will delete all the data in the online table. If the source
Delta table was deleted or modified since this Online Table was created, this will lose the data
forever!

:param name: str
  Full three-part (catalog, schema, table) name of the table.




    .. py:method:: get(name: str) -> OnlineTable

        Get an Online Table.

Get information about an existing online table and its status.

:param name: str
  Full three-part (catalog, schema, table) name of the table.

:returns: :class:`OnlineTable`
