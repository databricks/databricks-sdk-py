``w.serverless_compute_service``: ServerlessCompute Service
===========================================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: ServerlessComputeServiceAPI

    ServerlessCompute Service API.

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
        