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
        

    .. py:method:: create_sandbox(sandbox: Sandbox, sandbox_id: str) -> Sandbox

        Creates a new Sandbox.

        :param sandbox: :class:`Sandbox`
          The sandbox to create.
        :param sandbox_id: str
          Client-supplied ID that becomes the final path segment of the resource name.

        :returns: :class:`Sandbox`
        

    .. py:method:: delete_sandbox(name: str)

        Deletes a Sandbox.

        :param name: str


        

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
        

    .. py:method:: list_sandboxes( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Sandbox]

        Lists all Sandboxes.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Sandbox`
        

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
        