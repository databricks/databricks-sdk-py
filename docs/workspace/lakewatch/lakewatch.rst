``w.lakewatch``: Lakewatch.v1
=============================
.. currentmodule:: databricks.sdk.service.lakewatch

.. py:class:: LakewatchAPI

    Manage Lakewatch: security-analytics data sources, detection rules, and per-catalog configuration.

    .. py:method:: create_datasource(datasource: Datasource) -> Datasource

        Creates a new datasource.

        :param datasource: :class:`Datasource`

        :returns: :class:`Datasource`
        

    .. py:method:: create_rule(rule: Rule) -> Rule

        Creates a new rule.

        :param rule: :class:`Rule`
          The rule to create. Server-assigned fields (``name``, ``rule_id``, timestamps, ``etag``, …) are
          ignored on the request.

        :returns: :class:`Rule`
        

    .. py:method:: delete_datasource(name: str)

        Deletes a datasource by its resource name.

        :param name: str


        

    .. py:method:: delete_rule(name: str)

        Deletes a rule by its resource name.

        :param name: str
          Resource name of the rule to delete. Format: ``rules/{rule_id}``.


        

    .. py:method:: get_alert_config(name: str) -> AlertConfig

        Returns the alert delivery configuration for a catalog.

        :param name: str

        :returns: :class:`AlertConfig`
        

    .. py:method:: get_common_config(name: str) -> CommonConfig

        Returns the common Lakewatch configuration for a catalog.

        :param name: str

        :returns: :class:`CommonConfig`
        

    .. py:method:: get_datasource(name: str) -> Datasource

        Returns a single datasource by its resource name.

        :param name: str

        :returns: :class:`Datasource`
        

    .. py:method:: get_datasource_config(name: str) -> DatasourceConfig

        Returns the datasource ingestion configuration for a catalog.

        :param name: str

        :returns: :class:`DatasourceConfig`
        

    .. py:method:: get_rule(name: str) -> Rule

        Returns a single rule by its resource name.

        :param name: str
          Full resource name of the detection rule, in the form ``rules/{rule_id}``.

        :returns: :class:`Rule`
        

    .. py:method:: get_rule_config(name: str) -> RuleConfig

        Returns the detection-rule configuration for a catalog.

        :param name: str

        :returns: :class:`RuleConfig`
        

    .. py:method:: list_datasources(catalog_name: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], schema_name: Optional[str], view: Optional[DatasourceView]]) -> Iterator[Datasource]

        Lists the datasources in a Unity Catalog catalog, optionally narrowed to one schema or filtered by
        name. Results are paginated. Datasources that are still being created or deleted are not listed.

        :param catalog_name: str
          Name of the Unity Catalog catalog to list datasources from. Required; each request lists the
          datasources of a single catalog.
        :param filter: str (optional)
          Filter expression that restricts the results to datasources with a given name, for example
          ``datasource_name = "my_source"``. Only a single exact-match comparison on ``datasource_name`` is
          supported, and it matches the datasource's current Unity Catalog name, which reads report in
          ``effective_datasource_name``. Filtered results are returned in a single page.
        :param page_size: int (optional)
          Maximum number of results to return in one page. This is a best-effort upper bound, not a guarantee:
          the server may return fewer items than requested (even zero) while more results still exist. If
          unset or 0, the server picks a default.
        :param page_token: str (optional)
        :param schema_name: str (optional)
          Name of a Unity Catalog schema in ``catalog_name``. Optional; if set, only the datasources in this
          schema are returned, and if omitted, the datasources in all schemas of the catalog are returned.
        :param view: :class:`DatasourceView` (optional)
          Which fields to return for each datasource. Defaults to ``DATASOURCE_VIEW_FULL``.
          ``DATASOURCE_VIEW_BASIC`` returns only the identity and Unity Catalog location fields.

        :returns: Iterator over :class:`Datasource`
        

    .. py:method:: list_rules(catalog_name: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str], schema_name: Optional[str], view: Optional[RuleView]]) -> Iterator[Rule]

        Lists rules, with optional filtering and pagination.

        :param catalog_name: str
          Name of the Unity Catalog catalog to list rules from. Required.
        :param filter: str (optional)
          Filter expression that restricts the results, such as ``rule_name = "my_rule"`` to return only the
          rule with that name. The name is matched against the current UC name, which reads report in
          ``effective_rule_name``.
        :param page_size: int (optional)
          Maximum number of rules to return. The server may return fewer. If unset or 0, the server picks a
          default page size.
        :param page_token: str (optional)
          Page token from a previous ``ListRules`` response, used to fetch the next page of results.
        :param schema_name: str (optional)
          Name of a Unity Catalog schema in ``catalog_name``. If set, only rules in this schema are returned.
          If unset, rules in all schemas of the catalog are returned.
        :param view: :class:`RuleView` (optional)
          How much of each rule to return. Defaults to ``RULE_VIEW_FULL``. ``RULE_VIEW_BASIC`` returns only
          each rule's identity and Unity Catalog location.

        :returns: Iterator over :class:`Rule`
        

    .. py:method:: update_alert_config(name: str, alert_config: AlertConfig, update_mask: FieldMask [, etag: Optional[str]]) -> AlertConfig

        Updates the alert delivery configuration for a catalog.

        :param name: str
        :param alert_config: :class:`AlertConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`AlertConfig`
        

    .. py:method:: update_common_config(name: str, common_config: CommonConfig, update_mask: FieldMask [, etag: Optional[str]]) -> CommonConfig

        Updates the common Lakewatch configuration for a catalog.

        :param name: str
        :param common_config: :class:`CommonConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`CommonConfig`
        

    .. py:method:: update_datasource(name: str, datasource: Datasource, update_mask: FieldMask [, etag: Optional[str]]) -> Datasource

        Updates an existing datasource.

        :param name: str
          Resource name of the datasource, in the format ``datasources/{datasource_id}``. Unlike the
          datasource's Unity Catalog location (``catalog_name``, ``schema_name``, and ``datasource_name``),
          the name does not change when the datasource or its catalog or schema is renamed in Unity Catalog.
        :param datasource: :class:`Datasource`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set to a non-empty value that does not match the resource's
          current ``etag``, the update is rejected as a conflict (HTTP 409). Omit this field or send an empty
          string to update unconditionally.

        :returns: :class:`Datasource`
        

    .. py:method:: update_datasource_config(name: str, datasource_config: DatasourceConfig, update_mask: FieldMask [, etag: Optional[str]]) -> DatasourceConfig

        Updates the datasource ingestion configuration for a catalog.

        :param name: str
        :param datasource_config: :class:`DatasourceConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`DatasourceConfig`
        

    .. py:method:: update_rule(name: str, rule: Rule, update_mask: FieldMask [, etag: Optional[str]]) -> Rule

        Updates an existing rule.

        :param name: str
          Resource name, in the form ``rules/{rule_id}``. Assigned by the server on create; required on
          update.
        :param rule: :class:`Rule`
          The rule with its new field values. ``rule.name`` identifies the rule to update.
        :param update_mask: FieldMask
          The set of fields to update. Only fields named in the mask are modified.
        :param etag: str (optional)
          Optimistic-concurrency token from the latest read. A non-empty token that does not match the current
          ``etag`` rejects the update as a conflict (HTTP 409). Omit this field or provide an empty string to
          update unconditionally.

        :returns: :class:`Rule`
        

    .. py:method:: update_rule_config(name: str, rule_config: RuleConfig, update_mask: FieldMask [, etag: Optional[str]]) -> RuleConfig

        Updates the detection-rule configuration for a catalog.

        :param name: str
        :param rule_config: :class:`RuleConfig`
        :param update_mask: FieldMask
          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g.,
          ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the
          API changes in the future.
        :param etag: str (optional)
          Optimistic-concurrency precondition: if set and it does not match the resource's current ``etag``,
          the update is rejected as a conflict (HTTP 409).

        :returns: :class:`RuleConfig`
        