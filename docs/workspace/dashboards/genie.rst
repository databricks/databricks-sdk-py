``w.genie``: Genie
==================
.. currentmodule:: databricks.sdk.service.dashboards

.. py:class:: GenieAPI

    Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up spaces that
    business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled.

    .. py:method:: create_message(space_id: str, conversation_id: str, content: str) -> Wait[GenieMessage]

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


    .. py:method:: create_space(warehouse_id: str, serialized_space: str [, description: Optional[str], parent_path: Optional[str], title: Optional[str]]) -> GenieSpace

        Creates a Genie space from a serialized payload.

        :param warehouse_id: str
          Warehouse to associate with the new space
        :param serialized_space: str
          The contents of the Genie Space in serialized string form. Use the [Get Genie
          Space](:method:genie/getspace) API to retrieve an example response, which includes the
          `serialized_space` field. This field provides the structure of the JSON string that represents the
          space's layout and components.
        :param description: str (optional)
          Optional description
        :param parent_path: str (optional)
          Parent folder path where the space will be registered
        :param title: str (optional)
          Optional title override

        :returns: :class:`GenieSpace`
        

    .. py:method:: delete_conversation(space_id: str, conversation_id: str)

        Delete a conversation.

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

        Initiates a new SQL execution and returns a `download_id` and `download_id_signature` that you can use
        to track the progress of the download. The query result is stored in an external link and can be
        retrieved using the [Get Download Full Query Result](:method:genie/getdownloadfullqueryresult) API.
        Both `download_id` and `download_id_signature` must be provided when calling the Get endpoint.

        ----

        ### **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        `EXTERNAL_LINKS` disposition.**

        When you use the `EXTERNAL_LINKS` disposition, a short-lived, URL is generated, which can be used to
        download the results directly from . As a short-lived is embedded in this URL, you should protect the
        URL.

        Because URLs are already generated with embedded temporary s, you must not set an `Authorization`
        header in the download requests.

        See [Execute Statement](:method:statementexecution/executestatement) for more details.

        ----

        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        :param attachment_id: str
          Attachment ID

        :returns: :class:`GenieGenerateDownloadFullQueryResultResponse`
        

    .. py:method:: get_download_full_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str, download_id: str, download_id_signature: str) -> GenieGetDownloadFullQueryResultResponse

        After [Generating a Full Query Result Download](:method:genie/generatedownloadfullqueryresult) and
        successfully receiving a `download_id` and `download_id_signature`, use this API to poll the download
        progress. Both `download_id` and `download_id_signature` are required to call this endpoint. When the
        download is complete, the API returns the result in the `EXTERNAL_LINKS` disposition, containing one
        or more external links to the query result files.

        ----

        ### **Warning: Databricks strongly recommends that you protect the URLs that are returned by the
        `EXTERNAL_LINKS` disposition.**

        When you use the `EXTERNAL_LINKS` disposition, a short-lived, URL is generated, which can be used to
        download the results directly from . As a short-lived is embedded in this URL, you should protect the
        URL.

        Because URLs are already generated with embedded temporary s, you must not set an `Authorization`
        header in the download requests.

        See [Execute Statement](:method:statementexecution/executestatement) for more details.

        ----

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

        Get message from conversation.

        :param space_id: str
          The ID associated with the Genie space where the target conversation is located.
        :param conversation_id: str
          The ID associated with the target conversation.
        :param message_id: str
          The ID associated with the target message from the identified conversation.

        :returns: :class:`GenieMessage`
        

    .. py:method:: get_message_attachment_query_result(space_id: str, conversation_id: str, message_id: str, attachment_id: str) -> GenieGetMessageQueryResultResponse

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
          Whether to include the serialized space export in the response. Requires at least CAN EDIT
          permission on the space.

        :returns: :class:`GenieSpace`
        

    .. py:method:: list_conversation_messages(space_id: str, conversation_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListConversationMessagesResponse

        List messages in a conversation

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

        Get a list of conversations in a Genie Space.

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
        

    .. py:method:: list_spaces( [, page_size: Optional[int], page_token: Optional[str]]) -> GenieListSpacesResponse

        Get list of Genie Spaces.

        :param page_size: int (optional)
          Maximum number of spaces to return per page
        :param page_token: str (optional)
          Pagination token for getting the next page of results

        :returns: :class:`GenieListSpacesResponse`
        

    .. py:method:: send_message_feedback(space_id: str, conversation_id: str, message_id: str, rating: GenieFeedbackRating)

        Send feedback for a message.

        :param space_id: str
          The ID associated with the Genie space where the message is located.
        :param conversation_id: str
          The ID associated with the conversation.
        :param message_id: str
          The ID associated with the message to provide feedback for.
        :param rating: :class:`GenieFeedbackRating`
          The rating (POSITIVE, NEGATIVE, or NONE).


        

    .. py:method:: start_conversation(space_id: str, content: str) -> Wait[GenieMessage]

        Start a new conversation.

        :param space_id: str
          The ID associated with the Genie space where you want to start a conversation.
        :param content: str
          The text of the message that starts the conversation.

        :returns:
          Long-running operation waiter for :class:`GenieMessage`.
          See :method:wait_get_message_genie_completed for more details.
        

    .. py:method:: start_conversation_and_wait(space_id: str, content: str, timeout: datetime.timedelta = 0:20:00) -> GenieMessage


    .. py:method:: trash_space(space_id: str)

        Move a Genie Space to the trash.

        :param space_id: str
          The ID associated with the Genie space to be sent to the trash.


        

    .. py:method:: update_space(space_id: str [, description: Optional[str], serialized_space: Optional[str], title: Optional[str], warehouse_id: Optional[str]]) -> GenieSpace

        Updates a Genie space with a serialized payload.

        :param space_id: str
          Genie space ID
        :param description: str (optional)
          Optional description
        :param serialized_space: str (optional)
          The contents of the Genie Space in serialized string form (full replacement). Use the [Get Genie
          Space](:method:genie/getspace) API to retrieve an example response, which includes the
          `serialized_space` field. This field provides the structure of the JSON string that represents the
          space's layout and components.
        :param title: str (optional)
          Optional title override
        :param warehouse_id: str (optional)
          Optional warehouse override

        :returns: :class:`GenieSpace`
        

    .. py:method:: wait_get_message_genie_completed(conversation_id: str, message_id: str, space_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GenieMessage], None]]) -> GenieMessage
