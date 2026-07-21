``w.clean_room_task_runs``: Task Runs
=====================================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomTaskRunsAPI

    Clean room task runs are the executions of notebooks and JAR analyses in a clean room.

    .. py:method:: list(clean_room_name: str [, notebook_name: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CleanRoomNotebookTaskRun]

        List all the historical notebook task runs in a clean room.

        :param clean_room_name: str
          Name of the clean room.
        :param notebook_name: str (optional)
          Notebook name
        :param page_size: int (optional)
          The maximum number of task runs to return. Currently ignored - all runs will be returned.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.

        :returns: Iterator over :class:`CleanRoomNotebookTaskRun`
        

    .. py:method:: list_clean_room_task_runs_handler(clean_room_name: str [, name: Optional[str], page_size: Optional[int], page_token: Optional[str], task_type: Optional[CleanRoomTaskType]]) -> Iterator[CleanRoomTaskRun]

        List all the historical task runs in a clean room.

        :param clean_room_name: str
          Name of the clean room.
        :param name: str (optional)
          Executable name.
        :param page_size: int (optional)
          The maximum number of task runs to return. Maximum value of 100.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        :param task_type: :class:`CleanRoomTaskType` (optional)
          Filter by the type of Clean Room task.

        :returns: Iterator over :class:`CleanRoomTaskRun`
        