---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - billing
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>budgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="budgets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.budgets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="budgets_get"
    values={[
        { label: 'budgets_get', value: 'budgets_get' },
        { label: 'budgets_list', value: 'budgets_list' }
    ]}
>
<TabItem value="budgets_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_configuration_id",
    "type": "string",
    "description": "Databricks budget configuration ID."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable name of budget configuration. Max Length: 128"
  },
  {
    "name": "alert_configurations",
    "type": "array",
    "description": "Alerts to configure when this budget is in a triggered state. Budgets must have exactly one alert configuration.",
    "children": [
      {
        "name": "action_configurations",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "action_configuration_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "action_type",
            "type": "string",
            "description": "The type of the action. (EMAIL_NOTIFICATION)"
          },
          {
            "name": "target",
            "type": "string",
            "description": "Target for the action. For example, an email address."
          }
        ]
      },
      {
        "name": "alert_configuration_id",
        "type": "string",
        "description": "Databricks alert configuration ID."
      },
      {
        "name": "quantity_threshold",
        "type": "string",
        "description": "The threshold for the budget alert to determine if it is in a triggered state. The number is evaluated based on `quantity_type`."
      },
      {
        "name": "quantity_type",
        "type": "string",
        "description": "The way to calculate cost for this budget alert. This is what `quantity_threshold` is measured in. (LIST_PRICE_DOLLARS_USD)"
      },
      {
        "name": "time_period",
        "type": "string",
        "description": "The time window of usage data for the budget. (MONTH)"
      },
      {
        "name": "trigger_type",
        "type": "string",
        "description": "The evaluation method to determine when this budget alert is in a triggered state. (CUMULATIVE_SPENDING_EXCEEDED)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "integer",
    "description": "Creation time of this budget configuration."
  },
  {
    "name": "filter",
    "type": "object",
    "description": "Configured filters for this budget. These are applied to your account's usage to limit the scope of what is considered for this budget. Leave empty to include all usage for this account. All provided filters must be matched for usage to be included.",
    "children": [
      {
        "name": "tags",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "operator",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN)"
              },
              {
                "name": "values",
                "type": "array",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "workspace_id",
        "type": "object",
        "description": "If provided, usage must match with the provided Databricks workspace IDs.",
        "children": [
          {
            "name": "operator",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN)"
          },
          {
            "name": "values",
            "type": "array",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "integer",
    "description": "Update time of this budget configuration."
  }
]} />
</TabItem>
<TabItem value="budgets_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_configuration_id",
    "type": "string",
    "description": "Databricks budget configuration ID."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable name of budget configuration. Max Length: 128"
  },
  {
    "name": "alert_configurations",
    "type": "array",
    "description": "Alerts to configure when this budget is in a triggered state. Budgets must have exactly one alert configuration.",
    "children": [
      {
        "name": "action_configurations",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "action_configuration_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "action_type",
            "type": "string",
            "description": "The type of the action. (EMAIL_NOTIFICATION)"
          },
          {
            "name": "target",
            "type": "string",
            "description": "Target for the action. For example, an email address."
          }
        ]
      },
      {
        "name": "alert_configuration_id",
        "type": "string",
        "description": "Databricks alert configuration ID."
      },
      {
        "name": "quantity_threshold",
        "type": "string",
        "description": "The threshold for the budget alert to determine if it is in a triggered state. The number is evaluated based on `quantity_type`."
      },
      {
        "name": "quantity_type",
        "type": "string",
        "description": "The way to calculate cost for this budget alert. This is what `quantity_threshold` is measured in. (LIST_PRICE_DOLLARS_USD)"
      },
      {
        "name": "time_period",
        "type": "string",
        "description": "The time window of usage data for the budget. (MONTH)"
      },
      {
        "name": "trigger_type",
        "type": "string",
        "description": "The evaluation method to determine when this budget alert is in a triggered state. (CUMULATIVE_SPENDING_EXCEEDED)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "integer",
    "description": "Creation time of this budget configuration."
  },
  {
    "name": "filter",
    "type": "object",
    "description": "Configured filters for this budget. These are applied to your account's usage to limit the scope of what is considered for this budget. Leave empty to include all usage for this account. All provided filters must be matched for usage to be included.",
    "children": [
      {
        "name": "tags",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "operator",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN)"
              },
              {
                "name": "values",
                "type": "array",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "workspace_id",
        "type": "object",
        "description": "If provided, usage must match with the provided Databricks workspace IDs.",
        "children": [
          {
            "name": "operator",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN)"
          },
          {
            "name": "values",
            "type": "array",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "integer",
    "description": "Update time of this budget configuration."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#budgets_get"><CopyableCode code="budgets_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-budget_id"><code>budget_id</code></a></td>
    <td></td>
    <td>Gets a budget configuration for an account. Both account and budget configuration are specified by ID.</td>
</tr>
<tr>
    <td><a href="#budgets_list"><CopyableCode code="budgets_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets all budgets associated with this account.</td>
</tr>
<tr>
    <td><a href="#budgets_create"><CopyableCode code="budgets_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-budget"><code>budget</code></a></td>
    <td></td>
    <td>Create a new budget configuration for an account. For full details, see</td>
</tr>
<tr>
    <td><a href="#budgets_update"><CopyableCode code="budgets_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-budget_id"><code>budget_id</code></a>, <a href="#parameter-budget"><code>budget</code></a></td>
    <td></td>
    <td>Updates a budget configuration for an account. Both account and budget configuration are specified by</td>
</tr>
<tr>
    <td><a href="#budgets_delete"><CopyableCode code="budgets_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-budget_id"><code>budget_id</code></a></td>
    <td></td>
    <td>Deletes a budget configuration for an account. Both account and budget configuration are specified by</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-budget_id">
    <td><CopyableCode code="budget_id" /></td>
    <td><code>string</code></td>
    <td>The Databricks budget configuration ID.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token received from a previous get all budget configurations call. This token can be used to retrieve the subsequent page. Requests first page if absent.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="budgets_get"
    values={[
        { label: 'budgets_get', value: 'budgets_get' },
        { label: 'budgets_list', value: 'budgets_list' }
    ]}
>
<TabItem value="budgets_get">

Gets a budget configuration for an account. Both account and budget configuration are specified by ID.

```sql
SELECT
account_id,
budget_configuration_id,
display_name,
alert_configurations,
create_time,
filter,
update_time
FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}' -- required
AND budget_id = '{{ budget_id }}' -- required
;
```
</TabItem>
<TabItem value="budgets_list">

Gets all budgets associated with this account.

```sql
SELECT
account_id,
budget_configuration_id,
display_name,
alert_configurations,
create_time,
filter,
update_time
FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}' -- required
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="budgets_create"
    values={[
        { label: 'budgets_create', value: 'budgets_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="budgets_create">

Create a new budget configuration for an account. For full details, see

```sql
INSERT INTO databricks_account.billing.budgets (
budget,
account_id
)
SELECT 
'{{ budget }}' /* required */,
'{{ account_id }}'
RETURNING
budget
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: budgets
  props:
    - name: account_id
      value: string
      description: Required parameter for the budgets resource.
    - name: budget
      value: object
      description: |
        Properties of the new budget configuration.
      props:
      - name: account_id
        value: string
      - name: alert_configurations
        value: array
        description: |
          Alerts to configure when this budget is in a triggered state. Budgets must have exactly one alert configuration.
        props:
        - name: action_configurations
          value: array
          props:
          - name: action_type
            value: string
            description: |
              Create a collection of name/value pairs.
              Example enumeration:
              >>> class Color(Enum):
              ...     RED = 1
              ...     BLUE = 2
              ...     GREEN = 3
              Access them by:
              - attribute access::
              >>> Color.RED
              <Color.RED: 1>
              - value lookup:
              >>> Color(1)
              <Color.RED: 1>
              - name lookup:
              >>> Color['RED']
              <Color.RED: 1>
              Enumerations can be iterated over, and know how many members they have:
              >>> len(Color)
              3
              >>> list(Color)
              [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
              Methods can be added to enumerations, and members can have their own
              attributes -- see the documentation for details.
          - name: target
            value: string
            description: |
              Target for the action. For example, an email address.
        - name: quantity_threshold
          value: string
          description: |
            The threshold for the budget alert to determine if it is in a triggered state. The number is evaluated based on `quantity_type`.
        - name: quantity_type
          value: string
          description: |
            The way to calculate cost for this budget alert. This is what `quantity_threshold` is measured in.
        - name: time_period
          value: string
          description: |
            The time window of usage data for the budget.
        - name: trigger_type
          value: string
          description: |
            The evaluation method to determine when this budget alert is in a triggered state.
      - name: display_name
        value: string
        description: |
          Human-readable name of budget configuration. Max Length: 128
      - name: filter
        value: object
        description: |
          Configured filters for this budget. These are applied to your account's usage to limit the scope of what is considered for this budget. Leave empty to include all usage for this account. All provided filters must be matched for usage to be included.
        props:
        - name: tags
          value: array
          props:
          - name: key
            value: string
          - name: value
            value: object
            props:
            - name: operator
              value: string
              description: |
                Create a collection of name/value pairs.
                Example enumeration:
                >>> class Color(Enum):
                ...     RED = 1
                ...     BLUE = 2
                ...     GREEN = 3
                Access them by:
                - attribute access::
                >>> Color.RED
                <Color.RED: 1>
                - value lookup:
                >>> Color(1)
                <Color.RED: 1>
                - name lookup:
                >>> Color['RED']
                <Color.RED: 1>
                Enumerations can be iterated over, and know how many members they have:
                >>> len(Color)
                3
                >>> list(Color)
                [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
                Methods can be added to enumerations, and members can have their own
                attributes -- see the documentation for details.
            - name: values
              value: array
        - name: workspace_id
          value: object
          description: |
            If provided, usage must match with the provided Databricks workspace IDs.
          props:
          - name: operator
            value: string
            description: |
              Create a collection of name/value pairs.
              Example enumeration:
              >>> class Color(Enum):
              ...     RED = 1
              ...     BLUE = 2
              ...     GREEN = 3
              Access them by:
              - attribute access::
              >>> Color.RED
              <Color.RED: 1>
              - value lookup:
              >>> Color(1)
              <Color.RED: 1>
              - name lookup:
              >>> Color['RED']
              <Color.RED: 1>
              Enumerations can be iterated over, and know how many members they have:
              >>> len(Color)
              3
              >>> list(Color)
              [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
              Methods can be added to enumerations, and members can have their own
              attributes -- see the documentation for details.
          - name: values
            value: array
            items:
              type: integer
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="budgets_update"
    values={[
        { label: 'budgets_update', value: 'budgets_update' }
    ]}
>
<TabItem value="budgets_update">

Updates a budget configuration for an account. Both account and budget configuration are specified by

```sql
REPLACE databricks_account.billing.budgets
SET 
budget = '{{ budget }}'
WHERE 
account_id = '{{ account_id }}' --required
AND budget_id = '{{ budget_id }}' --required
AND budget = '{{ budget }}' --required
RETURNING
budget;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="budgets_delete"
    values={[
        { label: 'budgets_delete', value: 'budgets_delete' }
    ]}
>
<TabItem value="budgets_delete">

Deletes a budget configuration for an account. Both account and budget configuration are specified by

```sql
DELETE FROM databricks_account.billing.budgets
WHERE account_id = '{{ account_id }}' --required
AND budget_id = '{{ budget_id }}' --required
;
```
</TabItem>
</Tabs>
