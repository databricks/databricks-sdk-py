---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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

Creates, updates, deletes, gets or lists a <code>repos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="repos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.repos" /></td></tr>
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
    "name": "id",
    "type": "integer",
    "description": "ID of the Git folder (repo) object in the workspace."
  },
  {
    "name": "head_commit_id",
    "type": "string",
    "description": "SHA-1 hash representing the commit ID of the current HEAD of the repo."
  },
  {
    "name": "branch",
    "type": "string",
    "description": ""
  },
  {
    "name": "path",
    "type": "string",
    "description": "Path of the Git folder (repo) in the workspace."
  },
  {
    "name": "provider",
    "type": "string",
    "description": "Git provider of the linked Git repository."
  },
  {
    "name": "sparse_checkout",
    "type": "object",
    "description": "Sparse checkout settings for the Git folder (repo).",
    "children": [
      {
        "name": "patterns",
        "type": "array",
        "description": "List of sparse checkout cone patterns, see [cone mode handling] for details. [cone mode handling]: https://git-scm.com/docs/git-sparse-checkout#_internalscone_mode_handling"
      }
    ]
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL of the linked Git repository."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "integer",
    "description": "Id of the git folder (repo) in the Workspace."
  },
  {
    "name": "head_commit_id",
    "type": "string",
    "description": "Current git commit id of the git folder (repo)."
  },
  {
    "name": "branch",
    "type": "string",
    "description": "Name of the current git branch of the git folder (repo)."
  },
  {
    "name": "path",
    "type": "string",
    "description": "Root path of the git folder (repo) in the Workspace."
  },
  {
    "name": "provider",
    "type": "string",
    "description": "Git provider of the remote git repository, e.g. `gitHub`."
  },
  {
    "name": "sparse_checkout",
    "type": "object",
    "description": "Sparse checkout config for the git folder (repo).",
    "children": [
      {
        "name": "patterns",
        "type": "array",
        "description": "List of sparse checkout cone patterns, see [cone mode handling] for details. [cone mode handling]: https://git-scm.com/docs/git-sparse-checkout#_internalscone_mode_handling"
      }
    ]
  },
  {
    "name": "url",
    "type": "string",
    "description": "URL of the remote git repository."
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
    <td><a href="#parameter-repo_id"><code>repo_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Returns the repo with the given repo ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-next_page_token"><code>next_page_token</code></a>, <a href="#parameter-path_prefix"><code>path_prefix</code></a></td>
    <td>Returns repos that the calling user has Manage permissions on. Use `next_page_token` to iterate</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-provider"><code>provider</code></a></td>
    <td></td>
    <td>Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-repo_id"><code>repo_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-repo_id"><code>repo_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes the specified repo.</td>
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
<tr id="parameter-repo_id">
    <td><CopyableCode code="repo_id" /></td>
    <td><code>integer</code></td>
    <td>The ID for the corresponding repo to delete.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-next_page_token">
    <td><CopyableCode code="next_page_token" /></td>
    <td><code>string</code></td>
    <td>Token used to get the next page of results. If not specified, returns the first page of results as well as a next page token if there are more results.</td>
</tr>
<tr id="parameter-path_prefix">
    <td><CopyableCode code="path_prefix" /></td>
    <td><code>string</code></td>
    <td>Filters repos that have paths starting with the given path prefix. If not provided or when provided an effectively empty prefix (`/` or `/Workspace`) Git folders (repos) from `/Workspace/Repos` will be served.</td>
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

Returns the repo with the given repo ID.

```sql
SELECT
id,
head_commit_id,
branch,
path,
provider,
sparse_checkout,
url
FROM databricks_workspace.workspace.repos
WHERE repo_id = '{{ repo_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns repos that the calling user has Manage permissions on. Use `next_page_token` to iterate

```sql
SELECT
id,
head_commit_id,
branch,
path,
provider,
sparse_checkout,
url
FROM databricks_workspace.workspace.repos
WHERE workspace = '{{ workspace }}' -- required
AND next_page_token = '{{ next_page_token }}'
AND path_prefix = '{{ path_prefix }}'
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

Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created

```sql
INSERT INTO databricks_workspace.workspace.repos (
url,
provider,
path,
sparse_checkout,
workspace
)
SELECT 
'{{ url }}' /* required */,
'{{ provider }}' /* required */,
'{{ path }}',
'{{ sparse_checkout }}',
'{{ workspace }}'
RETURNING
id,
head_commit_id,
branch,
path,
provider,
sparse_checkout,
url
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: repos
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the repos resource.
    - name: url
      value: "{{ url }}"
      description: |
        URL of the Git repository to be linked.
    - name: provider
      value: "{{ provider }}"
      description: |
        Git provider. This field is case-insensitive. The available Git providers are \`gitHub\`, \`bitbucketCloud\`, \`gitLab\`, \`azureDevOpsServices\`, \`gitHubEnterprise\`, \`bitbucketServer\`, \`gitLabEnterpriseEdition\` and \`awsCodeCommit\`.
    - name: path
      value: "{{ path }}"
      description: |
        Desired path for the repo in the workspace. Almost any path in the workspace can be chosen. If repo is created in \`/Repos\`, path must be in the format \`/Repos/{folder}/{repo-name}\`.
    - name: sparse_checkout
      description: |
        If specified, the repo will be created with sparse checkout enabled. You cannot enable/disable sparse checkout after the repo is created.
      value:
        patterns:
          - "{{ patterns }}"
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

Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same

```sql
UPDATE databricks_workspace.workspace.repos
SET 
branch = '{{ branch }}',
sparse_checkout = '{{ sparse_checkout }}',
tag = '{{ tag }}'
WHERE 
repo_id = '{{ repo_id }}' --required
AND workspace = '{{ workspace }}' --required;
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

Deletes the specified repo.

```sql
DELETE FROM databricks_workspace.workspace.repos
WHERE repo_id = '{{ repo_id }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
