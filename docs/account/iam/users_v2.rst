``a.users_v2``: Account Users
=============================
.. currentmodule:: databricks.sdk.service.iam

.. py:class:: AccountUsersV2API

    User identities recognized by Databricks and represented by email addresses.

    Databricks recommends using SCIM provisioning to sync users and groups automatically from your identity
    provider to your Databricks account. SCIM streamlines onboarding a new employee or team by using your
    identity provider to create users and groups in Databricks account and give them the proper level of
    access. When a user leaves your organization or no longer needs access to Databricks account, admins can
    terminate the user in your identity provider and that user’s account will also be removed from
    Databricks account. This ensures a consistent offboarding process and prevents unauthorized users from
    accessing sensitive data.

    .. py:method:: create( [, active: Optional[bool], display_name: Optional[str], emails: Optional[List[ComplexValue]], external_id: Optional[str], id: Optional[str], name: Optional[Name], roles: Optional[List[ComplexValue]], user_name: Optional[str]]) -> AccountUser

        Creates a new user in the Databricks account. This new user will also be added to the Databricks
        account.

        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param id: str (optional)
          Databricks user ID.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Indicates if the group has the admin role.
        :param user_name: str (optional)
          Email address of the Databricks user.

        :returns: :class:`AccountUser`
        

    .. py:method:: delete(id: str)

        Deletes a user. Deleting a user from a Databricks account also removes objects associated with the
        user.

        :param id: str
          Unique ID for a user in the Databricks account.


        

    .. py:method:: get(id: str [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[GetSortOrder], start_index: Optional[int]]) -> AccountUser

        Gets information for a specific user in Databricks account.

        :param id: str
          Unique ID for a user in the Databricks account.
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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`GetSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.

        :returns: :class:`AccountUser`
        

    .. py:method:: list( [, attributes: Optional[str], count: Optional[int], excluded_attributes: Optional[str], filter: Optional[str], sort_by: Optional[str], sort_order: Optional[ListSortOrder], start_index: Optional[int]]) -> Iterator[AccountUser]

        Gets details for all the users associated with a Databricks account.

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
          Attribute to sort the results. Multi-part paths are supported. For example, `userName`,
          `name.givenName`, and `emails`.
        :param sort_order: :class:`ListSortOrder` (optional)
          The order to sort the results.
        :param start_index: int (optional)
          Specifies the index of the first result. First item is number 1.

        :returns: Iterator over :class:`AccountUser`
        

    .. py:method:: patch(id: str [, operations: Optional[List[Patch]], schemas: Optional[List[PatchSchema]]])

        Partially updates a user resource by applying the supplied operations on specific user attributes.

        :param id: str
          Unique ID in the Databricks workspace.
        :param operations: List[:class:`Patch`] (optional)
        :param schemas: List[:class:`PatchSchema`] (optional)
          The schema of the patch request. Must be ["urn:ietf:params:scim:api:messages:2.0:PatchOp"].


        

    .. py:method:: update(id: str [, active: Optional[bool], display_name: Optional[str], emails: Optional[List[ComplexValue]], external_id: Optional[str], name: Optional[Name], roles: Optional[List[ComplexValue]], user_name: Optional[str]])

        Replaces a user's information with the data supplied in request.

        :param id: str
          Databricks user ID.
        :param active: bool (optional)
          If this user is active
        :param display_name: str (optional)
          String that represents a concatenation of given and family names. For example `John Smith`.
        :param emails: List[:class:`ComplexValue`] (optional)
          All the emails associated with the Databricks user.
        :param external_id: str (optional)
          External ID is not currently supported. It is reserved for future use.
        :param name: :class:`Name` (optional)
        :param roles: List[:class:`ComplexValue`] (optional)
          Indicates if the group has the admin role.
        :param user_name: str (optional)
          Email address of the Databricks user.


        