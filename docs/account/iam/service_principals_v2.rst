``a.service_principals_v2``: Account Service Principals
=======================================================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AccountServicePrincipalsV2API

    Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
    Databricks recommends creating service principals to run production jobs or modify production data. If all
    processes that act on production data run with service principals, interactive users do not need any
    write, delete, or modify privileges in production. This eliminates the risk of a user overwriting
    production data by accident.

    .. py:method:: create( [, active: Optional[bool], application_id: Optional[str], display_name: Optional[str], external_id: Optional[str], id: Optional[str], roles: Optional[List[ComplexValue]]]) -> AccountServicePrincipal

        Creates a new service principal in the Databricks account.

        :param active: bool (optional)
          If this user is active
        :param application_id: str (optional)
          UUID relating to the service principal
        :param display_name: str (optional)
          String that represents a concatenation of given and family names.
        :param external_id: str (optional)
        :param id: str (optional)
          Databricks service principal ID.
        :param roles: List[:class:`ComplexValue`] (optional)
          Indicates if the group has the admin role.

        :returns: :class:`AccountServicePrincipal`
        

    .. py:method:: delete(id: str)

        Delete a single service principal in the Databricks account.

        :param id: str
          Unique ID for a service principal in the Databricks account.


        

    .. py:method:: get(id: str) -> AccountServicePrincipal

        Gets the details for a single service principal define in the Databricks account.

        :param id: str
          Unique ID for a service principal in the Databricks account.

        :returns: :class:`AccountServicePrincipal`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[AccountServicePrincipal]

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

        :returns: Iterator over :class:`AccountServicePrincipal`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])

        Partially updates the details of a single service principal in the Databricks account.

        :param id: str
          Unique ID in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].


        

    .. py:method:: update(id: str [, active: Optional[bool], application_id: Optional[str], display_name: Optional[str], external_id: Optional[str], roles: Optional[List[ComplexValue]]])

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
        :param external_id: str (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Indicates if the group has the admin role.


        