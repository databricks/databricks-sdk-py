``w.serverless_compute_service``: ServerlessCompute Service
===========================================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: ServerlessComputeServiceAPI

    ServerlessCompute Service API.

    .. py:method:: create_compute_policy(compute_policy: ComputePolicy) -> ComputePolicy

        Creates a custom compute policy in the workspace.

        :param compute_policy: :class:`ComputePolicy`
          The compute policy to create.

        :returns: :class:`ComputePolicy`
        

    .. py:method:: delete_compute_policy(compute_policy_id: str)

        Deletes a custom compute policy in the workspace. Default (system-provisioned) policies cannot be
        deleted.

        :param compute_policy_id: str
          The ID of the compute policy to delete.


        

    .. py:method:: get_compute_policy(compute_policy_id: str) -> ComputePolicy

        Retrieves a compute policy by its ID.

        :param compute_policy_id: str
          The ID of the compute policy to retrieve.

        :returns: :class:`ComputePolicy`
        

    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ServerlessCompute]

        Lists Interactive serverless computes that the caller can use or manage. Results are returned in an
        unspecified order.

        :param page_size: int (optional)
          Maximum number of computes to return per response. Unset or zero defaults to 100. The server caps
          requests above 150 to bound per-request RBAC fan-out.
        :param page_token: str (optional)
          Token for cursor-based pagination.

        :returns: Iterator over :class:`ServerlessCompute`
        

    .. py:method:: list_compute_policies( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ComputePolicy]

        Lists compute policies in the workspace. Results are returned in an unspecified order; callers should
        sort client-side if a specific order is needed.

        :param page_size: int (optional)
          Maximum number of policies to return per response. Unset or zero defaults to 100. The server caps
          requests above 150.
        :param page_token: str (optional)
          Token for cursor-based pagination.

        :returns: Iterator over :class:`ComputePolicy`
        

    .. py:method:: update_compute_policy(compute_policy_id: str, compute_policy: ComputePolicy, update_mask: FieldMask) -> ComputePolicy

        Updates a custom compute policy in the workspace. The display_name and allowed_compute_products are
        mutable; use update_mask to control which fields change. Default (system-provisioned) policies cannot
        be updated.

        :param compute_policy_id: str
          The unique identifier of the compute policy (UUID). Server-assigned on create.
        :param compute_policy: :class:`ComputePolicy`
          The compute policy to update. ``compute_policy.compute_policy_id`` identifies which policy to
          update; only the fields named in ``update_mask`` are applied.
        :param update_mask: FieldMask
          Fields to update, relative to ``compute_policy``. Must contain at least one path; the supported
          paths are ``display_name`` and ``allowed_compute_products``. Supplied product arms replace their
          constraints and omitted products remain unchanged. An empty arm clears that product's limits; an
          absent or empty products object is invalid. Removing a product requires its delete API. Nested masks
          and wildcards are unsupported. ``display_name`` cannot be cleared: if it is in the mask it must be
          non-empty.

        :returns: :class:`ComputePolicy`
        