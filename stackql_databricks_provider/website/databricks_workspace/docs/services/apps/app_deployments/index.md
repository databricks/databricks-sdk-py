---
title: app_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - app_deployments
  - apps
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

Creates, updates, deletes, gets or lists an <code>app_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.app_deployments" /></td></tr>
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
    "name": "deployment_id",
    "type": "string",
    "description": "The unique id of the deployment."
  },
  {
    "name": "command",
    "type": "array",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user creates the deployment."
  },
  {
    "name": "deployment_artifacts",
    "type": "object",
    "description": "The deployment artifacts for an app.",
    "children": [
      {
        "name": "source_code_path",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "env_vars",
    "type": "array",
    "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value for the environment variable."
      },
      {
        "name": "value_from",
        "type": "string",
        "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
      }
    ]
  },
  {
    "name": "git_source",
    "type": "object",
    "description": "Git repository to use as the source for the app deployment.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Git branch to checkout."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Git commit SHA to checkout."
      },
      {
        "name": "git_repository",
        "type": "object",
        "description": "Git repository configuration. Populated from the app's git_repository configuration.",
        "children": [
          {
            "name": "url",
            "type": "string",
            "description": "URL of the Git repository."
          },
          {
            "name": "provider",
            "type": "string",
            "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
          }
        ]
      },
      {
        "name": "resolved_commit",
        "type": "string",
        "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
      },
      {
        "name": "tag",
        "type": "string",
        "description": "Git tag to checkout."
      }
    ]
  },
  {
    "name": "mode",
    "type": "string",
    "description": "The mode of which the deployment will manage the source code."
  },
  {
    "name": "source_code_path",
    "type": "string",
    "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
  },
  {
    "name": "status",
    "type": "object",
    "description": "Status and status message of the deployment",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the deployment."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "deployment_id",
    "type": "string",
    "description": "The unique id of the deployment."
  },
  {
    "name": "command",
    "type": "array",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the deployment. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user creates the deployment."
  },
  {
    "name": "deployment_artifacts",
    "type": "object",
    "description": "The deployment artifacts for an app.",
    "children": [
      {
        "name": "source_code_path",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "env_vars",
    "type": "array",
    "description": "The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value for the environment variable."
      },
      {
        "name": "value_from",
        "type": "string",
        "description": "The name of an external Databricks resource that contains the value, such as a secret or a database table."
      }
    ]
  },
  {
    "name": "git_source",
    "type": "object",
    "description": "Git repository to use as the source for the app deployment.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Git branch to checkout."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Git commit SHA to checkout."
      },
      {
        "name": "git_repository",
        "type": "object",
        "description": "Git repository configuration. Populated from the app's git_repository configuration.",
        "children": [
          {
            "name": "url",
            "type": "string",
            "description": "URL of the Git repository."
          },
          {
            "name": "provider",
            "type": "string",
            "description": "Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit."
          }
        ]
      },
      {
        "name": "resolved_commit",
        "type": "string",
        "description": "The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time."
      },
      {
        "name": "source_code_path",
        "type": "string",
        "description": "Relative path to the app source code within the Git repository. If not specified, the root of the repository is used."
      },
      {
        "name": "tag",
        "type": "string",
        "description": "Git tag to checkout."
      }
    ]
  },
  {
    "name": "mode",
    "type": "string",
    "description": "The mode of which the deployment will manage the source code."
  },
  {
    "name": "source_code_path",
    "type": "string",
    "description": "The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment."
  },
  {
    "name": "status",
    "type": "object",
    "description": "Status and status message of the deployment",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the deployment."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
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
    <td><a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Retrieves information for the app deployment with the supplied name and deployment id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all app deployments for the app with the supplied name.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__app_deployment"><code>data__app_deployment</code></a></td>
    <td></td>
    <td>Creates an app deployment for the app with the supplied name.</td>
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
<tr id="parameter-app_name">
    <td><CopyableCode code="app_name" /></td>
    <td><code>string</code></td>
    <td>The name of the app.</td>
</tr>
<tr id="parameter-deployment_id">
    <td><CopyableCode code="deployment_id" /></td>
    <td><code>string</code></td>
    <td>The unique id of the deployment.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>string</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of apps. Requests first page if absent.</td>
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

Retrieves information for the app deployment with the supplied name and deployment id.

```sql
SELECT
deployment_id,
command,
create_time,
creator,
deployment_artifacts,
env_vars,
git_source,
mode,
source_code_path,
status,
update_time
FROM databricks_workspace.apps.app_deployments
WHERE app_name = '{{ app_name }}' -- required
AND deployment_id = '{{ deployment_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all app deployments for the app with the supplied name.

```sql
SELECT
deployment_id,
command,
create_time,
creator,
deployment_artifacts,
env_vars,
git_source,
mode,
source_code_path,
status,
update_time
FROM databricks_workspace.apps.app_deployments
WHERE app_name = '{{ app_name }}' -- required
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

Creates an app deployment for the app with the supplied name.

```sql
INSERT INTO databricks_workspace.apps.app_deployments (
data__app_deployment,
app_name,
deployment_name
)
SELECT 
'{{ app_deployment }}' /* required */,
'{{ app_name }}',
'{{ deployment_name }}'
RETURNING
deployment_id,
command,
create_time,
creator,
deployment_artifacts,
env_vars,
git_source,
mode,
source_code_path,
status,
update_time
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: app_deployments
  props:
    - name: app_name
      value: string
      description: Required parameter for the app_deployments resource.
    - name: deployment_name
      value: string
      description: Required parameter for the app_deployments resource.
    - name: app_deployment
      value: string
      description: |
        The app deployment configuration.
```
</TabItem>
</Tabs>
