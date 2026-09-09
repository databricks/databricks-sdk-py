``w.domains``: Domains.v1
=========================
.. currentmodule:: databricks.sdk.service.domains

.. py:class:: DomainsAPI

    Manage domains for organizing and discovering data assets.

    .. py:method:: create_domain(domain: Domain [, domain_id: Optional[str]]) -> Domain

        Create a domain. If ``domain_id`` is omitted, the server generates one.

        :param domain: :class:`Domain`
        :param domain_id: str (optional)
          Client-supplied resource ID for the new domain. If omitted, the server generates one.

        :returns: :class:`Domain`
        

    .. py:method:: delete_domain(name: str [, force: Optional[bool]])

        Delete a domain. By default the request fails if the domain still has Glossary pages; set ``force`` to
        delete those pages along with the domain.

        :param name: str
          Full resource name of the domain to delete. Format: ``domains/{domain_id}``
        :param force: bool (optional)
          When false (default), DeleteDomain is rejected with FAILED_PRECONDITION if the domain still has
          Glossary pages. When true, those pages are deleted first and then the domain is removed. Forwarded
          to the central service.


        

    .. py:method:: get_domain(name: str) -> Domain

        Get a domain by resource name.

        Authorization: external callers must have the ``MANAGE DISCOVERY`` permission.

        :param name: str
          Full resource name of the domain to retrieve. Format: ``domains/{domain_id}``

        :returns: :class:`Domain`
        

    .. py:method:: list_domains( [, page_size: Optional[int], page_token: Optional[str], parent_domain_id: Optional[str]]) -> Iterator[Domain]

        List domains in the account. Set ``parent_domain_id`` to return only the direct subdomains of a given
        domain.

        Authorization: external callers must have the ``MANAGE DISCOVERY`` permission; only domains the caller
        is authorized to read are returned.

        :param page_size: int (optional)
        :param page_token: str (optional)
        :param parent_domain_id: str (optional)
          Filter by parent domain.

          - Absent: return all domains regardless of hierarchy.
          - Present: return only direct children of the specified domain.

        :returns: Iterator over :class:`Domain`
        

    .. py:method:: update_domain(name: str, domain: Domain, update_mask: FieldMask) -> Domain

        Update a domain. ``update_mask`` selects which fields to modify; the domain is identified by its
        resource ``name``.

        :param name: str
          Full resource name of the domain. The primary identifier for this resource. Format:
          ``domains/{domain_id}`` Identifies the domain on get, update, and delete. Not an input on create —
          to choose the id, set ``CreateDomainRequest.domain_id``.
        :param domain: :class:`Domain`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.

        :returns: :class:`Domain`
        