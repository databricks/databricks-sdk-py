``w.service_principals``: Service Principals
============================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: ServicePrincipalsAPI

    Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
    Databricks recommends creating service principals to run production jobs or modify production data. If all
    processes that act on production data run with service principals, interactive users do not need any
    write, delete, or modify privileges in production. This eliminates the risk of a user overwriting
    production data by accident.

    .. py:method:: create( [, active: Optional[bool], application_id: Optional[str], display_name: Optional[str], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], id: Optional[str], roles: Optional[List[ComplexValue]], schemas: Optional[List[ServicePrincipalSchema]]]) -> ServicePrincipal


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())
            
            spn = w.service_principals.create(display_name=f'sdk-{time.time_ns()}',
                                              groups=[iam.ComplexValue(value=groups["admins"])])
            
            # cleanup
            w.service_principals.delete(id=spn.id)

        Create a service principal.
        
        Creates a new service principal in the Databricks workspace.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        :returns: :class:`ServicePrincipal`
        

    .. py:method:: delete(id: str)

        Delete a service principal.
        
        Delete a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        
        

    .. py:method:: get(id: str) -> ServicePrincipal


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')
            
            by_id = w.service_principals.get(id=created.id)
            
            # cleanup
            w.service_principals.delete(id=created.id)

        Get service principal details.
        
        Gets the details for a single service principal define in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        
        :returns: :class:`ServicePrincipal`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[ServicePrincipal]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            all = w.service_principals.list(iam.ListServicePrincipalsRequest())

        List service principals.
        
        Gets the set of service principals associated with a Databricks workspace.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page.
        :param excluded_attributes: str (optional)
          Comma-separated list of attributes to exclude in response.
        :param filter: str (optional)
          Query by which the results have to be filtered. Supported operators are equals(`eq`),
          contains(`co`), starts with(`sw`) and not equals(`ne`). Additionally, simple expressions can be
          formed using logical operators - `and` and `or`. The [SCIM RFC] has more details but we currently
          only support simple expressions.
          
          [SCIM RFC]: https://tools.ietf.org/html/rfc7644#section-3.4.2.2
        :param sort_by: str (optional)
          Attribute to sort the results.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.
        
        :returns: Iterator over :class:`ServicePrincipal`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')
            
            by_id = w.service_principals.get(id=created.id)
            
            w.service_principals.patch(id=by_id.id,
                                       operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                                       schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])
            
            # cleanup
            w.service_principals.delete(id=created.id)

        Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks workspace.
        
        :param id: str
          Unique ID for a service principal in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        

    .. py:method:: update(id: str [, active: Optional[bool], application_id: Optional[str], display_name: Optional[str], entitlements: Optional[List[ComplexValue]], external_id: Optional[str], groups: Optional[List[ComplexValue]], roles: Optional[List[ComplexValue]], schemas: Optional[List[ServicePrincipalSchema]]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import iam
            
            w = WorkspaceClient()
            
            created = w.service_principals.create(display_name=f'sdk-{time.time_ns()}')
            
            w.service_principals.update(id=created.id,
                                        display_name=f'sdk-{time.time_ns()}',
                                        roles=[iam.ComplexValue(value="xyz")])
            
            # cleanup
            w.service_principals.delete(id=created.id)

        Replace service principal.
        
        Updates the details of a single service principal.
        
        This action replaces the existing service principal with the same name.
        
        :param id: str
          Databricks service principal ID.
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
          Entitlements assigned to the service principal. See [assigning entitlements] for a full list of
          supported values.
          
          [assigning entitlements]: https://docs.databricks.com/administration-guide/users-groups/index.html#assigning-entitlements
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        
        