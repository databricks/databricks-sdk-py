``w.clean_room_auto_approval_rules``: Auto-approval Rules
=========================================================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomAutoApprovalRulesAPI

    Clean room auto-approval rules automatically create an approval on your behalf when an asset (e.g.
    notebook) meeting specific criteria is shared in a clean room.

    .. py:method:: create(clean_room_name: str, auto_approval_rule: CleanRoomAutoApprovalRule) -> CleanRoomAutoApprovalRule

        Create an auto-approval rule
        
        :param clean_room_name: str
          The name of the clean room this auto-approval rule belongs to.
        :param auto_approval_rule: :class:`CleanRoomAutoApprovalRule`
        
        :returns: :class:`CleanRoomAutoApprovalRule`
        

    .. py:method:: delete(clean_room_name: str, rule_id: str)

        Delete a auto-approval rule by rule ID
        
        :param clean_room_name: str
        :param rule_id: str
        
        
        

    .. py:method:: get(clean_room_name: str, rule_id: str) -> CleanRoomAutoApprovalRule

        Get a auto-approval rule by rule ID
        
        :param clean_room_name: str
        :param rule_id: str
        
        :returns: :class:`CleanRoomAutoApprovalRule`
        

    .. py:method:: list(clean_room_name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CleanRoomAutoApprovalRule]

        List all auto-approval rules for the caller
        
        :param clean_room_name: str
        :param page_size: int (optional)
          Maximum number of auto-approval rules to return. Defaults to 100.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`CleanRoomAutoApprovalRule`
        

    .. py:method:: update(clean_room_name: str, rule_id: str, auto_approval_rule: CleanRoomAutoApprovalRule) -> CleanRoomAutoApprovalRule

        Update a auto-approval rule by rule ID
        
        :param clean_room_name: str
          The name of the clean room this auto-approval rule belongs to.
        :param rule_id: str
          A generated UUID identifying the rule.
        :param auto_approval_rule: :class:`CleanRoomAutoApprovalRule`
          The auto-approval rule to update. The rule_id field is used to identify the rule to update.
        
        :returns: :class:`CleanRoomAutoApprovalRule`
        