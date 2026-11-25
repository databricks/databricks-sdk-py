``w.genie``: Genie
==================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: GenieAPI

    Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces that
    business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled.

    .. py:method:: create_message(space_id: str, conversation_id: str, content: str [, enable_visualization: Optional[bool]]) -> Wait[GenieMessage]

        Sends a new message in a chat-mode [conversation](:method:genie/startconversation). The AI response
        uses all previously created messages in the conversation to respond. The message is processed
        asynchronously. Poll [Get a conversation message](:method:genie/getmessage) until its ``status`` is
        ``COMPLETED``, ``FAILED``, or ``CANCELLED``.

        :param space_id: str
          The ID associated with the Genie space where the conversation is started.
        :param conversation_id: str
          The ID associated with the conversation.
        :param content: str
          User message content.
        :param enable_visualization: bool (optional)
          Enable visualization generation.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        

    .. py:method:: create_message_and_wait(space_id: str, conversation_id: str, content: str [, enable_visualization: Optional[bool], timeout: datetime.timedelta = 0:20:00]) -> GenieMessage


    .. py:method:: create_message_comment(space_id: str, conversation_id: str, message_id: str, content: str) -> GenieMessageComment

        Create a comment on a conversation message.

        :param space_id: str
          The ID associated with the Genie space.
        :param conversation_id: str
          The ID associated with the conversation.
        :param message_id: str
          The ID associated with the message.
        :param content: str
          Comment text content.

        :returns: :class:`GenieMessageComment`
        

    .. py:method:: create_space(warehouse_id: str, serialized_space: str [, description: Optional[str], parent_path: Optional[str], title: Optional[str]]) -> GenieSpace

        Creates a Genie space from a serialized payload.

        :param warehouse_id: str
          ID of the SQL warehouse that runs the queries Genie generates for the space, as a 16-character
          hexadecimal string.
        :param serialized_space: str
          Configuration of the new space as a JSON string. The configuration must include at least one table,
          metric view, volume, MCP connection, or sub-agent data source. To copy an existing space, use the
          value that [Get Genie Space](:method:genie/getspace) returns when ``include_serialized_space`` is
          true. For the JSON format and its validation rules, see
          https://docs.databricks.com/aws/en/genie-agents/conversation-api.
        :param description: str (optional)
          Description of the space, up to 16384 bytes.
        :param parent_path: str (optional)
          Path of the workspace folder in which to create the space.
        :param title: str (optional)
          Display name of the new space. A default name is assigned when omitted.

        :returns: :class:`GenieSpace`
        

    .. py:method:: delete_conversation(space_id: str, conversation_id: str)

        Deletes a conversation and all of its messages. Users can delete their own conversations. Deleting
        another user's conversation requires at least CAN MANAGE permission on the space.

        :param space_id: str
          The ID associated with the Genie space where the conversation is located.
        :param conversation_id: str
          The ID of the conversation to delete.


        

    .. py:method:: delete_conversation_message(space_id: str, conversation_id: str, message_id: str)

        Delete a conversation message.

        :param space_id: str
          The ID associated with the Genie space where the message is located.
        :param conversation_id: str
          The ID associated with the conversation.
        :param message_id: str
          The ID associated with the message to delete.


        

    .. py:method:: download_message_attachment_visualization(name: str) -> DownloadMessageAttachmentVisualizationResponse

        Download a rendered image of a message visualization attachment. The response body is the raw PNG
        image, not a JSON payload. This is only available if the attachment is a visualization and the message
        status is ``COMPLETED``.

        :param name: str
          The resource name of the attachment to render, in the format
          ``spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}``.

        :returns: :class:`DownloadMessageAttachmentVisualizationResponse`
        

    .. py:method:: execute_message_attachment_query(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

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

        DEPRECATED: Use [Execute Message Attachment Query](:method:genie/executemessageattachmentquery)
        instead.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: generate_download_full_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGenerateDownloadFullQueryResultResponse

        Initiates a new SQL execution and returns a ``download_id`` and ``download_id_signature`` that you can
        use to track the progress of the download. The query result is stored in an external link and can be
        retrieved using the [Get Download Full Query Result](:method:genie/getdownloadfullqueryresult) API.
        Both ``download_id`` and ``download_id_signature`` must be provided when calling the Get endpoint.

        **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        ``EXTERNAL_LINKS`` disposition.**

        When you use the ``EXTERNAL_LINKS`` disposition, a short-lived cloud-storage URL is generated to
        download the results. The URL contains temporary access credentials, so protect it and do not set an
        ``Authorization`` header in the download request.

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
        

    .. py:method:: genie_cancel_response(agent_id: str, conversation_id: str, response_id: str) -> GenieMessage

        Cancels an in-flight agent-mode response. ``response_id`` is the id returned in the
        ``response.created`` event from the agent-mode responses endpoint. The response stops at the next
        agent boundary and its terminal state is returned.

        :param agent_id: str
          The ID of the Genie agent (synonymous with the Genie space ID).
        :param conversation_id: str
          The ID of the conversation containing the response.
        :param response_id: str
          The ID of the response to cancel (the id from the ``response.created`` event).

        :returns: :class:`GenieMessage`
        

    .. py:method:: genie_create_eval_run(space_id: str [, benchmark_question_ids: Optional[List[str]]]) -> GenieEvalRunResponse

        Starts a benchmark evaluation run that asks Genie each selected benchmark question in a Genie space
        and compares every response with the benchmark SQL. The run executes asynchronously: the response is
        the new run with its current status. If it is still running, poll with the get method until the status
        is terminal.

        :param space_id: str
          The ID associated with the Genie space where the evaluations will be executed.
        :param benchmark_question_ids: List[str] (optional)
          List of benchmark question IDs to evaluate. These questions must exist in the specified Genie space.
          If none are specified, then all benchmark questions are evaluated.

        :returns: :class:`GenieEvalRunResponse`
        

    .. py:method:: genie_get_eval_result_details(space_id: str, eval_run_id: str, result_id: str) -> GenieEvalResultDetails

        Gets the full result for one benchmark question in an evaluation run: its assessment and the reasons
        for it, Genie's response with the SQL execution result, and the expected response from the benchmark.
        The result must belong to the given run.

        :param space_id: str
          The ID associated with the Genie space where the evaluation run is located.
        :param eval_run_id: str
          The unique identifier for the evaluation run.
        :param result_id: str
          The unique identifier for the evaluation result.

        :returns: :class:`GenieEvalResultDetails`
        

    .. py:method:: genie_get_eval_run(space_id: str, eval_run_id: str) -> GenieEvalRunResponse

        Gets the current status and summary counts of a benchmark evaluation run. Poll this method until
        ``eval_run_status`` is terminal: DONE, EVALUATION_CANCELLED or EVALUATION_TIMEOUT.

        :param space_id: str
          The ID associated with the Genie space where the evaluation run is located.
        :param eval_run_id: str
          The ID of the evaluation run, as returned when the run was created.

        :returns: :class:`GenieEvalRunResponse`
        

    .. py:method:: genie_list_eval_results(space_id: str, eval_run_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListEvalResultsResponse

        Lists the results of a benchmark evaluation run, one per benchmark question. Each entry carries the
        result status and a snapshot of the question and benchmark answer; the assessment and Genie's response
        are available through the result details method.

        :param space_id: str
          The ID associated with the Genie space where the evaluation run is located.
        :param eval_run_id: str
          The unique identifier for the evaluation run.
        :param page_size: int (optional)
          Maximum number of eval results to return per page.
        :param page_token: str (optional)
          Opaque token to retrieve the next page of results.

        :returns: :class:`GenieListEvalResultsResponse`
        

    .. py:method:: genie_list_eval_runs(space_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListEvalRunsResponse

        Lists the benchmark evaluation runs in a Genie space with the current status and summary counts of
        each run.

        :param space_id: str
          The ID associated with the Genie space where the evaluation run is located.
        :param page_size: int (optional)
          Maximum number of evaluation runs to return per page
        :param page_token: str (optional)
          Token to get the next page of results

        :returns: :class:`GenieListEvalRunsResponse`
        

    .. py:method:: get_download_full_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str, download_id: str, download_id_signature: str) -> GenieGetDownloadFullQueryResultResponse

        After [Generating a Full Query Result Download](:method:genie/generatedownloadfullqueryresult) and
        successfully receiving a ``download_id`` and ``download_id_signature``, use this API to poll the
        download progress. Both ``download_id`` and ``download_id_signature`` are required to call this
        endpoint. When the download is complete, the API returns the result in the ``EXTERNAL_LINKS``
        disposition, containing one or more external links to the query result files.

        **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        ``EXTERNAL_LINKS`` disposition.**

        When you use the ``EXTERNAL_LINKS`` disposition, a short-lived cloud-storage URL is generated to
        download the results. The URL contains temporary access credentials, so protect it and do not set an
        ``Authorization`` header in the download request.

        See [Execute Statement](:method:statementexecution/executestatement) for more details.

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
        :param download_id_signature: str
          JWT signature for the download_id to ensure secure access to query results

        :returns: :class:`GenieGetDownloadFullQueryResultResponse`
        

    .. py:method:: get_message(space_id: str, conversation_id: str, message_id: str) -> GenieMessage

        Gets a message from a chat-mode or agent-mode conversation. For a complete agent-mode transcript, use
        the List conversation items endpoint.

        :param space_id: str
          The ID associated with the Genie space where the target conversation is located.
        :param conversation_id: str
          The ID associated with the target conversation.
        :param message_id: str
          The ID associated with the target message from the identified conversation.

        :returns: :class:`GenieMessage`
        

    .. py:method:: get_message_attachment_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

        Gets the result of the SQL query in a message's query attachment. The result is available only while
        the message status is ``EXECUTING_QUERY`` or ``COMPLETED``.

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

        DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)
        instead.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: get_message_query_result_by_attachment(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

        DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)
        instead.

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGetMessageQueryResultResponse`
        

    .. py:method:: get_space(space_id: str [, include_serialized_space: Optional[bool]]) -> GenieSpace

        Get details of a Genie Space.

        :param space_id: str
          The ID associated with the Genie space
        :param include_serialized_space: bool (optional)
          Whether to include the serialized space export in the response. When true, the response also carries
          the configuration ``etag``. Requires at least CAN EDIT permission on the space.

        :returns: :class:`GenieSpace`
        

    .. py:method:: list_conversation_comments(space_id: str, conversation_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListConversationCommentsResponse

        List all comments across all messages in a conversation.

        :param space_id: str
          The ID associated with the Genie space.
        :param conversation_id: str
          The ID associated with the conversation.
        :param page_size: int (optional)
          Maximum number of comments to return per page.
        :param page_token: str (optional)
          Pagination token for getting the next page of results.

        :returns: :class:`GenieListConversationCommentsResponse`
        

    .. py:method:: list_conversation_messages(space_id: str, conversation_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListConversationMessagesResponse

        Lists messages in a chat-mode or agent-mode conversation. Agent-mode messages are returned as
        GenieMessage projections. Use the List conversation items endpoint for the complete reasoning and
        tool-call history.

        :param space_id: str
          The ID associated with the Genie space where the conversation is located
        :param conversation_id: str
          The ID of the conversation to list messages from
        :param page_size: int (optional)
          Maximum number of messages to return per page
        :param page_token: str (optional)
          Token to get the next page of results

        :returns: :class:`GenieListConversationMessagesResponse`
        

    .. py:method:: list_conversations(space_id: str [, include_all: Optional[bool], page_size: Optional[int], page_token: Optional[str]]) -> GenieListConversationsResponse

        Lists the conversations in a Genie space. By default the list contains only the caller's own
        conversations, ordered by most recent activity. With ``include_all``, it contains every user's
        conversations in the space, ordered by creation time with the newest first.

        :param space_id: str
          The ID of the Genie space to retrieve conversations from.
        :param include_all: bool (optional)
          Include all conversations in the space across all users. Requires at least CAN MANAGE permission on
          the space.
        :param page_size: int (optional)
          Maximum number of conversations to return per page
        :param page_token: str (optional)
          Token to get the next page of results

        :returns: :class:`GenieListConversationsResponse`
        

    .. py:method:: list_message_comments(space_id: str, conversation_id: str, message_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListMessageCommentsResponse

        List comments on a specific conversation message.

        :param space_id: str
          The ID associated with the Genie space.
        :param conversation_id: str
          The ID associated with the conversation.
        :param message_id: str
          The ID associated with the message.
        :param page_size: int (optional)
          Maximum number of comments to return per page.
        :param page_token: str (optional)
          Pagination token for getting the next page of results.

        :returns: :class:`GenieListMessageCommentsResponse`
        

    .. py:method:: list_spaces( [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListSpacesResponse

        Lists the Genie spaces that the caller can access, most recently updated first.

        :param page_size: int (optional)
          Maximum number of spaces to return per page
        :param page_token: str (optional)
          Pagination token for getting the next page of results

        :returns: :class:`GenieListSpacesResponse`
        

    .. py:method:: send_message_feedback(space_id: str, conversation_id: str, message_id: str, rating: GenieFeedbackRating [, comment: Optional[str]])

        Sends feedback for a message in a chat-mode or agent-mode conversation.

        :param space_id: str
          The ID associated with the Genie space where the message is located.
        :param conversation_id: str
          The ID associated with the conversation.
        :param message_id: str
          The ID associated with the message to provide feedback for.
        :param rating: :class:`GenieFeedbackRating`
          The rating (POSITIVE, NEGATIVE, or NONE).
        :param comment: str (optional)
          Optional text feedback that will be stored as a comment.


        

    .. py:method:: start_conversation(space_id: str, content: str [, enable_visualization: Optional[bool]]) -> Wait[GenieMessage]

        Starts a new chat-mode conversation and sends its first message. The message is processed
        asynchronously. Poll [Get a conversation message](:method:genie/getmessage) until its ``status`` is
        ``COMPLETED``, ``FAILED``, or ``CANCELLED``.

        :param space_id: str
          The ID associated with the Genie space where you want to start a conversation.
        :param content: str
          The text of the message that starts the conversation.
        :param enable_visualization: bool (optional)
          Enable visualization generation.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        

    .. py:method:: start_conversation_and_wait(space_id: str, content: str [, enable_visualization: Optional[bool], timeout: datetime.timedelta = 0:20:00]) -> GenieMessage


    .. py:method:: trash_space(space_id: str)

        Move a Genie Space to the trash.

        :param space_id: str
          The ID associated with the Genie space to be sent to the trash.


        

    .. py:method:: update_space(space_id: str [, description: Optional[str], etag: Optional[str], parent_path: Optional[str], serialized_space: Optional[str], title: Optional[str], warehouse_id: Optional[str]]) -> GenieSpace

        Updates a Genie space. Replaces the whole configuration when ``serialized_space`` is set and changes
        the title, description, warehouse or folder when those fields are set; omitted fields keep their
        current values.

        :param space_id: str
          Genie space ID
        :param description: str (optional)
          New description for the space, up to 16384 bytes.
        :param etag: str (optional)
          ETag returned by a previous GET or UPDATE. When set, the update will fail if the space has been
          modified since. Omit to apply the update unconditionally.
        :param parent_path: str (optional)
          Parent workspace folder path to move this Genie space under.
        :param serialized_space: str (optional)
          New configuration of the space as a JSON string. It replaces the whole configuration; when omitted,
          the current configuration is kept. Start from the value that [Get Genie
          Space](:method:genie/getspace) returns when ``include_serialized_space`` is true. For the JSON
          format and its validation rules, see
          https://docs.databricks.com/aws/en/genie-agents/conversation-api.
        :param title: str (optional)
          New display name for the space. Cannot be empty or contain a slash.
        :param warehouse_id: str (optional)
          ID of the SQL warehouse that runs the queries Genie generates for the space.

        :returns: :class:`GenieSpace`
        

    .. py:method:: wait_get_message_genie_completed(conversation_id: str, message_id: str, space_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GenieMessage], None]]) -> GenieMessage
