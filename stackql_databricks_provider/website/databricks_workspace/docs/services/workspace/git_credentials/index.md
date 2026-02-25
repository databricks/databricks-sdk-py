---
title: git_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - git_credentials
  - workspace
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>git_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="git_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.git_credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "the name of the git credential, used for identification and ease of lookup"
  },
  {
    "name": "credential_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "git_email",
    "type": "string",
    "description": "The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit. Learn more at https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider"
  },
  {
    "name": "git_provider",
    "type": "string",
    "description": "The Git provider associated with the credential."
  },
  {
    "name": "git_username",
    "type": "string",
    "description": "The username provided with your Git provider account and associated with the credential. For most Git providers it is only used to set the Git committer & author names for commits, however it may be required for authentication depending on your Git provider / token requirements. Required for AWS CodeCommit."
  },
  {
    "name": "is_default_for_provider",
    "type": "boolean",
    "description": "if the credential is the default for the given provider"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "the name of the git credential, used for identification and ease of lookup"
  },
  {
    "name": "credential_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "git_email",
    "type": "string",
    "description": "The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit. Learn more at https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider"
  },
  {
    "name": "git_provider",
    "type": "string",
    "description": "The Git provider associated with the credential."
  },
  {
    "name": "git_username",
    "type": "string",
    "description": "The username provided with your Git provider account and associated with the credential. For most Git providers it is only used to set the Git committer & author names for commits, however it may be required for authentication depending on your Git provider / token requirements. Required for AWS CodeCommit."
  },
  {
    "name": "is_default_for_provider",
    "type": "boolean",
    "description": "if the credential is the default for the given provider"
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Gets the Git credential with the specified credential ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Lists the calling user's Git credentials.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-git_provider"><code>git_provider</code></a></td>
    <td></td>
    <td>Creates a Git credential entry for the user. Only one Git credential per user is supported, so any</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-git_provider"><code>git_provider</code></a></td>
    <td></td>
    <td>Updates the specified Git credential.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Deletes the specified Git credential.</td>
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
<tr id="parameter-credential_id">
    <td><CopyableCode code="credential_id" /></td>
    <td><code>integer</code></td>
    <td>The ID for the corresponding credential to access.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>The ID of the service principal whose credentials will be modified. Only service principal managers can perform this action.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the Git credential with the specified credential ID.

```sql
SELECT
name,
credential_id,
git_email,
git_provider,
git_username,
is_default_for_provider
FROM databricks_workspace.workspace.git_credentials
WHERE credential_id = '{{ credential_id }}' -- required
AND workspace = '{{ workspace }}' -- required
AND principal_id = '{{ principal_id }}'
;
```
</TabItem>
<TabItem value="list">

Lists the calling user's Git credentials.

```sql
SELECT
name,
credential_id,
git_email,
git_provider,
git_username,
is_default_for_provider
FROM databricks_workspace.workspace.git_credentials
WHERE workspace = '{{ workspace }}' -- required
AND principal_id = '{{ principal_id }}'
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

Creates a Git credential entry for the user. Only one Git credential per user is supported, so any

```sql
INSERT INTO databricks_workspace.workspace.git_credentials (
git_provider,
git_email,
git_username,
is_default_for_provider,
name,
personal_access_token,
principal_id,
workspace
)
SELECT 
'{{ git_provider }}' /* required */,
'{{ git_email }}',
'{{ git_username }}',
{{ is_default_for_provider }},
'{{ name }}',
'{{ personal_access_token }}',
{{ principal_id }},
'{{ workspace }}'
RETURNING
name,
credential_id,
git_email,
git_provider,
git_username,
is_default_for_provider
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: git_credentials
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the git_credentials resource.
    - name: git_provider
      value: "{{ git_provider }}"
      description: |
        Git provider. This field is case-insensitive. The available Git providers are \`gitHub\`, \`bitbucketCloud\`, \`gitLab\`, \`azureDevOpsServices\`, \`gitHubEnterprise\`, \`bitbucketServer\`, \`gitLabEnterpriseEdition\` and \`awsCodeCommit\`.
    - name: git_email
      value: "{{ git_email }}"
      description: |
        The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit. Learn more at https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
    - name: git_username
      value: "{{ git_username }}"
      description: |
        The username provided with your Git provider account and associated with the credential. For most Git providers it is only used to set the Git committer & author names for commits, however it may be required for authentication depending on your Git provider / token requirements. Required for AWS CodeCommit.
    - name: is_default_for_provider
      value: {{ is_default_for_provider }}
      description: |
        if the credential is the default for the given provider
    - name: name
      value: "{{ name }}"
      description: |
        the name of the git credential, used for identification and ease of lookup
    - name: personal_access_token
      value: "{{ personal_access_token }}"
      description: |
        The personal access token used to authenticate to the corresponding Git provider. For certain providers, support may exist for other types of scoped access tokens. [Learn more]. [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html
    - name: principal_id
      value: {{ principal_id }}
      description: |
        The ID of the service principal whose credentials will be modified. Only service principal managers can perform this action.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the specified Git credential.

```sql
UPDATE databricks_workspace.workspace.git_credentials
SET 
git_provider = '{{ git_provider }}',
git_email = '{{ git_email }}',
git_username = '{{ git_username }}',
is_default_for_provider = {{ is_default_for_provider }},
name = '{{ name }}',
personal_access_token = '{{ personal_access_token }}',
principal_id = {{ principal_id }}
WHERE 
credential_id = '{{ credential_id }}' --required
AND workspace = '{{ workspace }}' --required
AND git_provider = '{{ git_provider }}' --required;
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

Deletes the specified Git credential.

```sql
DELETE FROM databricks_workspace.workspace.git_credentials
WHERE credential_id = '{{ credential_id }}' --required
AND workspace = '{{ workspace }}' --required
AND principal_id = '{{ principal_id }}'
;
```
</TabItem>
</Tabs>
