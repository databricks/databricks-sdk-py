``w.rfa``: Request for Access
=============================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: RfaAPI

    Request for Access enables users to request access for Unity Catalog securables.

    These APIs provide a standardized way for securable owners (or users with MANAGE privileges) to manage
    access request destinations.

    .. py:method:: batch_create_access_requests( [, requests: Optional[List[CreateAccessRequest]]]) -> BatchCreateAccessRequestsResponse

        Creates access requests for Unity Catalog permissions for a specified principal on a securable object.
        This Batch API can take in multiple principals, securable objects, and permissions as the input and
        returns the access request destinations for each. Principals must be unique across the API call.

        The supported securable types are: "metastore", "catalog", "schema", "table", "external_location",
        "connection", "credential", "function", "registered_model", and "volume".

        :param requests: List[:class:`CreateAccessRequest`] (optional)
          A list of individual access requests, where each request corresponds to a set of permissions being
          requested on a list of securables for a specified principal.

          At most 30 requests per API call.

        :returns: :class:`BatchCreateAccessRequestsResponse`
        

    .. py:method:: get_access_request_destinations(securable_type: str, full_name: str) -> AccessRequestDestinations

        Gets an array of access request destinations for the specified securable. Any caller can see URL
        destinations or the destinations on the metastore. Otherwise, only those with **BROWSE** permissions
        on the securable can see destinations.

        The supported securable types are: "metastore", "catalog", "schema", "table", "external_location",
        "connection", "credential", "function", "registered_model", and "volume".

        :param securable_type: str
          The type of the securable.
        :param full_name: str
          The full name of the securable.

        :returns: :class:`AccessRequestDestinations`
        

    .. py:method:: update_access_request_destinations(access_request_destinations: AccessRequestDestinations, update_mask: str) -> AccessRequestDestinations

        Updates the access request destinations for the given securable. The caller must be a metastore admin,
        the owner of the securable, or a user that has the **MANAGE** privilege on the securable in order to
        assign destinations. Destinations cannot be updated for securables underneath schemas (tables,
        volumes, functions, and models). For these securable types, destinations are inherited from the parent
        securable. A maximum of 5 emails and 5 external notification destinations (Slack, Microsoft Teams, and
        Generic Webhook destinations) can be assigned to a securable. If a URL destination is assigned, no
        other destinations can be set.

        The supported securable types are: "metastore", "catalog", "schema", "table", "external_location",
        "connection", "credential", "function", "registered_model", and "volume".

        :param access_request_destinations: :class:`AccessRequestDestinations`
          The access request destinations to assign to the securable. For each destination, a
          **destination_id** and **destination_type** must be defined.
        :param update_mask: str
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`AccessRequestDestinations`
        