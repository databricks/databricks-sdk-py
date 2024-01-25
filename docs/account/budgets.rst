Budgets
=======
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: BudgetsAPI

    These APIs manage budget configuration including notifications for exceeding a budget for a period. They
    can also retrieve the status of each budget.

    .. py:method:: create(budget: Budget) -> WrappedBudgetWithStatus


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            created = a.budgets.create(budget=billing.Budget(
                name=f'sdk-{time.time_ns()}',
                filter="tag.tagName = 'all'",
                period="1 month",
                start_date="2022-01-01",
                target_amount="100",
                alerts=[billing.BudgetAlert(email_notifications=["admin@example.com"], min_percentage=50)]))
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_id)

        Create a new budget.
        
        Creates a new budget in the specified account.
        
        :param budget: :class:`Budget`
          Budget configuration to be created.
        
        :returns: :class:`WrappedBudgetWithStatus`
        

    .. py:method:: delete(budget_id: str)

        Delete budget.
        
        Deletes the budget specified by its UUID.
        
        :param budget_id: str
          Budget ID
        
        
        

    .. py:method:: get(budget_id: str) -> WrappedBudgetWithStatus


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            created = a.budgets.create(budget=billing.Budget(
                name=f'sdk-{time.time_ns()}',
                filter="tag.tagName = 'all'",
                period="1 month",
                start_date="2022-01-01",
                target_amount="100",
                alerts=[billing.BudgetAlert(email_notifications=["admin@example.com"], min_percentage=50)]))
            
            by_id = a.budgets.get(budget_id=created.budget.budget_id)
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_id)

        Get budget and its status.
        
        Gets the budget specified by its UUID, including noncumulative status for each day that the budget is
        configured to include.
        
        :param budget_id: str
          Budget ID
        
        :returns: :class:`WrappedBudgetWithStatus`
        

    .. py:method:: list() -> Iterator[BudgetWithStatus]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            
            a = AccountClient()
            
            all = a.budgets.list()

        Get all budgets.
        
        Gets all budgets associated with this account, including noncumulative status for each day that the
        budget is configured to include.
        
        :returns: Iterator over :class:`BudgetWithStatus`
        

    .. py:method:: update(budget_id: str, budget: Budget)


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            created = a.budgets.create(budget=billing.Budget(
                name=f'sdk-{time.time_ns()}',
                filter="tag.tagName = 'all'",
                period="1 month",
                start_date="2022-01-01",
                target_amount="100",
                alerts=[billing.BudgetAlert(email_notifications=["admin@example.com"], min_percentage=50)]))
            
            a.budgets.update(budget_id=created.budget.budget_id,
                             budget=billing.Budget(name=f'sdk-{time.time_ns()}',
                                                   filter="tag.tagName = 'all'",
                                                   period="1 month",
                                                   start_date="2022-01-01",
                                                   target_amount="100",
                                                   alerts=[
                                                       billing.BudgetAlert(email_notifications=["admin@example.com"],
                                                                           min_percentage=70)
                                                   ]))
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_id)

        Modify budget.
        
        Modifies a budget in this account. Budget properties are completely overwritten.
        
        :param budget_id: str
          Budget ID
        :param budget: :class:`Budget`
          Budget configuration to be created.
        
        
        