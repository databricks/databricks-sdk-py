``a.metastore_assignments``: Account Metastore Assignments
==========================================================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: AccountMetastoreAssignmentsAPI

    These APIs manage metastore assignments to a workspace.

    .. py:method:: create(workspace_id: int, metastore_id: str [, metastore_assignment: Optional[CreateMetastoreAssignment]]) -> AccountsCreateMetastoreAssignmentResponse

        Creates an assignment to a metastore for a workspace

        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_assignment: :class:`CreateMetastoreAssignment` (optional)

        :returns: :class:`AccountsCreateMetastoreAssignmentResponse`
        

    .. py:method:: delete(workspace_id: int, metastore_id: str) -> AccountsDeleteMetastoreAssignmentResponse

        Deletes a metastore assignment to a workspace, leaving the workspace with no metastore.

        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID

        :returns: :class:`AccountsDeleteMetastoreAssignmentResponse`
        

    .. py:method:: get(workspace_id: int) -> AccountsMetastoreAssignment

        Gets the metastore assignment, if any, for the workspace specified by ID. If the workspace is assigned
        a metastore, the mapping will be returned. If no metastore is assigned to the workspace, the
        assignment will not be found and a 404 returned.

        :param workspace_id: int
          Workspace ID.

        :returns: :class:`AccountsMetastoreAssignment`
        

    .. py:method:: list(metastore_id: str) -> Iterator[int]


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            ws = a.metastore_assignments.list(metastore_id=os.environ["TEST_METASTORE_ID"])

        Gets a list of all Databricks workspace IDs that have been assigned to given metastore.

        :param metastore_id: str
          Unity Catalog metastore ID

        :returns: Iterator over int
        

    .. py:method:: update(workspace_id: int, metastore_id: str [, metastore_assignment: Optional[UpdateMetastoreAssignment]]) -> AccountsUpdateMetastoreAssignmentResponse

        Updates an assignment to a metastore for a workspace. Currently, only the default catalog may be
        updated.

        :param workspace_id: int
          Workspace ID.
        :param metastore_id: str
          Unity Catalog metastore ID
        :param metastore_assignment: :class:`UpdateMetastoreAssignment` (optional)

        :returns: :class:`AccountsUpdateMetastoreAssignmentResponse`
        