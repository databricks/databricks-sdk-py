``w.settings.restrict_workspace_admins``: Restrict Workspace Admins
===================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: RestrictWorkspaceAdminsAPI

    The Restrict Workspace Admins setting lets you control the capabilities of workspace admins. With the
    setting status set to ALLOW_ALL, workspace admins can create service principal personal access tokens on
    behalf of any service principal in their workspace. Workspace admins can also change a job owner or the
    job run_as setting to any user in their workspace or a service principal on which they have the Service
    Principal User role. With the setting status set to RESTRICT_TOKENS_AND_JOB_RUN_AS, workspace admins can
    only create personal access tokens on behalf of service principals they have the Service Principal User
    role on. They can also only change a job owner or the job run_as setting to themselves or a service
    principal on which they have the Service Principal User role.

    .. py:method:: delete_restrict_workspace_admins_setting( [, etag: Optional[str]]) -> DeleteRestrictWorkspaceAdminsSettingResponse

        Delete the restrict workspace admins setting.
        
        Reverts the restrict workspace admins setting status for the workspace. A fresh etag needs to be
        provided in DELETE requests (as a query parameter). The etag can be retrieved by making a GET request
        before the DELETE request. If the setting is updated/deleted concurrently, DELETE will fail with 409
        and the request will need to be retried by using the fresh etag in the 409 response.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteRestrictWorkspaceAdminsSettingResponse`
        

    .. py:method:: get_restrict_workspace_admins_setting( [, etag: Optional[str]]) -> RestrictWorkspaceAdminsSetting

        Get the restrict workspace admins setting.
        
        Gets the restrict workspace admins setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        

    .. py:method:: update_restrict_workspace_admins_setting(allow_missing: bool, setting: RestrictWorkspaceAdminsSetting, field_mask: str) -> RestrictWorkspaceAdminsSetting

        Update the restrict workspace admins setting.
        
        Updates the restrict workspace admins setting for the workspace. A fresh etag needs to be provided in
        PATCH requests (as part of the setting field). The etag can be retrieved by making a GET request
        before the PATCH request. If the setting is updated concurrently, PATCH will fail with 409 and the
        request will need to be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`RestrictWorkspaceAdminsSetting`
        :param field_mask: str
          Field mask is required to be passed into the PATCH request. Field mask specifies which fields of the
          setting payload will be updated. The field mask needs to be supplied as single string. To specify
          multiple fields in the field mask, use comma as the separator (no space).
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        