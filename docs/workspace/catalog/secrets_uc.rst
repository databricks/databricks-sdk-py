``w.secrets_uc``: Secrets
=========================
.. currentmodule:: databricks.sdk.service.catalog

.. py:class:: SecretsUcAPI

    A secret is a Unity Catalog securable object that stores sensitive credential data (such as passwords,
    tokens, and keys) within a three-level namespace (**catalog_name.schema_name.secret_name**).

    Secrets can be managed using standard Unity Catalog permissions and are scoped to a schema within a
    catalog.

    .. py:method:: create_secret(secret: Secret) -> Secret

        Creates a new secret in Unity Catalog.

        You must be the owner of the parent schema or have the **CREATE_SECRET** and **USE SCHEMA** privileges
        on the parent schema and **USE CATALOG** on the parent catalog.

        The secret is stored in the specified catalog and schema, and the **value** field contains the
        sensitive data to be securely stored.

        :param secret: :class:`Secret`
          The secret object to create. The **name**, **catalog_name**, **schema_name**, and **value** fields
          are required.

        :returns: :class:`Secret`
        

    .. py:method:: delete_secret(full_name: str)

        Deletes a secret by its three-level (fully qualified) name.

        You must be the owner of the secret or a metastore admin.

        :param full_name: str
          The three-level (fully qualified) name of the secret (for example,
          **catalog_name.schema_name.secret_name**).


        

    .. py:method:: get_secret(full_name: str [, include_browse: Optional[bool]]) -> Secret

        Gets a secret by its three-level (fully qualified) name.

        You must be a metastore admin, the owner of the secret, or have the **MANAGE** privilege on the
        secret.

        The secret value isn't returned by default. To retrieve it, you must also have the **READ_SECRET**
        privilege and set **include_value** to true in the request.

        :param full_name: str
          The three-level (fully qualified) name of the secret (for example,
          **catalog_name.schema_name.secret_name**).
        :param include_browse: bool (optional)
          Whether to include secrets in the response for which you only have the **BROWSE** privilege, which
          limits access to metadata.

        :returns: :class:`Secret`
        

    .. py:method:: list_secrets( [, catalog_name: Optional[str], include_browse: Optional[bool], page_size: Optional[int], page_token: Optional[str], schema_name: Optional[str]]) -> Iterator[Secret]

        Lists secrets in Unity Catalog.

        You must be a metastore admin, the owner of the secret, or have the **MANAGE** privilege on the
        secret.

        Both **catalog_name** and **schema_name** must be specified together to filter secrets within a
        specific schema. Results are paginated; use the **page_token** field from the response to retrieve
        subsequent pages.

        :param catalog_name: str (optional)
          The name of the catalog under which to list secrets. Both **catalog_name** and **schema_name** must
          be specified together.
        :param include_browse: bool (optional)
          Whether to include secrets in the response for which you only have the **BROWSE** privilege, which
          limits access to metadata.
        :param page_size: int (optional)
          Maximum number of secrets to return.

          - If not specified, at most 10000 secrets are returned. - If set to a value greater than 0, the page
          length is the minimum of this value and 10000. - If set to 0, the page length is set to 10000. - If
          set to a value less than 0, an invalid parameter error is returned.
        :param page_token: str (optional)
          Opaque pagination token to go to the next page based on previous query. The maximum page length is
          determined by a server configured value.
        :param schema_name: str (optional)
          The name of the schema under which to list secrets. Both **catalog_name** and **schema_name** must
          be specified together.

        :returns: Iterator over :class:`Secret`
        

    .. py:method:: update_secret(full_name: str, secret: Secret, update_mask: FieldMask) -> Secret

        Updates an existing secret in Unity Catalog.

        You must be the owner of the secret or a metastore admin. If you are a metastore admin, only the
        **owner** field can be changed.

        Use the **update_mask** field to specify which fields to update. Supported updatable fields include
        **value**, **comment**, **owner**, and **expire_time**.

        :param full_name: str
          The three-level (fully qualified) name of the secret (for example,
          **catalog_name.schema_name.secret_name**).
        :param secret: :class:`Secret`
          The secret object containing the fields to update. Only fields specified in **update_mask** will be
          updated.
        :param update_mask: FieldMask
          The field mask specifying which fields of the secret to update. Supported fields: **value**,
          **comment**, **owner**, **expire_time**.

        :returns: :class:`Secret`
        