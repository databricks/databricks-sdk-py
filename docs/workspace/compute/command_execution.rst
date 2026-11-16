``w.command_execution``: Command Execution
==========================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: CommandExecutionAPI

    This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters. This API
    only supports (classic) all-purpose clusters. Serverless compute is not supported.

    .. py:method:: cancel( [, cluster_id: Optional[str], command_id: Optional[str], context_id: Optional[str]]) -> Wait[CommandStatusResponse]

        Cancels a currently running command within an execution context.

        The command ID is obtained from a prior successful call to **execute**. Cancellation is asynchronous:
        this method returns once the request is accepted, and the command moves through the ``Cancelling``
        status before reaching a terminal one. Poll **commandStatus** to observe the outcome; a cancelled
        command ends in the ``Finished`` status with an ``error`` result that describes the cancellation.

        :param cluster_id: str (optional)
          ID of the cluster that hosts the execution context.
        :param command_id: str (optional)
          ID of the command to cancel, as returned by **execute**.
        :param context_id: str (optional)
          ID of the execution context the command runs in.

        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_cancelled for more details.
        

    .. py:method:: cancel_and_wait( [, cluster_id: Optional[str], command_id: Optional[str], context_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> CommandStatusResponse


    .. py:method:: command_status(cluster_id: str, context_id: str, command_id: str) -> CommandStatusResponse

        Gets the status of and, if available, the results from a currently executing command.

        The command ID is obtained from a prior successful call to **execute**. Poll this method until the
        status is one of the terminal values ``Finished``, ``Error`` or ``Cancelled``; the ``results`` field
        is populated only once the command has reached a terminal status.

        :param cluster_id: str
          ID of the cluster that hosts the execution context.
        :param context_id: str
          ID of the execution context the command runs in.
        :param command_id: str
          ID of the command, as returned by **execute**.

        :returns: :class:`CommandStatusResponse`
        

    .. py:method:: context_status(cluster_id: str, context_id: str) -> ContextStatusResponse

        Gets the status for an execution context.

        After **Create**, poll this method until the status is ``Running`` or ``Error``. Requests for a
        context that has been deleted fail with an error instead of returning a status.

        :param cluster_id: str
          ID of the cluster that hosts the execution context.
        :param context_id: str
          ID of the execution context, as returned by **Create**.

        :returns: :class:`ContextStatusResponse`
        

    .. py:method:: create( [, cluster_id: Optional[str], language: Optional[Language]]) -> Wait[ContextStatusResponse]


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]
            
            context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()
            
            # cleanup
            w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

        Creates an execution context for running cluster commands.

        If successful, this method returns the ID of the new execution context. The context may still be
        initializing when this method returns, so poll **contextStatus** until the status is ``Running``
        before running commands in it. This method and the other methods of this API require the CAN ATTACH TO
        permission on the cluster.

        :param cluster_id: str (optional)
          ID of the cluster to create the execution context on. The cluster must be running.
        :param language: :class:`Language` (optional)
          Programming language of the execution context.

        :returns:
          Long-running operation waiter for :class:`ContextStatusResponse`.
          See :method:wait_context_status_command_execution_running for more details.
        

    .. py:method:: create_and_wait( [, cluster_id: Optional[str], language: Optional[Language], timeout: datetime.timedelta = 0:20:00]) -> ContextStatusResponse


    .. py:method:: destroy(cluster_id: str, context_id: str)

        Deletes an execution context.

        Delete contexts you no longer need, because a cluster can host only a limited number of execution
        contexts at a time. Deleting a context that no longer exists succeeds, so the call is safe to retry.

        :param cluster_id: str
          ID of the cluster that hosts the execution context.
        :param context_id: str
          ID of the execution context to delete, as returned by **Create**.


        

    .. py:method:: execute( [, cluster_id: Optional[str], command: Optional[str], context_id: Optional[str], language: Optional[Language]]) -> Wait[CommandStatusResponse]


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]
            
            context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()
            
            text_results = w.command_execution.execute(
                cluster_id=cluster_id,
                context_id=context.id,
                language=compute.Language.PYTHON,
                command="print(1)",
            ).result()
            
            # cleanup
            w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

        Runs a cluster command in the given execution context, using the provided language.

        If successful, it returns an ID for tracking the status of the command's execution. This method
        returns as soon as the command is accepted, so poll **commandStatus** with the returned ID to wait for
        the command to finish and to read its results.

        :param cluster_id: str (optional)
          ID of the cluster that hosts the execution context.
        :param command: str (optional)
          Code to run, written in the specified language.
        :param context_id: str (optional)
          ID of the execution context to run the command in, as returned by **Create**.
        :param language: :class:`Language` (optional)
          Language the command is written in.

        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_finished_or_error for more details.
        

    .. py:method:: execute_and_wait( [, cluster_id: Optional[str], command: Optional[str], context_id: Optional[str], language: Optional[Language], timeout: datetime.timedelta = 0:20:00]) -> CommandStatusResponse


    .. py:method:: wait_command_status_command_execution_cancelled(cluster_id: str, command_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[CommandStatusResponse], None]]) -> CommandStatusResponse


    .. py:method:: wait_command_status_command_execution_finished_or_error(cluster_id: str, command_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[CommandStatusResponse], None]]) -> CommandStatusResponse


    .. py:method:: wait_context_status_command_execution_running(cluster_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ContextStatusResponse], None]]) -> ContextStatusResponse
