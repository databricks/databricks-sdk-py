``w.settings.restrict_workspace_admins``: Restrict Workspace Admins
===================================================================
.. currentmodule:: databricks.sdk.service.settings

.. py:class:: RestrictWorkspaceAdminsAPI

    The Restrict Workspace Admins setting lets you control the capabilities of workspace admins. With the
    setting status set to ALLOW_ALL, workspace admins can create service principal personal access tokens on
    behalf of any service principal in their workspace. Workspace admins can also change a job owner to any
    user in their workspace. And they can change the job run_as setting to any user in their workspace or to a
    service principal on which they have the Service Principal User role. With the setting status set to
    RESTRICT_TOKENS_AND_JOB_RUN_AS, workspace admins can only create personal access tokens on behalf of
    service principals they have the Service Principal User role on. They can also only change a job owner to
    themselves. And they can change the job run_as setting to themselves or to a service principal on which
    they have the Service Principal User role.

    .. py:method:: delete( [, etag: Optional[str]]) -> DeleteRestrictWorkspaceAdminsSettingResponse

        Delete the restrict workspace admins setting.
        
        Reverts the restrict workspace admins setting status for the workspace. A fresh etag needs to be
        provided in `DELETE` requests (as a query parameter). The etag can be retrieved by making a `GET`
        request before the DELETE request. If the setting is updated/deleted concurrently, `DELETE` fails with
        409 and the request must be retried by using the fresh etag in the 409 response.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`DeleteRestrictWorkspaceAdminsSettingResponse`
        

    .. py:method:: get( [, etag: Optional[str]]) -> RestrictWorkspaceAdminsSetting

        Get the restrict workspace admins setting.
        
        Gets the restrict workspace admins setting.
        
        :param etag: str (optional)
          etag used for versioning. The response is at least as fresh as the eTag provided. This is used for
          optimistic concurrency control as a way to help prevent simultaneous writes of a setting overwriting
          each other. It is strongly suggested that systems make use of the etag in the read -> delete pattern
          to perform setting deletions in order to avoid race conditions. That is, get an etag from a GET
          request, and pass it with the DELETE request to identify the rule set version you are deleting.
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        

    .. py:method:: update(allow_missing: bool, setting: RestrictWorkspaceAdminsSetting, field_mask: str) -> RestrictWorkspaceAdminsSetting

        Update the restrict workspace admins setting.
        
        Updates the restrict workspace admins setting for the workspace. A fresh etag needs to be provided in
        `PATCH` requests (as part of the setting field). The etag can be retrieved by making a GET request
        before the `PATCH` request. If the setting is updated concurrently, `PATCH` fails with 409 and the
        request must be retried by using the fresh etag in the 409 response.
        
        :param allow_missing: bool
          This should always be set to true for Settings API. Added for AIP compliance.
        :param setting: :class:`RestrictWorkspaceAdminsSetting`
        :param field_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.
          
          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.
        
        :returns: :class:`RestrictWorkspaceAdminsSetting`
        