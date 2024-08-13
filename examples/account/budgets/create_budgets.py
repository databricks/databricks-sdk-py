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
