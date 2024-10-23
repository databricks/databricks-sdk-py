``w.command_execution``: Command Execution
==========================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: CommandExecutionAPI

    This API allows execution of Python, Scala, SQL, or R commands on running Databricks Clusters. This API
    only supports (classic) all-purpose clusters. Serverless compute is not supported.

    .. py:method:: cancel( [, cluster_id: Optional[str], command_id: Optional[str], context_id: Optional[str]]) -> Wait[CommandStatusResponse]

        Cancel a command.
        
        Cancels a currently running command within an execution context.
        
        The command ID is obtained from a prior successful call to __execute__.
        
        :param cluster_id: str (optional)
        :param command_id: str (optional)
        :param context_id: str (optional)
        
        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_cancelled for more details.
        

    .. py:method:: cancel_and_wait( [, cluster_id: Optional[str], command_id: Optional[str], context_id: Optional[str], timeout: datetime.timedelta = 0:20:00]) -> CommandStatusResponse


    .. py:method:: command_status(cluster_id: str, context_id: str, command_id: str) -> CommandStatusResponse

        Get command info.
        
        Gets the status of and, if available, the results from a currently executing command.
        
        The command ID is obtained from a prior successful call to __execute__.
        
        :param cluster_id: str
        :param context_id: str
        :param command_id: str
        
        :returns: :class:`CommandStatusResponse`
        

    .. py:method:: context_status(cluster_id: str, context_id: str) -> ContextStatusResponse

        Get status.
        
        Gets the status for an execution context.
        
        :param cluster_id: str
        :param context_id: str
        
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

        Create an execution context.
        
        Creates an execution context for running cluster commands.
        
        If successful, this method returns the ID of the new execution context.
        
        :param cluster_id: str (optional)
          Running cluster id
        :param language: :class:`Language` (optional)
        
        :returns:
          Long-running operation waiter for :class:`ContextStatusResponse`.
          See :method:wait_context_status_command_execution_running for more details.
        

    .. py:method:: create_and_wait( [, cluster_id: Optional[str], language: Optional[Language], timeout: datetime.timedelta = 0:20:00]) -> ContextStatusResponse


    .. py:method:: destroy(cluster_id: str, context_id: str)

        Delete an execution context.
        
        Deletes an execution context.
        
        :param cluster_id: str
        :param context_id: str
        
        
        

    .. py:method:: execute( [, cluster_id: Optional[str], command: Optional[str], context_id: Optional[str], language: Optional[Language]]) -> Wait[CommandStatusResponse]


        Usage:

        .. code-block::

            import os
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import compute
            
            w = WorkspaceClient()
            
            cluster_id = os.environ["TEST_DEFAULT_CLUSTER_ID"]
            
            context = w.command_execution.create(cluster_id=cluster_id, language=compute.Language.PYTHON).result()
            
            text_results = w.command_execution.execute(cluster_id=cluster_id,
                                                       context_id=context.id,
                                                       language=compute.Language.PYTHON,
                                                       command="print(1)").result()
            
            # cleanup
            w.command_execution.destroy(cluster_id=cluster_id, context_id=context.id)

        Run a command.
        
        Runs a cluster command in the given execution context, using the provided language.
        
        If successful, it returns an ID for tracking the status of the command's execution.
        
        :param cluster_id: str (optional)
          Running cluster id
        :param command: str (optional)
          Executable code
        :param context_id: str (optional)
          Running context id
        :param language: :class:`Language` (optional)
        
        :returns:
          Long-running operation waiter for :class:`CommandStatusResponse`.
          See :method:wait_command_status_command_execution_finished_or_error for more details.
        

    .. py:method:: execute_and_wait( [, cluster_id: Optional[str], command: Optional[str], context_id: Optional[str], language: Optional[Language], timeout: datetime.timedelta = 0:20:00]) -> CommandStatusResponse


    .. py:method:: wait_command_status_command_execution_cancelled(cluster_id: str, command_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[CommandStatusResponse], None]]) -> CommandStatusResponse


    .. py:method:: wait_command_status_command_execution_finished_or_error(cluster_id: str, command_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[CommandStatusResponse], None]]) -> CommandStatusResponse


    .. py:method:: wait_context_status_command_execution_running(cluster_id: str, context_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[ContextStatusResponse], None]]) -> ContextStatusResponse
