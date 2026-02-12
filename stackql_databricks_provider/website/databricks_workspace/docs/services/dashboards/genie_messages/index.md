---
title: genie_messages
hide_title: false
hide_table_of_contents: false
keywords:
  - genie_messages
  - dashboards
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>genie_messages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>genie_messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dashboards.genie_messages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_query_result_by_attachment"
    values={[
        { label: 'get_query_result_by_attachment', value: 'get_query_result_by_attachment' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_query_result_by_attachment">

<SchemaTable fields={[
  {
    "name": "statement_response",
    "type": "string",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "conversation_id",
    "type": "string",
    "description": "Conversation ID"
  },
  {
    "name": "message_id",
    "type": "string",
    "description": "Message ID"
  },
  {
    "name": "space_id",
    "type": "string",
    "description": "Genie space ID"
  },
  {
    "name": "user_id",
    "type": "integer",
    "description": "ID of the user who created the message"
  },
  {
    "name": "attachments",
    "type": "array",
    "description": "AI-generated response to the message",
    "children": [
      {
        "name": "attachment_id",
        "type": "string",
        "description": "Attachment ID"
      },
      {
        "name": "query",
        "type": "object",
        "description": "Query Attachment if Genie responds with a SQL query",
        "children": [
          {
            "name": "description",
            "type": "string",
            "description": ""
          },
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "last_updated_timestamp",
            "type": "integer",
            "description": "Time when the user updated the query last"
          },
          {
            "name": "parameters",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "keyword",
                "type": "string",
                "description": ""
              },
              {
                "name": "sql_type",
                "type": "string",
                "description": ""
              },
              {
                "name": "value",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "query",
            "type": "string",
            "description": "AI generated SQL query"
          },
          {
            "name": "query_result_metadata",
            "type": "object",
            "description": "Metadata associated with the query result.",
            "children": [
              {
                "name": "is_truncated",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "row_count",
                "type": "integer",
                "description": "The number of rows in the result set."
              }
            ]
          },
          {
            "name": "statement_id",
            "type": "string",
            "description": "Statement Execution API statement id. Use [Get status, manifest, and result first chunk](:method:statementexecution/getstatement) to get the full result data."
          },
          {
            "name": "title",
            "type": "string",
            "description": "Name of the query"
          }
        ]
      },
      {
        "name": "suggested_questions",
        "type": "object",
        "description": "Follow-up questions suggested by Genie",
        "children": [
          {
            "name": "questions",
            "type": "array",
            "description": "The suggested follow-up questions"
          }
        ]
      },
      {
        "name": "text",
        "type": "object",
        "description": "Text Attachment if Genie responds with text. This also contains the final summary when available.",
        "children": [
          {
            "name": "content",
            "type": "string",
            "description": ""
          },
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "purpose",
            "type": "string",
            "description": "Purpose/intent of this text attachment"
          }
        ]
      }
    ]
  },
  {
    "name": "content",
    "type": "string",
    "description": "User message content"
  },
  {
    "name": "created_timestamp",
    "type": "integer",
    "description": "Timestamp when the message was created"
  },
  {
    "name": "error",
    "type": "object",
    "description": "Error message if Genie failed to respond to the message",
    "children": [
      {
        "name": "error",
        "type": "string",
        "description": ""
      },
      {
        "name": "type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
      }
    ]
  },
  {
    "name": "feedback",
    "type": "object",
    "description": "User feedback for the message if provided",
    "children": [
      {
        "name": "rating",
        "type": "string",
        "description": "The feedback rating"
      }
    ]
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "Timestamp when the message was last updated"
  },
  {
    "name": "query_result",
    "type": "object",
    "description": "The result of SQL query if the message includes a query attachment. Deprecated. Use `query_result_metadata` in `GenieQueryAttachment` instead.",
    "children": [
      {
        "name": "is_truncated",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "row_count",
        "type": "integer",
        "description": "Row count of the result"
      },
      {
        "name": "statement_id",
        "type": "string",
        "description": "Statement Execution API statement id. Use [Get status, manifest, and result first chunk](:method:statementexecution/getstatement) to get the full result data."
      },
      {
        "name": "statement_id_signature",
        "type": "string",
        "description": "JWT corresponding to the statement contained in this result"
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "MessageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data<br />sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *<br />`ASKING_AI`: Waiting for the LLM to respond to the user's question. * `PENDING_WAREHOUSE`:<br />Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing a<br />generated SQL query. Get the SQL query result by calling<br />[getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *<br />`FAILED`: The response generation or query execution failed. See `error` field. * `COMPLETED`:<br />Message processing is completed. Results are in the `attachments` field. Get the SQL query<br />result by calling<br />[getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *<br />`SUBMITTED`: Message has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available<br />anymore. The user needs to rerun the query. Rerun the SQL query result by calling<br />[executeMessageAttachmentQuery](:method:genie/executeMessageAttachmentQuery) API. * `CANCELLED`:<br />Message has been cancelled."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "messages",
    "type": "array",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      },
      {
        "name": "space_id",
        "type": "string",
        "description": "Genie space ID"
      },
      {
        "name": "conversation_id",
        "type": "string",
        "description": "Conversation ID"
      },
      {
        "name": "content",
        "type": "string",
        "description": "User message content"
      },
      {
        "name": "message_id",
        "type": "string",
        "description": "Message ID"
      },
      {
        "name": "attachments",
        "type": "array",
        "description": "AI-generated response to the message",
        "children": [
          {
            "name": "attachment_id",
            "type": "string",
            "description": "Attachment ID"
          },
          {
            "name": "query",
            "type": "object",
            "description": "Query Attachment if Genie responds with a SQL query",
            "children": [
              {
                "name": "description",
                "type": "string",
                "description": ""
              },
              {
                "name": "id",
                "type": "string",
                "description": ""
              },
              {
                "name": "last_updated_timestamp",
                "type": "integer",
                "description": "Time when the user updated the query last"
              },
              {
                "name": "parameters",
                "type": "array",
                "description": ""
              },
              {
                "name": "query",
                "type": "string",
                "description": "AI generated SQL query"
              },
              {
                "name": "query_result_metadata",
                "type": "object",
                "description": "Metadata associated with the query result."
              },
              {
                "name": "statement_id",
                "type": "string",
                "description": "Statement Execution API statement id. Use [Get status, manifest, and result first chunk](:method:statementexecution/getstatement) to get the full result data."
              },
              {
                "name": "title",
                "type": "string",
                "description": "Name of the query"
              }
            ]
          },
          {
            "name": "suggested_questions",
            "type": "object",
            "description": "Follow-up questions suggested by Genie",
            "children": [
              {
                "name": "questions",
                "type": "array",
                "description": "The suggested follow-up questions"
              }
            ]
          },
          {
            "name": "text",
            "type": "object",
            "description": "Text Attachment if Genie responds with text. This also contains the final summary when available.",
            "children": [
              {
                "name": "content",
                "type": "string",
                "description": ""
              },
              {
                "name": "id",
                "type": "string",
                "description": ""
              },
              {
                "name": "purpose",
                "type": "string",
                "description": "Purpose/intent of this text attachment"
              }
            ]
          }
        ]
      },
      {
        "name": "created_timestamp",
        "type": "integer",
        "description": "Timestamp when the message was created"
      },
      {
        "name": "error",
        "type": "object",
        "description": "Error message if Genie failed to respond to the message",
        "children": [
          {
            "name": "error",
            "type": "string",
            "description": ""
          },
          {
            "name": "type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details."
          }
        ]
      },
      {
        "name": "feedback",
        "type": "object",
        "description": "User feedback for the message if provided",
        "children": [
          {
            "name": "rating",
            "type": "string",
            "description": "The feedback rating"
          }
        ]
      },
      {
        "name": "last_updated_timestamp",
        "type": "integer",
        "description": "Timestamp when the message was last updated"
      },
      {
        "name": "query_result",
        "type": "object",
        "description": "The result of SQL query if the message includes a query attachment. Deprecated. Use `query_result_metadata` in `GenieQueryAttachment` instead.",
        "children": [
          {
            "name": "is_truncated",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "row_count",
            "type": "integer",
            "description": "Row count of the result"
          },
          {
            "name": "statement_id",
            "type": "string",
            "description": "Statement Execution API statement id. Use [Get status, manifest, and result first chunk](:method:statementexecution/getstatement) to get the full result data."
          },
          {
            "name": "statement_id_signature",
            "type": "string",
            "description": "JWT corresponding to the statement contained in this result"
          }
        ]
      },
      {
        "name": "status",
        "type": "string",
        "description": "MessageStatus. The possible values are: * `FETCHING_METADATA`: Fetching metadata from the data<br />sources. * `FILTERING_CONTEXT`: Running smart context step to determine relevant context. *<br />`ASKING_AI`: Waiting for the LLM to respond to the user's question. * `PENDING_WAREHOUSE`:<br />Waiting for warehouse before the SQL query can start executing. * `EXECUTING_QUERY`: Executing a<br />generated SQL query. Get the SQL query result by calling<br />[getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *<br />`FAILED`: The response generation or query execution failed. See `error` field. * `COMPLETED`:<br />Message processing is completed. Results are in the `attachments` field. Get the SQL query<br />result by calling<br />[getMessageAttachmentQueryResult](:method:genie/getMessageAttachmentQueryResult) API. *<br />`SUBMITTED`: Message has been submitted. * `QUERY_RESULT_EXPIRED`: SQL result is not available<br />anymore. The user needs to rerun the query. Rerun the SQL query result by calling<br />[executeMessageAttachmentQuery](:method:genie/executeMessageAttachmentQuery) API. * `CANCELLED`:<br />Message has been cancelled."
      },
      {
        "name": "user_id",
        "type": "integer",
        "description": "ID of the user who created the message"
      }
    ]
  },
  {
    "name": "next_page_token",
    "type": "string",
    "description": "The token to use for retrieving the next page of results."
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
    <td><a href="#get_query_result_by_attachment"><CopyableCode code="get_query_result_by_attachment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-attachment_id"><code>attachment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get message from conversation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List messages in a conversation</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__content"><code>data__content</code></a></td>
    <td></td>
    <td>Create new message in a [conversation](:method:genie/startconversation). The AI response uses all</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Delete a conversation message.</td>
</tr>
<tr>
    <td><a href="#execute_query"><CopyableCode code="execute_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>DEPRECATED: Use [Execute Message Attachment Query](:method:genie/executemessageattachmentquery)</td>
</tr>
<tr>
    <td><a href="#get_query_result_deprecated"><CopyableCode code="get_query_result_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)</td>
</tr>
<tr>
    <td><a href="#send_feedback"><CopyableCode code="send_feedback" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-space_id"><code>space_id</code></a>, <a href="#parameter-conversation_id"><code>conversation_id</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-rating"><code>rating</code></a></td>
    <td></td>
    <td>Send feedback for a message.</td>
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
<tr id="parameter-attachment_id">
    <td><CopyableCode code="attachment_id" /></td>
    <td><code>string</code></td>
    <td>Attachment ID</td>
</tr>
<tr id="parameter-conversation_id">
    <td><CopyableCode code="conversation_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the conversation.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-message_id">
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the message to provide feedback for.</td>
</tr>
<tr id="parameter-space_id">
    <td><CopyableCode code="space_id" /></td>
    <td><code>string</code></td>
    <td>The ID associated with the Genie space where the message is located.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Maximum number of messages to return per page</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token to get the next page of results</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_query_result_by_attachment"
    values={[
        { label: 'get_query_result_by_attachment', value: 'get_query_result_by_attachment' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_query_result_by_attachment">

DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)

```sql
SELECT
statement_response
FROM databricks_workspace.dashboards.genie_messages
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND message_id = '{{ message_id }}' -- required
AND attachment_id = '{{ attachment_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get message from conversation.

```sql
SELECT
id,
conversation_id,
message_id,
space_id,
user_id,
attachments,
content,
created_timestamp,
error,
feedback,
last_updated_timestamp,
query_result,
status
FROM databricks_workspace.dashboards.genie_messages
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND message_id = '{{ message_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List messages in a conversation

```sql
SELECT
messages,
next_page_token
FROM databricks_workspace.dashboards.genie_messages
WHERE space_id = '{{ space_id }}' -- required
AND conversation_id = '{{ conversation_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create new message in a [conversation](:method:genie/startconversation). The AI response uses all

```sql
INSERT INTO databricks_workspace.dashboards.genie_messages (
data__content,
space_id,
conversation_id,
deployment_name
)
SELECT 
'{{ content }}' /* required */,
'{{ space_id }}',
'{{ conversation_id }}',
'{{ deployment_name }}'
RETURNING
id,
conversation_id,
message_id,
space_id,
user_id,
attachments,
content,
created_timestamp,
error,
feedback,
last_updated_timestamp,
query_result,
status
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: genie_messages
  props:
    - name: space_id
      value: string
      description: Required parameter for the genie_messages resource.
    - name: conversation_id
      value: string
      description: Required parameter for the genie_messages resource.
    - name: deployment_name
      value: string
      description: Required parameter for the genie_messages resource.
    - name: content
      value: string
      description: |
        User message content.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a conversation message.

```sql
DELETE FROM databricks_workspace.dashboards.genie_messages
WHERE space_id = '{{ space_id }}' --required
AND conversation_id = '{{ conversation_id }}' --required
AND message_id = '{{ message_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_query"
    values={[
        { label: 'execute_query', value: 'execute_query' },
        { label: 'get_query_result_deprecated', value: 'get_query_result_deprecated' },
        { label: 'send_feedback', value: 'send_feedback' }
    ]}
>
<TabItem value="execute_query">

DEPRECATED: Use [Execute Message Attachment Query](:method:genie/executemessageattachmentquery)

```sql
EXEC databricks_workspace.dashboards.genie_messages.execute_query 
@space_id='{{ space_id }}' --required, 
@conversation_id='{{ conversation_id }}' --required, 
@message_id='{{ message_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="get_query_result_deprecated">

DEPRECATED: Use [Get Message Attachment Query Result](:method:genie/getmessageattachmentqueryresult)

```sql
EXEC databricks_workspace.dashboards.genie_messages.get_query_result_deprecated 
@space_id='{{ space_id }}' --required, 
@conversation_id='{{ conversation_id }}' --required, 
@message_id='{{ message_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="send_feedback">

Send feedback for a message.

```sql
EXEC databricks_workspace.dashboards.genie_messages.send_feedback 
@space_id='{{ space_id }}' --required, 
@conversation_id='{{ conversation_id }}' --required, 
@message_id='{{ message_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"rating": "{{ rating }}"
}'
;
```
</TabItem>
</Tabs>
