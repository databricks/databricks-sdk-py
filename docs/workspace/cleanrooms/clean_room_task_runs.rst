``w.clean_room_task_runs``: Task Runs
=====================================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomTaskRunsAPI

    Clean room task runs are the executions of notebooks in a clean room.

    .. py:method:: list(clean_room_name: str [, notebook_name: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CleanRoomNotebookTaskRun]

        List notebook task runs.

List all the historical notebook task runs in a clean room.

:param clean_room_name: str
  Name of the clean room.
:param notebook_name: str (optional)
  Notebook name
:param page_size: int (optional)
  The maximum number of task runs to return
:param page_token: str (optional)
  Opaque pagination token to go to next page based on previous query.

:returns: Iterator over :class:`CleanRoomNotebookTaskRun`
