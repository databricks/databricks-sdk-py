``w.genie_migrate``: GenieMigrate.v1
====================================
.. currentmodule:: databricks.sdk.service.geniemigrate

.. py:class:: GenieMigrateAPI

    Use the Genie Migrate API to create and manage migration projects and the source files to convert.

    .. py:method:: add_files(name: str, sources: List[SourceFileRef]) -> AddProjectFilesResponse

        Adds source files to a migration project. Files that are already in the project are skipped and keep
        their conversion results.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param sources: List[:class:`SourceFileRef`]
          The files to add, each identified by ``workspace.path`` or ``workspace.object_id``. Send at most 500
          files per request. Duplicate files, and requests that exceed a file-count limit, return
          ``INVALID_PARAMETER_VALUE``. Files already in the project aren't overwritten. An empty list changes
          nothing.

        :returns: :class:`AddProjectFilesResponse`
        

    .. py:method:: cancel_operation(name: str)

        Requests cancellation of a long-running operation. Requires ``CAN_EDIT`` permission on the project.
        Cancellation is best effort: the operation can complete before cancellation takes effect. Call
        ``GetOperation`` to see its final state.

        :param name: str
          The name of the operation resource to be cancelled.


        

    .. py:method:: convert_project_files(parent: str [, names: Optional[List[str]], skill_paths: Optional[List[str]], start_over: Optional[bool]]) -> ConvertProjectFilesOperation

        Converts files of a migration project in a background job. Returns an operation; poll it with
        ``GetOperation``. The operation's metadata is the current ``ConversionRun``, with the run's state and
        the status of each file. When the run completes, the operation's response is a
        ``ConvertProjectFilesResponse``. A failed or cancelled run sets the operation's ``error`` instead.
        Files that fail to convert don't fail the run.

        To stop a conversion, call ``CancelOperation``. Cancellation is best effort, and the conversion can
        complete first. ``GetOperation`` reports the final outcome.

        :param parent: str
          The resource name of the project whose files to convert, in the format ``projects/{project_id}``.
          For example, ``projects/123``.
        :param names: List[str] (optional)
          The files to convert, in the format ``projects/{project_id}/files/{file_id}``. For example,
          ``projects/123/files/789``. All files must belong to ``parent``. At most 500 files; a workspace can
          set a lower limit, and requests over it return ``INVALID_PARAMETER_VALUE``.
        :param skill_paths: List[str] (optional)
          Custom skills that the conversion can use, as workspace paths of skill folders. Each folder must
          contain a ``SKILL.md`` file and be directly inside a skills folder: ``<home>/.assistant/skills``,
          ``/Workspace/.assistant/skills``, or another configured skills folder. At most 10 paths, which
          together must fit in 1000 bytes when encoded as a JSON array. Larger values return
          ``INVALID_PARAMETER_VALUE``. If empty, the conversion discovers skills automatically.
        :param start_over: bool (optional)
          Whether to convert each selected file from scratch instead of continuing from its previous results
          (changes, to-do items, blockers, and notes). Supported only for projects whose target framework is
          ``TARGET_FRAMEWORK_SQL``; other projects return ``INVALID_PARAMETER_VALUE``. Defaults to ``false``.

        :returns: :class:`Operation`
        

    .. py:method:: create(project: Project) -> Project

        Creates a migration project in a workspace folder. The server assigns the project ID. Add source files
        to the project with ``AddProjectFiles``.

        :param project: :class:`Project`
          The project to create. The server sets ``name`` in the response.

        :returns: :class:`Project`
        

    .. py:method:: delete(name: str)

        Moves a migration project to the workspace trash. The project keeps its ID until it's removed from the
        trash.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.


        

    .. py:method:: get(name: str) -> Project

        Gets a migration project, including its conversion settings and whether they're locked. To list the
        project's source files, call ``ListProjectFiles``. To track a conversion, call ``GetOperation``.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.

        :returns: :class:`Project`
        

    .. py:method:: get_file(name: str) -> ProjectFile

        Gets a file of a migration project, including the conversion details stored with its converted file,
        when available. Requires ``CAN_READ`` permission on the project and, once the file is converted, on
        the converted file.

        :param name: str
          The resource name of the file, in the format ``projects/{project_id}/files/{file_id}``. For example,
          ``projects/123/files/789``.

        :returns: :class:`ProjectFile`
        

    .. py:method:: get_operation(name: str) -> Operation

        Gets the latest state of a long-running operation, such as a conversion started by
        ``ConvertProjectFiles``. Operation names have the format
        ``projects/{project_id}/operations/{operation_id}``. Use the full name that the service returned, and
        treat the operation ID as opaque. Requires ``CAN_READ`` permission on the project.

        :param name: str
          The name of the operation resource.

        :returns: :class:`Operation`
        

    .. py:method:: list( [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Project]

        Lists the migration projects in a workspace folder. Select the folder with ``filter``; without a
        filter, lists the caller's home folder. Listing every project in the workspace isn't supported.

        Returns project summaries without conversion settings; call ``GetProject`` for the full project. A
        page can be empty even when more pages follow, so keep requesting pages until ``next_page_token`` is
        empty.

        :param filter: str (optional)
          The folder to list, as ``folder = "folders/{folder_id}"``. For example, ``folder = "folders/456"``.
          No other filter is supported. Defaults to the caller's home folder.
        :param page_size: int (optional)
          The maximum number of projects to return, at most 500. Defaults to 100 if omitted, zero, or
          negative. A page can have fewer projects than requested, or none, even when more pages follow.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response. Omit it for the first page. Use the same
          ``filter`` for every page.

        :returns: Iterator over :class:`Project`
        

    .. py:method:: list_files(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[ProjectFile]

        Lists the files of a migration project with their latest conversion statuses. To read a file's
        changes, to-do items, blockers, and notes, call ``GetProjectFile``. A page can have fewer files than
        requested, or none, even when more pages follow; keep requesting pages until ``next_page_token`` is
        empty.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param page_size: int (optional)
          The maximum number of files to return, at most 500. If omitted, zero, or negative, the server
          chooses. The server can return a different number of files than requested, so keep requesting pages
          until ``next_page_token`` is empty.
        :param page_token: str (optional)
          The ``next_page_token`` from a previous response. Omit it for the first page. Use it only with the
          same ``parent``.

        :returns: Iterator over :class:`ProjectFile`
        

    .. py:method:: remove_files(name: str [, names: Optional[List[str]]]) -> RemoveProjectFilesResponse

        Removes files from a migration project by their resource names. The source files and their converted
        output stay in the workspace.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``.
        :param names: List[str] (optional)
          The files to remove, by ``ProjectFile.name``. For example, ``projects/123/files/789``. Every file
          must belong to the project in ``name``. An empty list changes nothing. Send at most 10 files per
          request, the default limit. Requests over a project's limit return ``INVALID_PARAMETER_VALUE``.

        :returns: :class:`RemoveProjectFilesResponse`
        

    .. py:method:: review_project_files(parent: str, names: List[str]) -> ReviewProjectFilesResponse

        Marks files of a migration project as reviewed, accepting their converted output. Each file's status
        becomes ``FILE_STATUS_REVIEWED``, and reviewed files aren't converted again. Files that are already
        reviewed don't change. Returns the files in request order.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. Every file in ``names`` must belong to this project.
        :param names: List[str]
          The files to review: 1 to 100 distinct file resource names, in the format
          ``projects/{project_id}/files/{file_id}``. For example, ``projects/123/files/789``.

        :returns: :class:`ReviewProjectFilesResponse`
        

    .. py:method:: unreview_project_files(parent: str, names: List[str]) -> UnreviewProjectFilesResponse

        Removes the reviewed status from files of a migration project. Each file returns to the status it had
        before it was reviewed. Files that aren't reviewed don't change. Returns the files in request order.

        :param parent: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. Every file in ``names`` must belong to this project.
        :param names: List[str]
          The files to unreview: 1 to 100 distinct file resource names, in the format
          ``projects/{project_id}/files/{file_id}``. For example, ``projects/123/files/789``.

        :returns: :class:`UnreviewProjectFilesResponse`
        

    .. py:method:: update(name: str, project: Project, update_mask: FieldMask) -> Project

        Updates a migration project. Only the fields listed in ``update_mask`` change. An empty mask, or a
        mask with an unsupported field, returns ``INVALID_PARAMETER_VALUE``. When ``changes_locked`` is
        ``true``, the source dialect and target framework can't be changed.

        :param name: str
          The resource name of the project, in the format ``projects/{project_id}``. For example,
          ``projects/123``. The server assigns it when the project is created.
        :param project: :class:`Project`
          The project to update, identified by ``name``.
        :param update_mask: FieldMask
          The fields to update. Supported fields are ``display_name``, ``project_config.source_dialect``,
          ``project_config.target_framework``, and ``project_config.lineage_location``. ``project_config`` and
          ``*`` update all three ``project_config`` fields and can't be combined with ``display_name``.

        :returns: :class:`Project`
        