``a.budgets``: Budgets
======================
.. currentmodule:: databricks.sdk.service.billing

.. py:class:: BudgetsAPI

    These APIs manage budget configurations for this account. Budgets enable you to monitor usage across your
    account. You can set up budgets to either track account-wide spending, or apply filters to track the
    spending of specific teams, projects, or workspaces.

    .. py:method:: create(budget: CreateBudgetConfigurationBudget) -> CreateBudgetConfigurationResponse


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

        Create new budget.
        
        Create a new budget configuration for an account. For full details, see
        https://docs.databricks.com/en/admin/account-settings/budgets.html.
        
        :param budget: :class:`CreateBudgetConfigurationBudget`
          Properties of the new budget configuration.
        
        :returns: :class:`CreateBudgetConfigurationResponse`
        

    .. py:method:: delete(budget_id: str)

        Delete budget.
        
        Deletes a budget configuration for an account. Both account and budget configuration are specified by
        ID. This cannot be undone.
        
        :param budget_id: str
          The Databricks budget configuration ID.
        
        
        

    .. py:method:: get(budget_id: str) -> GetBudgetConfigurationResponse


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

        Get budget.
        
        Gets a budget configuration for an account. Both account and budget configuration are specified by ID.
        
        :param budget_id: str
          The Databricks budget configuration ID.
        
        :returns: :class:`GetBudgetConfigurationResponse`
        

    .. py:method:: list( [, page_token: Optional[str]]) -> Iterator[BudgetConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            all = a.budgets.list(billing.ListBudgetConfigurationsRequest())

        Get all budgets.
        
        Gets all budgets associated with this account.
        
        :param page_token: str (optional)
          A page token received from a previous get all budget configurations call. This token can be used to
          retrieve the subsequent page. Requests first page if absent.
        
        :returns: Iterator over :class:`BudgetConfiguration`
        

    .. py:method:: update(budget_id: str, budget: UpdateBudgetConfigurationBudget) -> UpdateBudgetConfigurationResponse


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
        
        Updates a budget configuration for an account. Both account and budget configuration are specified by
        ID.
        
        :param budget_id: str
          The Databricks budget configuration ID.
        :param budget: :class:`UpdateBudgetConfigurationBudget`
          The updated budget. This will overwrite the budget specified by the budget ID.
        
        :returns: :class:`UpdateBudgetConfigurationResponse`
        