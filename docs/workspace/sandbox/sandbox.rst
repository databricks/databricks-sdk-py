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
        