``w.software_artifacts``: SoftwareArtifacts.v1
==============================================
.. currentmodule:: databricks.sdk.service.softwareartifacts

.. py:class:: SoftwareArtifactsAPI

    Manage software artifacts and their versions in Unity Catalog.

    .. py:method:: delete_software_artifact(name: str [, force: Optional[bool]])

        Deletes a software artifact. Fails if the artifact still has versions unless ``force`` is set.

        :param name: str
          Resource name of the software artifact, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param force: bool (optional)
          Force deletion even if the software artifact has versions, deleting them with it. Default is false.


        

    .. py:method:: delete_software_artifact_version(name: str)

        Deletes a software artifact version.

        :param name: str
          Resource name of the version, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}/versions/{version}``, where ``{version}`` is the
          version's content digest, for example ``sha256:<hex>``.


        

    .. py:method:: get_software_artifact(name: str) -> SoftwareArtifact

        Gets a software artifact by its resource name. Returns ``NOT_FOUND`` if the artifact does not exist.

        :param name: str
          Resource name of the artifact, of the form ``software-artifacts/{catalog}.{schema}.{artifact}``.

        :returns: :class:`SoftwareArtifact`
        

    .. py:method:: get_software_artifact_version(name: str) -> SoftwareArtifactVersion

        Gets a software artifact version by its resource name. Returns ``NOT_FOUND`` if the version does not
        exist.

        :param name: str
          Resource name of the version, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}/versions/{version}``, where ``{version}`` is the
          version's content digest.

        :returns: :class:`SoftwareArtifactVersion`
        

    .. py:method:: list_software_artifact_versions(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SoftwareArtifactVersion]

        Lists the versions of a software artifact.

        :param parent: str
          Resource name of the parent artifact, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param page_size: int (optional)
          Maximum number of versions to return. If omitted or set to 0, the page size defaults to 50. The
          maximum value is 50; values above 50 or below 0 are rejected.
        :param page_token: str (optional)
          Opaque continuation token from a previous response's next_page_token. Omit for the first page.

        :returns: Iterator over :class:`SoftwareArtifactVersion`
        

    .. py:method:: list_software_artifacts(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SoftwareArtifact]

        Lists software artifacts in a schema.

        :param parent: str
          Resource name of the parent schema, of the form ``schemas/{catalog}.{schema}``.
        :param page_size: int (optional)
          Maximum number of software artifacts to return. If omitted or set to 0, the page size defaults to
          50. The maximum value is 50; values above 50 or below 0 are rejected.
        :param page_token: str (optional)
          Opaque continuation token from a previous response's next_page_token. Omit for the first page.

        :returns: Iterator over :class:`SoftwareArtifact`
        

    .. py:method:: resolve_software_artifact_version(parent: str, alias: str) -> ResolveSoftwareArtifactVersionResponse

        Resolves a software artifact version from its tag alias. Returns ``NOT_FOUND`` if the artifact or the
        alias does not exist.

        :param parent: str
          Resource name of the software artifact containing the alias, of the form
          ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param alias: str
          Image tag alias selecting the version. The alias must be a valid OCI image tag of at most 128
          characters, made of letters, digits, underscores, periods, and hyphens, and must not start with a
          period or hyphen.

        :returns: :class:`ResolveSoftwareArtifactVersionResponse`
        

    .. py:method:: update_software_artifact(name: str, software_artifact: SoftwareArtifact, update_mask: FieldMask) -> SoftwareArtifact

        Updates a software artifact. The name is immutable; only the owner may be changed. The destination
        owner must exist in the account. The caller needs MANAGE_ACCESS_CONTROL on the artifact. The response
        contains its name and the requested owner; audit fields are omitted.

        :param name: str
          Resource name of the artifact, of the form ``software-artifacts/{catalog}.{schema}.{artifact}``.
        :param software_artifact: :class:`SoftwareArtifact`
          The software artifact to update. Its name identifies the existing artifact; only owner may be
          changed.
        :param update_mask: FieldMask
          Fields to update, relative to ``software_artifact``. Accepts ``owner`` or ``*``; owner is the only
          mutable field, so both select the same update. Output-only values in the resource are ignored.

        :returns: :class:`SoftwareArtifact`
        