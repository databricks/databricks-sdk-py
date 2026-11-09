``w.sandbox``: Sandbox.v1
=========================
.. currentmodule:: databricks.sdk.service.sandbox

.. py:class:: SandboxExt

    Create, manage, and control the lifecycle of sandboxes -- isolated, pre-configured, low-latency Serverless
    compute environments for running code.

    .. py:method:: connect_command(name: str, command_id: str [, text: bool = True, stdout: StreamMode = StreamMode.PIPE, stderr: StreamMode = StreamMode.PIPE]) -> CommandProcess

        Return a :class:`CommandProcess` handle to a command already started in
        sandbox ``name``, such as one started by another client.

        ``command_id`` is :attr:`CommandProcess.command_id` of the original
        handle. The new handle replays the command's output from the beginning,
        then continues with live output. The server keeps a bounded amount of
        output per command, and keeps a finished command's output only briefly
        after it exits. ``text``, ``stdout``, and ``stderr`` work as in
        :meth:`execute_command`.
        

    .. py:method:: create_directory(parent: str, path: str [, parents: Optional[bool]]) -> CreateDirectoryResponse

        Creates a directory in a sandbox, including missing parents by default.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the directory.
        :param parents: bool (optional)
          Defaults to true, which also succeeds when the directory already exists.

        :returns: :class:`CreateDirectoryResponse`
        

    .. py:method:: create_sandbox(sandbox: Sandbox, sandbox_id: str) -> Sandbox

        Creates a new Sandbox.

        :param sandbox: :class:`Sandbox`
          The sandbox to create.
        :param sandbox_id: str
          Client-supplied ID that becomes the final path segment of the resource name.

        :returns: :class:`Sandbox`
        

    .. py:method:: delete_path(parent: str, path: str [, recursive: Optional[bool]]) -> DeletePathResponse

        Deletes a file, symlink, or empty directory, with an option for recursive deletion. Succeeds if the
        path is already absent.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the entry to delete.
        :param recursive: bool (optional)
          Required for a non-empty directory.

        :returns: :class:`DeletePathResponse`
        

    .. py:method:: delete_sandbox(name: str)

        Deletes a Sandbox.

        :param name: str


        

    .. py:method:: download_file(parent: str, path: str [, byte_range: Optional[str], if_match: Optional[str], if_modified_since: Optional[str], if_none_match: Optional[str], if_range: Optional[str], if_unmodified_since: Optional[str]]) -> DownloadFileResponse

        Downloads a regular file from a sandbox as an application/octet-stream body. The sandbox starts
        automatically if it is stopped. Filesystem access uses the sandbox user's permissions and follows
        symbolic links.

        A full download returns 200 OK. A satisfiable single byte range returns 206 Partial Content. Multiple
        byte ranges are unsupported and return 400. Invalid ranges are ignored; an unsatisfiable range returns
        416 with Content-Range describing the file length. Range is ignored for empty files.

        Conditional requests can return 304 Not Modified or 412 Precondition Failed. If-Range selects a
        partial response only when its strong entity tag matches; otherwise, the entire file is returned.
        HTTP-date validators in If-Range cause a full download. Reads are not snapshots: concurrent in-place
        writes can affect the returned bytes. HEAD is unsupported.

        Range and conditional options may be supplied as query parameters or HTTP headers. A parameter and one
        header may both be supplied when their values match exactly. Conflicting values or repeated parameters
        return 400.

        :param parent: str
          The sandbox resource name, in the form sandboxes/{sandbox_id}.
        :param path: str
          The absolute UTF-8 path of the file inside the sandbox.
        :param byte_range: str (optional)
          A single byte range, such as bytes=0-1023 or bytes=-1024. Equivalent to the Range header.
        :param if_match: str (optional)
          Entity tags or *. A mismatch returns 412 Precondition Failed. Equivalent to the If-Match header.
        :param if_modified_since: str (optional)
          An HTTP-date. Returns 304 if the file has not changed since this time. Ignored when If-None-Match is
          present. Equivalent to the If-Modified-Since header.
        :param if_none_match: str (optional)
          Entity tags or *. A match returns 304 Not Modified. Equivalent to the If-None-Match header.
        :param if_range: str (optional)
          A strong entity tag. A mismatch, weak entity tag, or HTTP-date causes a full download. Equivalent to
          the If-Range header.
        :param if_unmodified_since: str (optional)
          An HTTP-date. Returns 412 if the file has changed since this time. Ignored when If-Match is present.
          Equivalent to the If-Unmodified-Since header.

        :returns: :class:`DownloadFileResponse`
        

    .. py:method:: execute_command(name: str, cmd: str [, args: Optional[list[str]], envs: Optional[Dict[str, str]], text: bool = True, stdout: StreamMode = StreamMode.PIPE, stderr: StreamMode = StreamMode.PIPE]) -> CommandProcess

        Start ``cmd`` in sandbox ``name`` and return a :class:`CommandProcess`
        handle for its output, input, and exit code.

        Returns once the command has started. ``cmd`` runs directly, not in a
        shell. With ``text=True`` (the default) output is decoded as UTF-8 into
        ``str``; pass ``text=False`` for ``bytes``. ``stdout`` and ``stderr``
        choose where each stream goes (see :class:`StreamMode`).

        The start is not retried, so the command never runs twice.
        

    .. py:method:: execute_command_sync(name: str, cmd: str [, args: Optional[List[str]], envs: Optional[Dict[str, str]], execution_timeout: Optional[Duration]]) -> ExecuteCommandSyncResponse

        Runs a command in the sandbox and blocks until it exits, returning the captured stdout, stderr and
        exit code in a single response.

        :param name: str
          Resource name of the sandbox to run the command in, in the form ``sandboxes/{sandbox_id}``. Bound
          from the URL path.
        :param cmd: str
          Executable or command to run (e.g. ``/bin/echo``, ``python3``).
        :param args: List[str] (optional)
          Arguments passed to ``cmd``.
        :param envs: Dict[str,str] (optional)
          Extra environment variables for the command's process, merged over the sandbox's default
          environment.
        :param execution_timeout: Duration (optional)
          Maximum time to wait for the command to finish. When it elapses the command is terminated and the
          response carries status ``TIMED_OUT``. The server applies a default when unset and clamps to an
          upper bound; negative or otherwise invalid durations are rejected with ``INVALID_ARGUMENT``.

        :returns: :class:`ExecuteCommandSyncResponse`
        

    .. py:method:: get_metadata(parent: str, path: str) -> GetMetadataResponse

        Returns metadata for a path without following its final symlink.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the entry to inspect.

        :returns: :class:`GetMetadataResponse`
        

    .. py:method:: get_sandbox(name: str) -> Sandbox

        Retrieves a Sandbox by name.

        :param name: str

        :returns: :class:`Sandbox`
        

    .. py:method:: list_commands(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> ListCommandsResponse

        Lists the tracked command executions (running and completed) in a sandbox.

        :param parent: str
          The sandbox whose commands to list, in the form ``sandboxes/{sandbox_id}``.
        :param page_size: int (optional)
          Maximum number of commands to return. The server may return fewer. If unspecified, the server
          returns all commands.
        :param page_token: str (optional)
          Page token returned by a previous ListCommands call. Use this to retrieve the next page of results.

        :returns: :class:`ListCommandsResponse`
        

    .. py:method:: list_directory_contents(parent: str, path: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SandboxFileInfo]

        Lists a directory's immediate children in UTF-8 name order. Later pages may reflect concurrent
        changes.

        :param parent: str
        :param path: str
          Absolute UTF-8 path of the directory.
        :param page_size: int (optional)
          Zero uses the default of 1000; values above 1000 are clamped to 1000.
        :param page_token: str (optional)
          The token from a prior response. Keep parent and path unchanged between pages.

        :returns: Iterator over :class:`SandboxFileInfo`
        

    .. py:method:: list_sandboxes( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Sandbox]

        Lists all Sandboxes.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Sandbox`
        

    .. py:method:: rename_path(parent: str, source: str, destination: str) -> RenamePathResponse

        Renames a path within a sandbox. The destination must be absent and on the same filesystem.

        :param parent: str
          Sandbox resource name, for example ``sandboxes/my-sandbox``.
        :param source: str
          Absolute UTF-8 path to move.
        :param destination: str
          Exact absolute UTF-8 destination; it must not already exist.

        :returns: :class:`RenamePathResponse`
        

    .. py:method:: start_sandbox(name: str) -> Sandbox

        Starts a previously stopped Sandbox under the same sandbox name. Returns NOT_FOUND if there is no
        stopped sandbox to start for the given name.

        :param name: str
          Resource name of the sandbox to start, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        

    .. py:method:: stop_sandbox(name: str) -> Sandbox

        Stops a running Sandbox, preserving it so it can later be restarted with a Start request.

        :param name: str
          Resource name of the sandbox to stop, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        

    .. py:method:: update_sandbox(name: str, sandbox: Sandbox, update_mask: FieldMask) -> Sandbox

        Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today: display_name,
        spec.compute.inactivity_timeout. Returns INVALID_PARAMETER_VALUE for empty masks or unknown paths;
        NOT_FOUND if the sandbox does not exist.

        :param name: str
          Resource name of the sandbox to update, in the form ``sandboxes/{sandbox_id}``.
        :param sandbox: :class:`Sandbox`
          The Sandbox resource carrying new field values. Only fields named in ``update_mask`` are read;
          unmasked fields are ignored.
        :param update_mask: FieldMask
          Field paths to update. Must be a non-empty subset of:

          - display_name
          - spec.compute.inactivity_timeout Any other path returns INVALID_PARAMETER_VALUE.

        :returns: :class:`Sandbox`
        

    .. py:method:: upload_file(parent: str, contents: BinaryIO, path: str)

        Uploads an application/octet-stream body to a sandbox. The sandbox starts automatically if it is
        stopped. Filesystem access uses the sandbox user's permissions. Replacements follow symbolic links.

        Creates the file or replaces its entire contents, creating parent directories if missing. The
        completed upload becomes visible atomically. A failure before commit leaves an existing destination
        unchanged; a lost response after commit does not undo the upload. Completion does not guarantee crash
        durability.

        Returns 201 Created for a new file or 204 No Content for a replacement. Set overwrite=false or supply
        If-None-Match: * to create a file only if the destination does not exist. An existing entry, including
        a symbolic link, returns 412 Precondition Failed. Conflicting options or repeated overwrite parameters
        return 400. Other If-None-Match values, Content-Range, If-Match, and If-Unmodified-Since are
        unsupported and return 400.

        :param parent: str
          The sandbox resource name, in the form sandboxes/{sandbox_id}.
        :param contents: BinaryIO
          The complete file contents. An empty body creates an empty file.
        :param path: str
          The absolute UTF-8 destination path inside the sandbox.


        