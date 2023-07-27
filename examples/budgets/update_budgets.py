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
