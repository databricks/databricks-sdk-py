``w.genie_agents``: GenieAgents.v1
==================================
.. currentmodule:: databricks.sdk.service.genieagents

.. py:class:: GenieAgentsAPI

    Genie provides a no-code experience for business users, powered by AI/BI. Analysts set up Genie Agents
    that business users can use to ask questions using natural language. Genie uses data registered to Unity
    Catalog and requires at least CAN USE permission on a Pro or Serverless SQL warehouse. Also, Databricks
    Assistant must be enabled.

    .. py:method:: create_genie_agent(genie_agent: GenieAgent [, genie_agent_id: Optional[str]]) -> GenieAgent

        Creates a Genie Agent.

        :param genie_agent: :class:`GenieAgent`
          The Genie Agent to create.
        :param genie_agent_id: str (optional)
          The ID for the new Genie Agent: 32 lowercase hexadecimal characters (a UUID without dashes), not all
          zeros. Assigned by the server if omitted. Fails with ALREADY_EXISTS if the ID is in use in the
          workspace, including by a Genie Agent in the trash, or PERMISSION_DENIED if the caller cannot view
          the Genie Agent using it.

        :returns: :class:`GenieAgent`
        

    .. py:method:: delete_genie_agent(name: str [, etag: Optional[str]])

        Deletes a Genie Agent, moving it to trash.

        :param name: str
          The resource name of the Genie Agent to delete, in the form ``agents/{genie_agent_id}``.
        :param etag: str (optional)
          Etag from a previous read. On mismatch the delete fails with ABORTED and nothing is deleted.


        

    .. py:method:: get_genie_agent(name: str) -> GenieAgent

        Gets a Genie Agent.

        :param name: str
          The resource name of the Genie Agent to retrieve, in the form ``agents/{genie_agent_id}``.

        :returns: :class:`GenieAgent`
        

    .. py:method:: list_genie_agents( [, page_size: Optional[int], page_token: Optional[str], view: Optional[GenieAgentView]]) -> Iterator[GenieAgent]

        Lists the Genie Agents in the workspace. Genie Agents created from an integration (for example, from a
        dashboard) are not listed.

        :param page_size: int (optional)
          Maximum number of Genie Agents to return per page. Defaults to 20 when unset or 0; values above 100
          are coerced to 100. Negative values are rejected with INVALID_PARAMETER_VALUE. With
          ``GENIE_AGENT_VIEW_FULL``, a smaller per-page maximum applies.
        :param page_token: str (optional)
          Pagination token from a previous response's ``next_page_token``. A token that was not returned by
          this method is rejected with INVALID_PARAMETER_VALUE.
        :param view: :class:`GenieAgentView` (optional)
          The fields to return for each Genie Agent. Defaults to ``GENIE_AGENT_VIEW_BASIC``. Use
          ``GENIE_AGENT_VIEW_FULL`` only when the agent bodies are needed, since it returns smaller pages.

        :returns: Iterator over :class:`GenieAgent`
        

    .. py:method:: update_genie_agent(name: str, genie_agent: GenieAgent, update_mask: FieldMask [, etag: Optional[str]]) -> GenieAgent

        Updates a Genie Agent. Only the fields named in update_mask are applied.

        :param name: str
          The resource name of the Genie Agent, in the form ``agents/{genie_agent_id}``. Ignored on create.
        :param genie_agent: :class:`GenieAgent`
          The Genie Agent to update. Its ``name`` identifies the resource; fields named in update_mask are
          applied.
        :param update_mask: FieldMask
          The set of fields to update. The mask is required and must name at least one field; an empty or
          absent mask is rejected with INVALID_PARAMETER_VALUE, as is a path that is not an updatable field.

          A field named in the mask takes the value from ``genie_agent``, even when it is unset there: an
          unset ``description`` is cleared; an unset ``display_name``, ``warehouse_id``, or ``definition`` is
          rejected with INVALID_PARAMETER_VALUE; an unset ``parent_path`` is cleared without moving the Genie
          Agent. ``definition`` is replaced as a whole; paths within it are not supported.

          The special value ``*`` replaces the whole Genie Agent, as if every updatable field were named. It
          must be the only path in the mask. Prefer naming fields explicitly: with ``*``, any field added to
          Genie Agent later is also replaced, so a client unaware of it may clear it.
        :param etag: str (optional)
          Etag from a previous read. On mismatch the update fails with ABORTED (metadata changes may already
          be applied); get the agent and retry. May return TEMPORARILY_UNAVAILABLE.

        :returns: :class:`GenieAgent`
        