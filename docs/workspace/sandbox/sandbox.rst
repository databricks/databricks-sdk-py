``w.sandbox``: Sandbox.v1
=========================
.. currentmodule:: databricks.sdk.service.sandbox

.. py:class:: SandboxExt

    Create, manage, and control the lifecycle of sandboxes -- isolated, pre-configured, low-latency Serverless
    compute environments for running code.

    .. py:method:: attach_command(name: str, command_id: str [, last_sequence_number: Optional[int], is_retryable: Optional[Callable[[Exception], bool]], max_attempts: int = 30, retry_interval_seconds: float = 3.0]) -> Iterator['_pb.AttachCommandResponse']

        Attach to a running command in sandbox ``name`` and stream its output.

        ``command_id`` comes from the ``StartEvent`` of a prior
        :meth:`execute_command_streaming`. The server replays buffered events with
        ``sequence_number`` greater than ``last_sequence_number`` (0 replays from
        the beginning; omitted tails live output only), then streams live events.

        Unlike :meth:`execute_command_streaming`, retries default to the
        transport's ``UNAVAILABLE`` policy: attach is a resumable replay, so
        re-opening from ``last_sequence_number`` is safe. Pass ``is_retryable`` to
        override.
        

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


        

    .. py:method:: execute_command_streaming(name: str, cmd: str [, args: Optional[list[str]], envs: Optional[Dict[str, str]], is_retryable: Optional[Callable[[Exception], bool]], max_attempts: int = 30, retry_interval_seconds: float = 3.0]) -> Iterator['_pb.ExecuteCommandResponse']

        Run ``cmd`` in sandbox ``name`` and stream its process events.

        Streaming counterpart of :meth:`SandboxAPI.execute_command_sync`: the same
        ``name`` (``sandboxes/{sandbox_id}``), ``cmd``, ``args``, and ``envs``,
        but the process output is streamed instead of returned in one response.
        Yields ``ExecuteCommandResponse`` messages, each carrying one
        ``ProcessEvent`` (a start event, then stdout/stderr data chunks, then an
        end event with the exit code) and a monotonic ``sequence_number``.

        Retries are off by default (``is_retryable`` defaults to
        :func:`_never_retry`) because ExecuteCommand is not idempotent: re-issuing
        a failed open could run the command twice. Pass an ``is_retryable``
        predicate - e.g. one matching ``UNAVAILABLE`` - to retry the stream open
        when the command is safe to run more than once, optionally tuning
        ``max_attempts`` and ``retry_interval_seconds``. Only the stream open is
        retried; a failure once events are flowing is always raised.
        

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
        

    .. py:method:: stream_input(name: str, command_id: str, inputs: Iterable[bytes] [, close_stdin: bool = True]) -> '_pb.StreamInputResponse'

        Forward stdin ``inputs`` to a running command in sandbox ``name``.

        ``command_id`` comes from the ``StartEvent`` of a prior
        :meth:`execute_command_streaming`. Sends a start message, one data message
        per chunk of ``inputs``, then (unless ``close_stdin`` is false) a close
        message that sends EOF to the process's stdin. Returns the server's
        acknowledgement once the input stream is fully sent.

        Not retried: forwarding input is stateful and side-effecting, so a
        transport failure is raised to the caller.
        

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
        