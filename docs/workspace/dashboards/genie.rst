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
        

    .. py:method:: get_space(space_id: str) -> GenieSpace

        Get details of a Genie Space.

        :param space_id: str
          The ID associated with the Genie space

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


        

    .. py:method:: wait_get_message_genie_completed(conversation_id: str, message_id: str, space_id: str, timeout: datetime.timedelta = 0:20:00, callback: Optional[Callable[[GenieMessage], None]]) -> GenieMessage
