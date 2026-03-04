``w.supervisor_agents``: SupervisorAgents.v1
============================================
.. currentmodule:: databricks.sdk.service.supervisoragents

.. py:class:: SupervisorAgentsAPI

    Manage Supervisor Agents and related resources.

    .. py:method:: create_supervisor_agent(supervisor_agent: SupervisorAgent) -> SupervisorAgent


    .. py:method:: create_tool(parent: str, tool: Tool) -> Tool

        Creates a Tool under a Supervisor Agent.

        :param parent: str
          Parent resource where this tool will be created. Format: supervisor-agents/{supervisor_agent_id}
        :param tool: :class:`Tool`

        :returns: :class:`Tool`
        

    .. py:method:: delete_supervisor_agent(name: str)


    .. py:method:: delete_tool(name: str)

        Deletes a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}


        

    .. py:method:: get_supervisor_agent(name: str) -> SupervisorAgent


    .. py:method:: get_tool(name: str) -> Tool

        Gets a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}

        :returns: :class:`Tool`
        

    .. py:method:: list_supervisor_agents( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SupervisorAgent]


    .. py:method:: list_tools(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Tool]

        Lists Tools under a Supervisor Agent.

        :param parent: str
          Parent resource to list from. Format: supervisor-agents/{supervisor_agent_id}
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Tool`
        

    .. py:method:: update_supervisor_agent(name: str, supervisor_agent: SupervisorAgent, update_mask: FieldMask) -> SupervisorAgent


    .. py:method:: update_tool(name: str, tool: Tool, update_mask: FieldMask) -> Tool

        Updates a Tool.

        :param name: str
        :param tool: :class:`Tool`
          The Tool to update.
        :param update_mask: FieldMask
          Field mask for fields to be updated.

        :returns: :class:`Tool`
        