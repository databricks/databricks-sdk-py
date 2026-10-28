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
            
            created = a.budgets.create(
                budget=billing.CreateBudgetConfigurationBudget(
                    display_name=f"sdk-{time.time_ns()}",
                    filter=billing.BudgetConfigurationFilter(
                        tags=[
                            billing.BudgetConfigurationFilterTagClause(
                                key="tagName",
                                value=billing.BudgetConfigurationFilterClause(
                                    operator=billing.BudgetConfigurationFilterOperator.IN,
                                    values=["all"],
                                ),
                            )
                        ]
                    ),
                    alert_configurations=[
                        billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                            time_period=billing.AlertConfigurationTimePeriod.MONTH,
                            quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                            trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                            quantity_threshold="100",
                            action_configurations=[
                                billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                    action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                    target="admin@example.com",
                                )
                            ],
                        )
                    ],
                )
            )
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

        Create a new budget configuration for an account. For full details, see
        https://docs.databricks.com/en/admin/account-settings/budgets.html.

        :param budget: :class:`CreateBudgetConfigurationBudget`
          Properties of the new budget configuration.

        :returns: :class:`CreateBudgetConfigurationResponse`
        

    .. py:method:: delete(budget_id: str)

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
            
            created = a.budgets.create(
                budget=billing.CreateBudgetConfigurationBudget(
                    display_name=f"sdk-{time.time_ns()}",
                    filter=billing.BudgetConfigurationFilter(
                        tags=[
                            billing.BudgetConfigurationFilterTagClause(
                                key="tagName",
                                value=billing.BudgetConfigurationFilterClause(
                                    operator=billing.BudgetConfigurationFilterOperator.IN,
                                    values=["all"],
                                ),
                            )
                        ]
                    ),
                    alert_configurations=[
                        billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                            time_period=billing.AlertConfigurationTimePeriod.MONTH,
                            quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                            trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                            quantity_threshold="100",
                            action_configurations=[
                                billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                    action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                    target="admin@example.com",
                                )
                            ],
                        )
                    ],
                )
            )
            
            by_id = a.budgets.get(budget_id=created.budget.budget_configuration_id)
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

        Gets a budget configuration for an account. Both account and budget configuration are specified by ID.

        :param budget_id: str
          The budget configuration ID

        :returns: :class:`GetBudgetConfigurationResponse`
        

    .. py:method:: get_budget_spend_status(name: str) -> BudgetSpendStatus

        Get the calling user's live spend against the blocking thresholds of a single Unity Gateway budget.
        Any account user can call this for their own spend. Spend is reported in USD at list price and is
        near-real-time, so it may differ slightly from billing data. Returns NOT_FOUND if the budget doesn't
        exist or has no blocking thresholds.

        :param name: str
          The resource name of the budget spend status to read, of the form
          ``accounts/{account_id}/budget-spend-statuses/{budget_id}``. A ``budget_id`` that isn't a valid UUID
          fails with INVALID_PARAMETER_VALUE.

        :returns: :class:`BudgetSpendStatus`
        

    .. py:method:: list( [, page_token: Optional[str]]) -> Iterator[BudgetConfiguration]


        Usage:

        .. code-block::

            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            all = a.budgets.list(billing.ListBudgetConfigurationsRequest())

        Gets all budgets associated with this account.

        :param page_token: str (optional)
          A page token received from a previous get all budget configurations call. This token can be used to
          retrieve the subsequent page. Requests first page if absent.

        :returns: Iterator over :class:`BudgetConfiguration`
        

    .. py:method:: list_budget_spend_statuses(parent: str [, filter: Optional[str], page_size: Optional[int], page_token: Optional[str]]) -> ListBudgetSpendStatusesResponse

        List the calling user's live spend against the blocking thresholds across the account's Unity Gateway
        budgets. Any account user can call this for their own spend. Spend is reported in USD at list price
        and is near-real-time, so it may differ slightly from billing data. By default, returns every budget
        in the account that has a blocking threshold. Use ``filter`` to narrow results by workspace.

        :param parent: str
          The parent account whose budget spend statuses to list, of the form ``accounts/{account_id}``.
        :param filter: str (optional)
          A filter expression that narrows the returned budgets by workspace. Only ``workspace_id`` is
          supported, in lower case with numeric workspace IDs, for example ``workspace_id = 123`` or
          ``workspace_id IN (123, 456)``. Matches budgets that apply to any of the listed workspaces,
          including budgets that apply to all workspaces. Any other expression, such as an empty ``IN ()``
          list, fails with INVALID_PARAMETER_VALUE. If empty, returns every budget in the account that has a
          blocking threshold.
        :param page_size: int (optional)
          The maximum number of spend statuses to return per page. If unspecified or 0, at most 100 are
          returned. The maximum value is 100; values above 100 are coerced to 100. Negative values fail with
          INVALID_PARAMETER_VALUE. The server may return fewer results than requested, including zero, even
          when more pages remain; page until ``next_page_token`` is absent.
        :param page_token: str (optional)
          A page token from a previous ``ListBudgetSpendStatuses`` response, used to fetch the next page.
          Requests the first page if absent. All other request parameters except ``page_size`` must match the
          request that returned the token; otherwise the request fails with INVALID_PARAMETER_VALUE.

        :returns: :class:`ListBudgetSpendStatusesResponse`
        

    .. py:method:: update(budget_id: str, budget: UpdateBudgetConfigurationBudget) -> UpdateBudgetConfigurationResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import AccountClient
            from databricks.sdk.service import billing
            
            a = AccountClient()
            
            created = a.budgets.create(
                budget=billing.CreateBudgetConfigurationBudget(
                    display_name=f"sdk-{time.time_ns()}",
                    filter=billing.BudgetConfigurationFilter(
                        tags=[
                            billing.BudgetConfigurationFilterTagClause(
                                key="tagName",
                                value=billing.BudgetConfigurationFilterClause(
                                    operator=billing.BudgetConfigurationFilterOperator.IN,
                                    values=["all"],
                                ),
                            )
                        ]
                    ),
                    alert_configurations=[
                        billing.CreateBudgetConfigurationBudgetAlertConfigurations(
                            time_period=billing.AlertConfigurationTimePeriod.MONTH,
                            quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                            trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                            quantity_threshold="100",
                            action_configurations=[
                                billing.CreateBudgetConfigurationBudgetActionConfigurations(
                                    action_type=billing.ActionConfigurationType.EMAIL_NOTIFICATION,
                                    target="admin@example.com",
                                )
                            ],
                        )
                    ],
                )
            )
            
            _ = a.budgets.update(
                budget_id=created.budget.budget_configuration_id,
                budget=billing.UpdateBudgetConfigurationBudget(
                    budget_configuration_id=created.budget.budget_configuration_id,
                    display_name=f"sdk-{time.time_ns()}",
                    filter=billing.BudgetConfigurationFilter(
                        tags=[
                            billing.BudgetConfigurationFilterTagClause(
                                key="tagName",
                                value=billing.BudgetConfigurationFilterClause(
                                    operator=billing.BudgetConfigurationFilterOperator.IN,
                                    values=["all"],
                                ),
                            )
                        ]
                    ),
                    alert_configurations=[
                        billing.AlertConfiguration(
                            alert_configuration_id=created.budget.alert_configurations[0].alert_configuration_id,
                            time_period=billing.AlertConfigurationTimePeriod.MONTH,
                            quantity_type=billing.AlertConfigurationQuantityType.LIST_PRICE_DOLLARS_USD,
                            trigger_type=billing.AlertConfigurationTriggerType.CUMULATIVE_SPENDING_EXCEEDED,
                            quantity_threshold="50",
                            action_configurations=created.budget.alert_configurations[0].action_configurations,
                        )
                    ],
                ),
            )
            
            # cleanup
            a.budgets.delete(budget_id=created.budget.budget_configuration_id)

        Updates a budget configuration for an account. Both account and budget configuration are specified by
        ID.

        :param budget_id: str
          The Databricks budget configuration ID.
        :param budget: :class:`UpdateBudgetConfigurationBudget`
          The updated budget. This will overwrite the budget specified by the budget ID.

        :returns: :class:`UpdateBudgetConfigurationResponse`
        