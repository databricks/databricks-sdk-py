``a.metastores``: Account Metastores
====================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AccountMetastoresAPI

    These APIs manage Unity Catalog metastores for an account. A metastore contains catalogs that can be
    associated with workspaces

    .. py:method:: create( [, metastore_info: Optional[CreateAccountsMetastore]]) -> AccountsCreateMetastoreResponse

        Creates a Unity Catalog metastore.

        :param metastore_info: :class:`CreateAccountsMetastore` (optional)

        :returns: :class:`AccountsCreateMetastoreResponse`
        

    .. py:method:: delete(metastore_id: str [, force: Optional[bool]]) -> AccountsDeleteMetastoreResponse

        Deletes a Unity Catalog metastore for an account, both specified by ID.

        :param metastore_id: str
          Unity Catalog metastore ID
        :param force: bool (optional)
          Force deletion even if the metastore is not empty. Default is false.

        :returns: :class:`AccountsDeleteMetastoreResponse`
        

    .. py:method:: get(metastore_id: str) -> AccountsGetMetastoreResponse

        Gets a Unity Catalog metastore from an account, both specified by ID.

        :param metastore_id: str
          Unity Catalog metastore ID

        :returns: :class:`AccountsGetMetastoreResponse`
        

    .. py:method:: list() -> Iterator[MetastoreInfo]

        Gets all Unity Catalog metastores associated with an account specified by ID.


        :returns: Iterator over :class:`MetastoreInfo`
        

    .. py:method:: update(metastore_id: str [, metastore_info: Optional[UpdateAccountsMetastore]]) -> AccountsUpdateMetastoreResponse

        Updates an existing Unity Catalog metastore.

        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_info: :class:`UpdateAccountsMetastore` (optional)
          Properties of the metastore to change.

        :returns: :class:`AccountsUpdateMetastoreResponse`
        