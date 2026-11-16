``w.queries``: Queries
======================
.. currentmodule:: databricks.sdk.service.sql

.. py:class:: QueriesAPI

    The queries API can be used to perform CRUD operations on queries. A query is a Databricks SQL object that
    includes the target SQL warehouse, query text, name, description, tags, and parameters. Queries can be
    scheduled using the ``sql_task`` type of the Jobs API, e.g. :method:jobs/create.

    .. py:method:: create( [, auto_resolve_display_name: Optional[bool], query: Optional[CreateQueryRequestQuery]]) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(
                query=sql.CreateQueryRequestQuery(
                    display_name=f"sdk-{time.time_ns()}",
                    warehouse_id=srcs[0].warehouse_id,
                    description="test query from Go SDK",
                    query_text="SELECT 1",
                )
            )
            
            # cleanup
            w.queries.delete(id=query.id)

        Creates a query. The caller becomes the owner of the new query.

        :param auto_resolve_display_name: bool (optional)
          If true, automatically resolve query display name conflicts. Otherwise, fail the request if the
          query's display name conflicts with an existing query's display name.
        :param query: :class:`CreateQueryRequestQuery` (optional)
          The query to create. A display name and query text are required.

        :returns: :class:`Query`
        

    .. py:method:: delete(id: str)

        Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and
        cannot be used for alerts. You can restore a trashed query through the UI. A trashed query is
        permanently deleted after 30 days.

        :param id: str
          UUID of the query to move to the trash.


        

    .. py:method:: get(id: str) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(
                query=sql.CreateQueryRequestQuery(
                    display_name=f"sdk-{time.time_ns()}",
                    warehouse_id=srcs[0].warehouse_id,
                    description="test query from Go SDK",
                    query_text="SHOW TABLES",
                )
            )
            
            by_id = w.queries.get(id=query.id)
            
            # cleanup
            w.queries.delete(id=query.id)

        Gets a query.

        :param id: str
          UUID of the query to fetch.

        :returns: :class:`Query`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ListQueryObjectsResponseQuery]

        Gets a list of queries accessible to the user, ordered by creation time. **Warning:** Calling this API
        concurrently 10 or more times could result in throttling, service degradation, or a temporary ban.

        :param page_size: int (optional)
          Maximum number of queries to return per page. Values above 100 are coerced to 100.
        :param page_token: str (optional)
          Token from the ``next_page_token`` of a previous response. Omit it to fetch the first page.

        :returns: Iterator over :class:`ListQueryObjectsResponseQuery`
        

    .. py:method:: list_visualizations(id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Visualization]

        Gets a list of visualizations on a query.

        :param id: str
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Visualization`
        

    .. py:method:: update(id: str, update_mask: str [, auto_resolve_display_name: Optional[bool], query: Optional[UpdateQueryRequestQuery]]) -> Query


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import sql
            
            w = WorkspaceClient()
            
            srcs = w.data_sources.list()
            
            query = w.queries.create(
                query=sql.CreateQueryRequestQuery(
                    display_name=f"sdk-{time.time_ns()}",
                    warehouse_id=srcs[0].warehouse_id,
                    description="test query from Go SDK",
                    query_text="SHOW TABLES",
                )
            )
            
            updated = w.queries.update(
                id=query.id,
                query=sql.UpdateQueryRequestQuery(
                    display_name=f"sdk-{time.time_ns()}",
                    description="UPDATED: test query from Go SDK",
                    query_text="SELECT 2+2",
                ),
                update_mask="display_name,description,query_text",
            )
            
            # cleanup
            w.queries.delete(id=query.id)

        Updates the fields of a query named in ``update_mask``. Changing ``owner_user_name`` requires
        workspace admin privileges. Changing ``run_as_mode`` requires CAN MANAGE permission on the query, and
        only the query owner can switch it to ``OWNER``.

        :param id: str
          UUID of the query to update.
        :param update_mask: str
          Comma-separated list of the query fields to update, such as the display name or query text. Fields
          not listed keep their current values.

          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param auto_resolve_display_name: bool (optional)
          If true, automatically resolve query display name conflicts. Otherwise, fail the request if the
          query's display name conflicts with an existing query's display name.
        :param query: :class:`UpdateQueryRequestQuery` (optional)
          Query fields to update. Only the fields named in ``update_mask`` are changed.

        :returns: :class:`Query`
        