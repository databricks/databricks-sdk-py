``w.tag_policies``: Tag Policies
================================
.. currentmodule:: databricks.sdk.service.tags

.. py:class:: TagPoliciesAPI

    The Tag Policy API allows you to manage policies for governed tags in Databricks. For Terraform usage, see
    the [Tag Policy Terraform documentation]. Permissions for tag policies can be managed using the [Account
    Access Control Proxy API].

    [Account Access Control Proxy API]: https://docs.databricks.com/api/workspace/accountaccesscontrolproxy
    [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/tag_policy
    

    .. py:method:: create_tag_policy(tag_policy: TagPolicy) -> TagPolicy

        Creates a new tag policy, making the associated tag key governed. For Terraform usage, see the [Tag
        Policy Terraform documentation]. To manage permissions for tag policies, use the [Account Access
        Control Proxy API].

        [Account Access Control Proxy API]: https://docs.databricks.com/api/workspace/accountaccesscontrolproxy
        [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/tag_policy

        :param tag_policy: :class:`TagPolicy`

        :returns: :class:`TagPolicy`
        

    .. py:method:: delete_tag_policy(tag_key: str)

        Deletes a tag policy by its associated governed tag's key, leaving that tag key ungoverned. For
        Terraform usage, see the [Tag Policy Terraform documentation].

        [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/tag_policy

        :param tag_key: str


        

    .. py:method:: get_tag_policy(tag_key: str) -> TagPolicy

        Gets a single tag policy by its associated governed tag's key. For Terraform usage, see the [Tag
        Policy Terraform documentation]. To list granted permissions for tag policies, use the [Account Access
        Control Proxy API].

        [Account Access Control Proxy API]: https://docs.databricks.com/api/workspace/accountaccesscontrolproxy
        [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/tag_policy

        :param tag_key: str

        :returns: :class:`TagPolicy`
        

    .. py:method:: list_tag_policies( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[TagPolicy]

        Lists the tag policies for all governed tags in the account. For Terraform usage, see the [Tag Policy
        Terraform documentation]. To list granted permissions for tag policies, use the [Account Access
        Control Proxy API].

        [Account Access Control Proxy API]: https://docs.databricks.com/api/workspace/accountaccesscontrolproxy
        [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/tag_policies

        :param page_size: int (optional)
          The maximum number of results to return in this request. Fewer results may be returned than
          requested. If unspecified or set to 0, this defaults to 1000. The maximum value is 1000; values
          above 1000 will be coerced down to 1000.
        :param page_token: str (optional)
          An optional page token received from a previous list tag policies call.

        :returns: Iterator over :class:`TagPolicy`
        

    .. py:method:: update_tag_policy(tag_key: str, tag_policy: TagPolicy, update_mask: str) -> TagPolicy

        Updates an existing tag policy for a single governed tag. For Terraform usage, see the [Tag Policy
        Terraform documentation]. To manage permissions for tag policies, use the [Account Access Control
        Proxy API].

        [Account Access Control Proxy API]: https://docs.databricks.com/api/workspace/accountaccesscontrolproxy
        [Tag Policy Terraform documentation]: https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/tag_policy

        :param tag_key: str
        :param tag_policy: :class:`TagPolicy`
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`TagPolicy`
        