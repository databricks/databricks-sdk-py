``w.policies``: ABAC Policies
=============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: PoliciesAPI

    Attribute-Based Access Control (ABAC) provides high leverage governance for enforcing compliance policies
    in Unity Catalog. With ABAC policies, access is controlled in a hierarchical and scalable manner, based on
    data attributes rather than specific resources, enabling more flexible and comprehensive access control.
    ABAC policies in Unity Catalog support conditions on securable properties, governance tags, and
    environment contexts. Callers must have the `MANAGE` privilege on a securable to view, create, update, or
    delete ABAC policies.

    .. py:method:: create_policy(policy_info: PolicyInfo) -> PolicyInfo

        Creates a new policy on a securable. The new policy applies to the securable and all its descendants.
        
        :param policy_info: :class:`PolicyInfo`
          Required. The policy to create.
        
        :returns: :class:`PolicyInfo`
        

    .. py:method:: delete_policy(on_securable_type: str, on_securable_fullname: str, name: str) -> DeletePolicyResponse

        Delete an ABAC policy defined on a securable.
        
        :param on_securable_type: str
          Required. The type of the securable to delete the policy from.
        :param on_securable_fullname: str
          Required. The fully qualified name of the securable to delete the policy from.
        :param name: str
          Required. The name of the policy to delete
        
        :returns: :class:`DeletePolicyResponse`
        

    .. py:method:: get_policy(on_securable_type: str, on_securable_fullname: str, name: str) -> PolicyInfo

        Get the policy definition on a securable
        
        :param on_securable_type: str
          Required. The type of the securable to retrieve the policy for.
        :param on_securable_fullname: str
          Required. The fully qualified name of securable to retrieve policy for.
        :param name: str
          Required. The name of the policy to retrieve.
        
        :returns: :class:`PolicyInfo`
        

    .. py:method:: list_policies(on_securable_type: str, on_securable_fullname: str [, include_inherited: Optional[bool], max_results: Optional[int], page_token: Optional[str]]) -> Iterator[PolicyInfo]

        List all policies defined on a securable. Optionally, the list can include inherited policies defined
        on the securable's parent schema or catalog.
        
        :param on_securable_type: str
          Required. The type of the securable to list policies for.
        :param on_securable_fullname: str
          Required. The fully qualified name of securable to list policies for.
        :param include_inherited: bool (optional)
          Optional. Whether to include policies defined on parent securables. By default, the inherited
          policies are not included.
        :param max_results: int (optional)
          Optional. Maximum number of policies to return on a single page (page length). - When not set or set
          to 0, the page length is set to a server configured value (recommended); - When set to a value
          greater than 0, the page length is the minimum of this value and a server configured value;
        :param page_token: str (optional)
          Optional. Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`PolicyInfo`
        

    .. py:method:: update_policy(on_securable_type: str, on_securable_fullname: str, name: str, policy_info: PolicyInfo [, update_mask: Optional[str]]) -> PolicyInfo

        Update an ABAC policy on a securable.
        
        :param on_securable_type: str
          Required. The type of the securable to update the policy for.
        :param on_securable_fullname: str
          Required. The fully qualified name of the securable to update the policy for.
        :param name: str
          Required. The name of the policy to update.
        :param policy_info: :class:`PolicyInfo`
          Optional fields to update. This is the request body for updating a policy. Use `update_mask` field
          to specify which fields in the request is to be updated. - If `update_mask` is empty or "*", all
          specified fields will be updated. - If `update_mask` is specified, only the fields specified in the
          `update_mask` will be updated. If a field is specified in `update_mask` and not set in the request,
          the field will be cleared. Users can use the update mask to explicitly unset optional fields such as
          `exception_principals` and `when_condition`.
        :param update_mask: str (optional)
          Optional. The update mask field for specifying user intentions on which fields to update in the
          request.
        
        :returns: :class:`PolicyInfo`
        