``w.global_init_scripts``: Global Init Scripts
==============================================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: GlobalInitScriptsAPI

    The Global Init Scripts API enables Workspace administrators to configure global initialization scripts
    for their workspace. These scripts run on every node in every cluster in the workspace.
    
    **Important:** Existing clusters must be restarted to pick up any changes made to global init scripts.
    Global init scripts are run in order. If the init script returns with a bad exit code, the Apache Spark
    container fails to launch and init scripts with later position are skipped. If enough containers fail, the
    entire cluster fails with a `GLOBAL_INIT_SCRIPT_FAILURE` error code.

    .. py:method:: create(name: str, script: str [, enabled: Optional[bool], position: Optional[int]]) -> CreateResponse


        Usage:

        .. code-block::

            import base64
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.global_init_scripts.create(
                name=f"sdk-{time.time_ns()}",
                script=base64.b64encode(("echo 1").encode()).decode(),
                enabled=True,
                position=10,
            )
            
            # cleanup
            w.global_init_scripts.delete(script_id=created.script_id)

        Create init script.
        
        Creates a new global init script in this workspace.
        
        :param name: str
          The name of the script
        :param script: str
          The Base64-encoded content of the script.
        :param enabled: bool (optional)
          Specifies whether the script is enabled. The script runs only if enabled.
        :param position: int (optional)
          The position of a global init script, where 0 represents the first script to run, 1 is the second
          script to run, in ascending order.
          
          If you omit the numeric position for a new global init script, it defaults to last position. It will
          run after all current scripts. Setting any value greater than the position of the last script is
          equivalent to the last position. Example: Take three existing scripts with positions 0, 1, and 2.
          Any position of (3) or greater puts the script in the last position. If an explicit position value
          conflicts with an existing script value, your request succeeds, but the original script at that
          position and all later scripts have their positions incremented by 1.
        
        :returns: :class:`CreateResponse`
        

    .. py:method:: delete(script_id: str)

        Delete init script.
        
        Deletes a global init script.
        
        :param script_id: str
          The ID of the global init script.
        
        
        

    .. py:method:: get(script_id: str) -> GlobalInitScriptDetailsWithContent


        Usage:

        .. code-block::

            import base64
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.global_init_scripts.create(
                name=f"sdk-{time.time_ns()}",
                script=base64.b64encode(("echo 1").encode()).decode(),
                enabled=True,
                position=10,
            )
            
            by_id = w.global_init_scripts.get(script_id=created.script_id)
            
            # cleanup
            w.global_init_scripts.delete(script_id=created.script_id)

        Get an init script.
        
        Gets all the details of a script, including its Base64-encoded contents.
        
        :param script_id: str
          The ID of the global init script.
        
        :returns: :class:`GlobalInitScriptDetailsWithContent`
        

    .. py:method:: list() -> Iterator[GlobalInitScriptDetails]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.global_init_scripts.list()

        Get init scripts.
        
        Get a list of all global init scripts for this workspace. This returns all properties for each script
        but **not** the script contents. To retrieve the contents of a script, use the [get a global init
        script](:method:globalinitscripts/get) operation.
        
        :returns: Iterator over :class:`GlobalInitScriptDetails`
        

    .. py:method:: update(script_id: str, name: str, script: str [, enabled: Optional[bool], position: Optional[int]])


        Usage:

        .. code-block::

            import base64
            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.global_init_scripts.create(
                name=f"sdk-{time.time_ns()}",
                script=base64.b64encode(("echo 1").encode()).decode(),
                enabled=True,
                position=10,
            )
            
            w.global_init_scripts.update(
                script_id=created.script_id,
                name=f"sdk-{time.time_ns()}",
                script=base64.b64encode(("echo 2").encode()).decode(),
            )
            
            # cleanup
            w.global_init_scripts.delete(script_id=created.script_id)

        Update init script.
        
        Updates a global init script, specifying only the fields to change. All fields are optional.
        Unspecified fields retain their current value.
        
        :param script_id: str
          The ID of the global init script.
        :param name: str
          The name of the script
        :param script: str
          The Base64-encoded content of the script.
        :param enabled: bool (optional)
          Specifies whether the script is enabled. The script runs only if enabled.
        :param position: int (optional)
          The position of a script, where 0 represents the first script to run, 1 is the second script to run,
          in ascending order. To move the script to run first, set its position to 0.
          
          To move the script to the end, set its position to any value greater or equal to the position of the
          last script. Example, three existing scripts with positions 0, 1, and 2. Any position value of 2 or
          greater puts the script in the last position (2).
          
          If an explicit position value conflicts with an existing script, your request succeeds, but the
          original script at that position and all later scripts have their positions incremented by 1.
        
        
        