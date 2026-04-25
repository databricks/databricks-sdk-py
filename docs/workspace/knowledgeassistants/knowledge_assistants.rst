``w.knowledge_assistants``: KnowledgeAssistants.v1
==================================================
.. currentmodule:: databricks.sdk.service.knowledgeassistants

.. py:class:: KnowledgeAssistantsAPI

    Manage Knowledge Assistants and related resources.

    .. py:method:: create_knowledge_assistant(knowledge_assistant: KnowledgeAssistant) -> KnowledgeAssistant

        Creates a Knowledge Assistant.

        :param knowledge_assistant: :class:`KnowledgeAssistant`
          The Knowledge Assistant to create.

        :returns: :class:`KnowledgeAssistant`
        

    .. py:method:: create_knowledge_source(parent: str, knowledge_source: KnowledgeSource) -> KnowledgeSource

        Creates a Knowledge Source under a Knowledge Assistant.

        :param parent: str
          Parent resource where this source will be created. Format:
          knowledge-assistants/{knowledge_assistant_id}
        :param knowledge_source: :class:`KnowledgeSource`

        :returns: :class:`KnowledgeSource`
        

    .. py:method:: delete_knowledge_assistant(name: str)

        Deletes a Knowledge Assistant.

        :param name: str
          The resource name of the knowledge assistant to be deleted. Format:
          knowledge-assistants/{knowledge_assistant_id}


        

    .. py:method:: delete_knowledge_source(name: str)

        Deletes a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source to delete. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}


        

    .. py:method:: get_knowledge_assistant(name: str) -> KnowledgeAssistant

        Gets a Knowledge Assistant.

        :param name: str
          The resource name of the knowledge assistant. Format: knowledge-assistants/{knowledge_assistant_id}

        :returns: :class:`KnowledgeAssistant`
        

    .. py:method:: get_knowledge_source(name: str) -> KnowledgeSource

        Gets a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}

        :returns: :class:`KnowledgeSource`
        

    .. py:method:: get_permission_levels(knowledge_assistant_id: str) -> GetKnowledgeAssistantPermissionLevelsResponse

        Gets the permission levels that a user can have on an object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.

        :returns: :class:`GetKnowledgeAssistantPermissionLevelsResponse`
        

    .. py:method:: get_permissions(knowledge_assistant_id: str) -> KnowledgeAssistantPermissions

        Gets the permissions of a knowledge assistant. Knowledge assistants can inherit permissions from their
        root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.

        :returns: :class:`KnowledgeAssistantPermissions`
        

    .. py:method:: list_knowledge_assistants( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[KnowledgeAssistant]

        List Knowledge Assistants

        :param page_size: int (optional)
          The maximum number of knowledge assistants to return. If unspecified, at most 100 knowledge
          assistants will be returned. The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token: str (optional)
          A page token, received from a previous `ListKnowledgeAssistants` call. Provide this to retrieve the
          subsequent page. If unspecified, the first page will be returned.

        :returns: Iterator over :class:`KnowledgeAssistant`
        

    .. py:method:: list_knowledge_sources(parent: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[KnowledgeSource]

        Lists Knowledge Sources under a Knowledge Assistant.

        :param parent: str
          Parent resource to list from. Format: knowledge-assistants/{knowledge_assistant_id}
        :param page_size: int (optional)
        :param page_token: str (optional)

        :returns: Iterator over :class:`KnowledgeSource`
        

    .. py:method:: set_permissions(knowledge_assistant_id: str [, access_control_list: Optional[List[KnowledgeAssistantAccessControlRequest]]]) -> KnowledgeAssistantPermissions

        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.
        :param access_control_list: List[:class:`KnowledgeAssistantAccessControlRequest`] (optional)

        :returns: :class:`KnowledgeAssistantPermissions`
        

    .. py:method:: sync_knowledge_sources(name: str)

        Sync all non-index Knowledge Sources for a Knowledge Assistant (index sources do not require sync)

        :param name: str
          The resource name of the Knowledge Assistant. Format: knowledge-assistants/{knowledge_assistant_id}


        

    .. py:method:: update_knowledge_assistant(name: str, knowledge_assistant: KnowledgeAssistant, update_mask: FieldMask) -> KnowledgeAssistant

        Updates a Knowledge Assistant.

        :param name: str
          The resource name of the Knowledge Assistant. Format: knowledge-assistants/{knowledge_assistant_id}
        :param knowledge_assistant: :class:`KnowledgeAssistant`
          The Knowledge Assistant update payload. Only fields listed in update_mask are updated. REQUIRED
          annotations on Knowledge Assistant fields describe create-time requirements and do not mean all
          those fields are required for update.
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the Knowledge Assistant. Allowed values: `display_name`,
          `description`, `instructions`. Examples: - `display_name` - `description,instructions`

        :returns: :class:`KnowledgeAssistant`
        

    .. py:method:: update_knowledge_source(name: str, knowledge_source: KnowledgeSource, update_mask: FieldMask) -> KnowledgeSource

        Updates a Knowledge Source.

        :param name: str
          The resource name of the Knowledge Source to update. Format:
          knowledge-assistants/{knowledge_assistant_id}/knowledge-sources/{knowledge_source_id}
        :param knowledge_source: :class:`KnowledgeSource`
          The Knowledge Source update payload. Only fields listed in update_mask are updated. REQUIRED
          annotations on Knowledge Source fields describe create-time requirements and do not mean all those
          fields are required for update.
        :param update_mask: FieldMask
          Comma-delimited list of fields to update on the Knowledge Source. Allowed values: `display_name`,
          `description`. Examples: - `display_name` - `display_name,description`

        :returns: :class:`KnowledgeSource`
        

    .. py:method:: update_permissions(knowledge_assistant_id: str [, access_control_list: Optional[List[KnowledgeAssistantAccessControlRequest]]]) -> KnowledgeAssistantPermissions

        Updates the permissions on a knowledge assistant. Knowledge assistants can inherit permissions from
        their root object.

        :param knowledge_assistant_id: str
          The knowledge assistant for which to get or manage permissions.
        :param access_control_list: List[:class:`KnowledgeAssistantAccessControlRequest`] (optional)

        :returns: :class:`KnowledgeAssistantPermissions`
        