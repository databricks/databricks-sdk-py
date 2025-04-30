``w.genie``: Genie
==================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: GenieAPI

    Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces that
    business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled.

    .. py:method:: create_message(space_id: str, conversation_id: str, content: str) -> Wait[GenieMessage]

        Create conversation message.

        Create new message in a [conversation](:method:genie/startconversation). The AI response uses all
        previously created messages in the conversation to respond.

        :param space_id: str
          The ID associated with the Genie space where the conversation is started.
        :param conversation_id: str
          The ID associated with the conversation.
        :param content: str
          User message content.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        

    .. py:method:: create_message_and_wait(space_id: str, conversation_id: str, content: str, timeout: datetime.timedelta = 0:20:00) -> GenieMessage


    .. py:method:: execute_message_attachment_query(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

        Execute message attachment SQL query.

        Execute the SQL for a message query attachment. Use this API when the query attachment has expired and
        needs to be re-executed.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: execute_message_query(space_id: str, conversation_id: str, message_id: str) -> GenieGetMessageQueryResultResponse

        [Deprecated] Execute SQL query in a conversation message.

        Execute the SQL query in the message.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: generate_download_full_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGenerateDownloadFullQueryResultResponse

        Generate full query result download.

        Initiates a new SQL execution and returns a `download_id` that you can use to track the progress of
        the download. The query result is stored in an external link and can be retrieved using the [Get
        Download Full Query Result](:method:genie/getdownloadfullqueryresult) API. Warning: Databricks
        strongly recommends that you protect the URLs that are returned by the `EXTERNAL_LINKS` disposition.
        See [Execute Statement](:method:statementexecution/executestatement) for more details.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGenerateDownloadFullQueryResultResponse`
        

    .. py:method:: get_download_full_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str, download_id: str) -> GenieGetDownloadFullQueryResultResponse

        Get download full query result.

        After [Generating a Full Query Result Download](:method:genie/getdownloadfullqueryresult) and
        successfully receiving a `download_id`, use this API to poll the download progress. When the download
        is complete, the API returns one or more external links to the query result files. Warning: Databricks
        strongly recommends that you protect the URLs that are returned by the `EXTERNAL_LINKS` disposition.
        You must not set an Authorization header in download requests. When using the `EXTERNAL_LINKS`
        disposition, Databricks returns presigned URLs that grant temporary access to data. See [Execute
        Statement](:method:statementexecution/executestatement) for more details.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID
        :param download_id: str
          Download ID. This ID is provided by the [Generate Download
          endpoint](:method:genie/generateDownloadFullQueryResult)

        :returns: :class:`GenieGetDownloadFullQueryResultResponse`
        

    .. py:method:: get_message(space_id: str, conversation_id: str, message_id: str) -> GenieMessage

        Get conversation message.

        Get message from conversation.

        :param space_id: str
          The ID associated with the Genie space where the target conversation is located.
        :param conversation_id: str
          The ID associated with the target conversation.
        :param message_id: str
          The ID associated with the target message from the identified conversation.

        :returns: :class:`GenieMessage`
        

    .. py:method:: get_message_attachment_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

        Get message attachment SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY` OR `COMPLETED`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: get_message_query_result(space_id: str, conversation_id: str, message_id: str) -> GenieGetMessageQueryResultResponse

        [Deprecated] Get conversation message SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: get_message_query_result_by_attachment(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

        [Deprecated] Get conversation message SQL query result.

        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY` OR `COMPLETED`.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: get_space(space_id: str) -> GenieSpace

        Get Genie Space.

        Get details of a Genie Space.

        :param space_id: str
          The ID associated with the Genie space

        :returns: :class:`GenieSpace`
        

    .. py:method:: start_conversation(space_id: str, content: str) -> Wait[GenieMessage]

        Start conversation.

        Start a new conversation.

        :param space_id: str
          The ID associated with the Genie space where you want to start a conversation.
        :param content: str
          The text of the message that starts the conversation.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        

    .. py:method:: start_conversation_and_wait(space_id: str, content: str, timeout: datetime.timedelta = 0:20:00) -> GenieMessage


    .. py:method:: wait_get_message_genie_completed(conversation_id: str, message_id: str, space_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GenieMessage], None]]) -> GenieMessage
