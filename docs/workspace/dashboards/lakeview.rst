``w.lakeview``: Lakeview
========================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: LakeviewAPI

    These APIs provide specific management operations for Lakeview dashboards. Generic resource management can
    be done with Workspace API (import, export, get-status, list, delete).

    .. py:method:: create(display_name: str [, parent_path: Optional[str], serialized_dashboard: Optional[str], warehouse_id: Optional[str]]) -> Dashboard

        Create dashboard.
        
        Create a draft dashboard.
        
        :param display_name: str
          The display name of the dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder containing the dashboard. Includes leading slash and no trailing
          slash.
        :param serialized_dashboard: str (optional)
          The contents of the dashboard in serialized string form.
        :param warehouse_id: str (optional)
          The warehouse ID used to run the dashboard.
        
        :returns: :class:`Dashboard`
        

    .. py:method:: get(dashboard_id: str) -> Dashboard

        Get dashboard.
        
        Get a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        :returns: :class:`Dashboard`
        

    .. py:method:: get_published(dashboard_id: str) -> PublishedDashboard

        Get published dashboard.
        
        Get the current published dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        :returns: :class:`PublishedDashboard`
        

    .. py:method:: migrate(source_dashboard_id: str [, display_name: Optional[str], parent_path: Optional[str]]) -> Dashboard

        Migrate dashboard.
        
        Migrates a classic SQL dashboard to Lakeview.
        
        :param source_dashboard_id: str
          UUID of the dashboard to be migrated.
        :param display_name: str (optional)
          Display name for the new Lakeview dashboard.
        :param parent_path: str (optional)
          The workspace path of the folder to contain the migrated Lakeview dashboard.
        
        :returns: :class:`Dashboard`
        

    .. py:method:: publish(dashboard_id: str [, embed_credentials: Optional[bool], warehouse_id: Optional[str]]) -> PublishedDashboard

        Publish dashboard.
        
        Publish the current draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        :param embed_credentials: bool (optional)
          Flag to indicate if the publisher's credentials should be embedded in the published dashboard. These
          embedded credentials will be used to execute the published dashboard's queries.
        :param warehouse_id: str (optional)
          The ID of the warehouse that can be used to override the warehouse which was set in the draft.
        
        :returns: :class:`PublishedDashboard`
        

    .. py:method:: trash(dashboard_id: str)

        Trash dashboard.
        
        Trash a dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        
        
        

    .. py:method:: unpublish(dashboard_id: str)

        Unpublish dashboard.
        
        Unpublish the dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard to be published.
        
        
        

    .. py:method:: update(dashboard_id: str [, display_name: Optional[str], etag: Optional[str], serialized_dashboard: Optional[str], warehouse_id: Optional[str]]) -> Dashboard

        Update dashboard.
        
        Update a draft dashboard.
        
        :param dashboard_id: str
          UUID identifying the dashboard.
        :param display_name: str (optional)
          The display name of the dashboard.
        :param etag: str (optional)
          The etag for the dashboard. Can be optionally provided on updates to ensure that the dashboard has
          not been modified since the last read.
        :param serialized_dashboard: str (optional)
          The contents of the dashboard in serialized string form.
        :param warehouse_id: str (optional)
          The warehouse ID used to run the dashboard.
        
        :returns: :class:`Dashboard`
        