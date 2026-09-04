``w.sandbox``: Sandbox.v1
=========================
.. currentmodule:: databricks.sdk.service.sandbox

.. py:class:: SandboxAPI

    Create, manage, and control the lifecycle of sandboxes -- isolated, pre-configured, low-latency Serverless
    compute environments for running code.

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


        

    .. py:method:: execute_command_sync(name: str, cmd: str [, args: Optional[List[str]], envs: Optional[Dict[str, str]], execution_timeout: Optional[Duration]]) -> ExecuteCommandSyncResponse

        Runs a command in the sandbox and blocks until it exits, returning the captured stdout, stderr and
        exit code in a single response. Unary convenience variant of the streaming command-execution API for
        callers that only need a command's final result (e.g. ``curl``, the SDK's ``sandbox.exec``). The
        streaming ``ExecuteCommand`` RPC remains for interactive and long-running use.

        :param name: str
          Resource name of the sandbox to run the command in, in the form ``sandboxes/{sandbox_id}``. Bound
          from the URL path.
        :param cmd: str
          Executable or command to run (e.g. ``/bin/echo``, ``python3``). A request with no ``cmd`` is
          rejected with ``INVALID_ARGUMENT``. Not audited (no ``compliance.audit_mode``): the command can
          carry secrets, and as a data-plane service lakebox must not record privileged customer content in
          its audit log.
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
        

    .. py:method:: list_sandboxes( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Sandbox]

        Lists all Sandboxes.

        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Sandbox`
        

    .. py:method:: start_sandbox(name: str) -> Sandbox

        Starts a stopped Sandbox by atomically restoring the TerminatedSandbox tombstone to the active table
        in PENDING and re-running the provisioning workflow. The provisioning workflow's claimWarmPoolSandbox
        step re-mints the app_instance_name (deterministic from sandbox_id, so equal to the prior life's
        name). The tombstone's volume_id is preserved so the new AppInstance binds to the same backing device
        file. The restored sandbox gets a fresh uid and create_time. Returns NOT_FOUND if no tombstone exists
        for the given (workspace_id, sandbox_id) — the sandbox may not exist or may currently be active;
        clients can disambiguate via Get.

        :param name: str
          Resource name of the sandbox to start, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        

    .. py:method:: stop_sandbox(name: str) -> Sandbox

        Stops a Sandbox, terminating the sandbox while allowing future use of StartSandbox to re-provision the
        same Sandbox without re-creating a brand new one. Transitions the active row to TERMINATING with
        USER_REQUEST_STOP; the termination workflow settles to a TerminatedSandbox tombstone (no row drop) so
        the sandbox can later be restarted via StartSandbox.

        :param name: str
          Resource name of the sandbox to stop, in the form ``sandboxes/{sandbox_id}``.

        :returns: :class:`Sandbox`
        

    .. py:method:: update_sandbox(name: str, sandbox: Sandbox, update_mask: FieldMask) -> Sandbox

        Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today:
        metadata.display_name, spec.compute.inactivity_timeout. Returns INVALID_PARAMETER_VALUE for empty
        masks or unknown paths; NOT_FOUND if no active row or tombstone exists for the given sandbox.
        Concurrent-update conflicts surface as ABORTED via EStore OccConflict.

        :param name: str
          Resource name of the sandbox to update, in the form ``sandboxes/{sandbox_id}``.
        :param sandbox: :class:`Sandbox`
          The Sandbox resource carrying new field values. Only fields named in ``update_mask`` are read;
          unmasked fields are ignored.
        :param update_mask: FieldMask
          Field paths to update. Must be a non-empty subset of:

          - metadata.display_name
          - spec.compute.inactivity_timeout Any other path returns INVALID_PARAMETER_VALUE.

        :returns: :class:`Sandbox`
        