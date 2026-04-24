``w.supervisor_agents``: SupervisorAgents.v1
============================================
.. currentmodule:: databricks.sdk.service.supervisoragents

.. py:class:: SupervisorAgentsAPI

    Manage Supervisor Agents and related resources.

    .. py:method:: create_supervisor_agent(supervisor_agent: SupervisorAgent) -> SupervisorAgent

        Creates a new Supervisor Agent.

        :param supervisor_agent: :class:`SupervisorAgent`
          The Supervisor Agent to create.

        :returns: :class:`SupervisorAgent`
        

    .. py:method:: create_tool(parent: str, tool: Tool, tool_id: str) -> Tool

        Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",
        "uc_function", "uc_connection", "app", "volume", "lakeview_dashboard", "uc_table",
        "vector_search_index" in the request body.

        :param parent: str
          Parent resource where this tool will be created. Format: supervisor-agents/{supervisor_agent_id}
        :param tool: :class:`Tool`
        :param tool_id: str
          The ID to use for the tool, which will become the final component of the tool's resource name.

        :returns: :class:`Tool`
        

    .. py:method:: delete_supervisor_agent(name: str)

        Deletes a Supervisor Agent.

        :param name: str
          The resource name of the Supervisor Agent. Format: supervisor-agents/{supervisor_agent_id}


        

    .. py:method:: delete_tool(name: str)

        Deletes a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}


        

    .. py:method:: get_supervisor_agent(name: str) -> SupervisorAgent

        Gets a Supervisor Agent.

        :param name: str
          The resource name of the Supervisor Agent. Format: supervisor-agents/{supervisor_agent_id}

        :returns: :class:`SupervisorAgent`
        

    .. py:method:: get_tool(name: str) -> Tool

        Gets a Tool.

        :param name: str
          The resource name of the Tool. Format: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}

        :returns: :class:`Tool`
        

    .. py:method:: list_supervisor_agents( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[SupervisorAgent]

        Lists Supervisor Agents.

        :param page_size: int (optional)
          The maximum number of supervisor agents to return. If unspecified, at most 100 supervisor agents
          will be returned. The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous `ListSupervisorAgents` call. Provide this to retrieve the
          subsequent page. If unspecified, the first page will be returned.

        :returns: Iterator over :class:`SupervisorAgent`
        

    .. py:method:: list_tools(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Tool]

        Lists Tools under a Supervisor Agent.

        :param parent: str
          Parent resource to list from. Format: supervisor-agents/{supervisor_agent_id}
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`Tool`
        

    .. py:method:: update_supervisor_agent(name: str, supervisor_agent: SupervisorAgent, update_mask: FieldMask) -> SupervisorAgent

        Updates a Supervisor Agent. The fields that are required depend on the paths specified in
        `update_mask`. Only fields included in the mask will be updated.

        :param name: str
          The resource name of the SupervisorAgent. Format: supervisor-agents/{supervisor_agent_id}
        :param supervisor_agent: :class:`SupervisorAgent`
          The SupervisorAgent to update.
        :param update_mask: FieldMask
          Field mask for fields to be updated.

        :returns: :class:`SupervisorAgent`
        

    .. py:method:: update_tool(name: str, tool: Tool, update_mask: FieldMask) -> Tool

        Updates a Tool. Only the `description` field can be updated. To change immutable fields such as tool
        type, spec, or tool ID, delete the tool and recreate it.

        :param name: str
          Full resource name: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}
        :param tool: :class:`Tool`
          The Tool to update.
        :param update_mask: FieldMask
          Field mask for fields to be updated.

        :returns: :class:`Tool`
        