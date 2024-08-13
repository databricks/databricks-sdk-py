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
        
        Create new message in [conversation](:method:genie/startconversation). The AI response uses all
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


    .. py:method:: execute_message_query(space_id: str, conversation_id: str, message_id: str) -> GenieGetMessageQueryResultResponse

        Execute SQL query in a conversation message.
        
        Execute the SQL query in the message.
        
        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        
        :returns: :class:`GenieGetMessageQueryResultResponse`
        

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
        

    .. py:method:: get_message_query_result(space_id: str, conversation_id: str, message_id: str) -> GenieGetMessageQueryResultResponse

        Get conversation message SQL query result.
        
        Get the result of SQL query if the message has a query attachment. This is only available if a message
        has a query attachment and the message status is `EXECUTING_QUERY`.
        
        :param space_id: str
          Genie space ID
        :param conversation_id: str
          Conversation ID
        :param message_id: str
          Message ID
        
        :returns: :class:`GenieGetMessageQueryResultResponse`
        

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
