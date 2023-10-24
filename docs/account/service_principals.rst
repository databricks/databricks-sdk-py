Account Service Principals
==========================
.. py:class:: AccountServicePrincipalsAPI

    Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
    Databricks recommends creating service principals to run production jobs or modify production data. If all
    processes that act on production data run with service principals, interactive users do not need any
    write, delete, or modify privileges in production. This eliminates the risk of a user overwriting
    production data by accident.

    .. py:method:: create( [, active, application_id, display_name, entitlements, external_id, groups, id, roles, schemas])

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
        
        Creates a new service principal in the Databricks account.
        
        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param entitlements: List[:class:`ComplexValue`] (optional)
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        :returns: :class:`ServicePrincipal`
        

    .. py:method:: delete(id)

        Delete a service principal.
        
        Delete a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        
        

    .. py:method:: get(id)

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
        
        Gets the details for a single service principal define in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        
        :returns: :class:`ServicePrincipal`
        

    .. py:method:: list( [, attributes, count, excluded_attributes, filter, sort_by, sort_order, start_index])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')
            
            sp = a.service_principals.get(id=sp_create.id)
            
            sp_list = a.service_principals.list(filter="displayName eq %v" % (sp.display_name))
            
            # cleanup
            a.service_principals.delete(id=sp_create.id)

        List service principals.
        
        Gets the set of service principals associated with a Databricks account.
        
        :param attributes: str (optional)
          Comma-separated list of attributes to return in response.
        :param count: int (optional)
          Desired number of results per page. Default is 10000.
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
        

    .. py:method:: patch(id [, operations, schemas])

        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import iam
            
            a = AccountClient()
            
            sp_create = a.service_principals.create(active=True, display_name=f'sdk-{time.time_ns()}')
            
            sp = a.service_principals.get(id=sp_create.id)
            
            a.service_principals.patch(id=sp.id,
                                       operations=[iam.Patch(op=iam.PatchOp.REPLACE, path="active", value="false")],
                                       schemas=[iam.PatchSchema.URN_IETF_PARAMS_SCIM_API_MESSAGES_2_0_PATCH_OP])
            
            # cleanup
            a.service_principals.delete(id=sp_create.id)

        Update service principal details.
        
        Partially updates the details of a single service principal in the Databricks account.
        
        :param id: str
          Unique ID for a service principal in the Databricks account.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].
        
        
        

    .. py:method:: update(id [, active, application_id, display_name, entitlements, external_id, groups, roles, schemas])

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
        :param external_id: str (optional)
        :param groups: List[:class:`ComplexValue`] (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Corresponds to AWS instance profile/arn role.
        :param schemas: List[:class:`ServicePrincipalSchema`] (optional)
          The schema of the List response.
        
        
        