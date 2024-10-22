``a.budgets``: Budgets
======================
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
            
            created = a.budgets.create(budget=billing.CreateBudgetConfigurationBudget(
                display_name=f'sdk-{time.time_ns()}',
                filter=billing.BudgetConfigurationFilter(tags=[
                    billing.BudgetConfigurationFilterTagClause(key="tagName",
                                                               value=billing.BudgetConfigurationFilterClause(
                                                                   operator=billing.BudgetConfigurationFilterOperator.IN,
                                                                   values=["all"]))
                ]),
                alert_configurations=[
                    billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                        time_period=billing.AlertConfigurationTimePeriod.MONTH,
                        quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                        trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                        quantity_threshold="100",
                        action_configurations=[
                            billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                target="admin@example.com")
                        ])
                ]))
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

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
            
            created = a.budgets.create(budget=billing.CreateBudgetConfigurationBudget(
                display_name=f'sdk-{time.time_ns()}',
                filter=billing.BudgetConfigurationFilter(tags=[
                    billing.BudgetConfigurationFilterTagClause(key="tagName",
                                                               value=billing.BudgetConfigurationFilterClause(
                                                                   operator=billing.BudgetConfigurationFilterOperator.IN,
                                                                   values=["all"]))
                ]),
                alert_configurations=[
                    billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                        time_period=billing.AlertConfigurationTimePeriod.MONTH,
                        quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                        trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                        quantity_threshold="100",
                        action_configurations=[
                            billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                target="admin@example.com")
                        ])
                ]))
            
            by_id = a.budgets.get(budget_id=created.budget.budget_configuration_id)
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

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
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            all = a.budgets.list(billing.ListBudgetConfigurationsRequest())

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
            
            created = a.budgets.create(budget=billing.CreateBudgetConfigurationBudget(
                display_name=f'sdk-{time.time_ns()}',
                filter=billing.BudgetConfigurationFilter(tags=[
                    billing.BudgetConfigurationFilterTagClause(key="tagName",
                                                               value=billing.BudgetConfigurationFilterClause(
                                                                   operator=billing.BudgetConfigurationFilterOperator.IN,
                                                                   values=["all"]))
                ]),
                alert_configurations=[
                    billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                        time_period=billing.AlertConfigurationTimePeriod.MONTH,
                        quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                        trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                        quantity_threshold="100",
                        action_configurations=[
                            billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                target="admin@example.com")
                        ])
                ]))
            
            _ = a.budgets.update(
                budget_id=created.budget.budget_configuration_id,
                budget=billing.UpdateBudgetConfigurationBudget(
                    budget_configuration_id=created.budget.budget_configuration_id,
                    display_name=f'sdk-{time.time_ns()}',
                    filter=billing.BudgetConfigurationFilter(tags=[
                        billing.BudgetConfigurationFilterTagClause(
                            key="tagName",
                            value=billing.BudgetConfigurationFilterClause(
                                operator=billing.BudgetConfigurationFilterOperator.IN, values=["all"]))
                    ]),
                    alert_configurations=[
                        billing.AlertConfiguration(
                            alert_configuration_id=created.budget.alert_configurations[0].alert_configuration_id,
                            time_period=billing.AlertConfigurationTimePeriod.MONTH,
                            quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                            trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                            quantity_threshold="50",
                            action_configurations=created.budget.alert_configurations[0].action_configurations)
                    ]))
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

        Modify budget.
        
        Modifies a budget in this account. Budget properties are completely overwritten.
        
        :param budget_id: str
          Budget ID
        :param budget: :class:`Budget`
          Budget configuration to be created.
        
        
        