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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>git_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_credentials</code></td></tr>
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
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Gets the Git credential with the specified credential ID.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.<br /><br />:returns: :class:`GetCredentialsResponse`</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Lists the calling user's Git credentials.<br /><br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be listed. Only service principal managers<br />  can perform this action.<br /><br />:returns: Iterator over :class:`CredentialInfo`</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__git_provider"><code>data__git_provider</code></a></td>
    <td></td>
    <td>Creates a Git credential entry for the user. Only one Git credential per user is supported, so any<br />attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update<br />existing credentials, or the DELETE endpoint to delete existing credentials.<br /><br />:param git_provider: str<br />  Git provider. This field is case-insensitive. The available Git providers are `gitHub`,<br />  `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,<br />  `gitLabEnterpriseEdition` and `awsCodeCommit`.<br />:param git_email: str (optional)<br />  The authenticating email associated with your Git provider user account. Used for authentication<br />  with the remote repository and also sets the author & committer identity for commits. Required for<br />  most Git providers except AWS CodeCommit. Learn more at<br />  https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider<br />:param git_username: str (optional)<br />  The username provided with your Git provider account and associated with the credential. For most<br />  Git providers it is only used to set the Git committer & author names for commits, however it may be<br />  required for authentication depending on your Git provider / token requirements. Required for AWS<br />  CodeCommit.<br />:param is_default_for_provider: bool (optional)<br />  if the credential is the default for the given provider<br />:param name: str (optional)<br />  the name of the git credential, used for identification and ease of lookup<br />:param personal_access_token: str (optional)<br />  The personal access token used to authenticate to the corresponding Git provider. For certain<br />  providers, support may exist for other types of scoped access tokens. [Learn more].<br /><br />  [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.<br /><br />:returns: :class:`CreateCredentialsResponse`</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-data__git_provider"><code>data__git_provider</code></a></td>
    <td></td>
    <td>Updates the specified Git credential.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param git_provider: str<br />  Git provider. This field is case-insensitive. The available Git providers are `gitHub`,<br />  `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,<br />  `gitLabEnterpriseEdition` and `awsCodeCommit`.<br />:param git_email: str (optional)<br />  The authenticating email associated with your Git provider user account. Used for authentication<br />  with the remote repository and also sets the author & committer identity for commits. Required for<br />  most Git providers except AWS CodeCommit. Learn more at<br />  https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider<br />:param git_username: str (optional)<br />  The username provided with your Git provider account and associated with the credential. For most<br />  Git providers it is only used to set the Git committer & author names for commits, however it may be<br />  required for authentication depending on your Git provider / token requirements. Required for AWS<br />  CodeCommit.<br />:param is_default_for_provider: bool (optional)<br />  if the credential is the default for the given provider<br />:param name: str (optional)<br />  the name of the git credential, used for identification and ease of lookup<br />:param personal_access_token: str (optional)<br />  The personal access token used to authenticate to the corresponding Git provider. For certain<br />  providers, support may exist for other types of scoped access tokens. [Learn more].<br /><br />  [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-credential_id"><code>credential_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td>Deletes the specified Git credential.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>string</code></td>
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

Gets the Git credential with the specified credential ID.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.<br /><br />:returns: :class:`GetCredentialsResponse`

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
AND deployment_name = '{{ deployment_name }}' -- required
AND principal_id = '{{ principal_id }}'
;
```
</TabItem>
<TabItem value="list">

Lists the calling user's Git credentials.<br /><br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be listed. Only service principal managers<br />  can perform this action.<br /><br />:returns: Iterator over :class:`CredentialInfo`

```sql
SELECT
name,
credential_id,
git_email,
git_provider,
git_username,
is_default_for_provider
FROM databricks_workspace.workspace.git_credentials
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a Git credential entry for the user. Only one Git credential per user is supported, so any<br />attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update<br />existing credentials, or the DELETE endpoint to delete existing credentials.<br /><br />:param git_provider: str<br />  Git provider. This field is case-insensitive. The available Git providers are `gitHub`,<br />  `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,<br />  `gitLabEnterpriseEdition` and `awsCodeCommit`.<br />:param git_email: str (optional)<br />  The authenticating email associated with your Git provider user account. Used for authentication<br />  with the remote repository and also sets the author & committer identity for commits. Required for<br />  most Git providers except AWS CodeCommit. Learn more at<br />  https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider<br />:param git_username: str (optional)<br />  The username provided with your Git provider account and associated with the credential. For most<br />  Git providers it is only used to set the Git committer & author names for commits, however it may be<br />  required for authentication depending on your Git provider / token requirements. Required for AWS<br />  CodeCommit.<br />:param is_default_for_provider: bool (optional)<br />  if the credential is the default for the given provider<br />:param name: str (optional)<br />  the name of the git credential, used for identification and ease of lookup<br />:param personal_access_token: str (optional)<br />  The personal access token used to authenticate to the corresponding Git provider. For certain<br />  providers, support may exist for other types of scoped access tokens. [Learn more].<br /><br />  [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.<br /><br />:returns: :class:`CreateCredentialsResponse`

```sql
INSERT INTO databricks_workspace.workspace.git_credentials (
data__git_provider,
data__git_email,
data__git_username,
data__is_default_for_provider,
data__name,
data__personal_access_token,
data__principal_id,
deployment_name
)
SELECT 
'{{ git_provider }}' /* required */,
'{{ git_email }}',
'{{ git_username }}',
'{{ is_default_for_provider }}',
'{{ name }}',
'{{ personal_access_token }}',
'{{ principal_id }}',
'{{ deployment_name }}'
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

```yaml
# Description fields are for documentation purposes
- name: git_credentials
  props:
    - name: deployment_name
      value: string
      description: Required parameter for the git_credentials resource.
    - name: git_provider
      value: string
      description: |
        Git provider. This field is case-insensitive. The available Git providers are `gitHub`, `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`, `gitLabEnterpriseEdition` and `awsCodeCommit`.
    - name: git_email
      value: string
      description: |
        The authenticating email associated with your Git provider user account. Used for authentication with the remote repository and also sets the author & committer identity for commits. Required for most Git providers except AWS CodeCommit. Learn more at https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
    - name: git_username
      value: string
      description: |
        The username provided with your Git provider account and associated with the credential. For most Git providers it is only used to set the Git committer & author names for commits, however it may be required for authentication depending on your Git provider / token requirements. Required for AWS CodeCommit.
    - name: is_default_for_provider
      value: string
      description: |
        if the credential is the default for the given provider
    - name: name
      value: string
      description: |
        the name of the git credential, used for identification and ease of lookup
    - name: personal_access_token
      value: string
      description: |
        The personal access token used to authenticate to the corresponding Git provider. For certain providers, support may exist for other types of scoped access tokens. [Learn more]. [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html
    - name: principal_id
      value: string
      description: |
        The ID of the service principal whose credentials will be modified. Only service principal managers can perform this action.
```
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

Updates the specified Git credential.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param git_provider: str<br />  Git provider. This field is case-insensitive. The available Git providers are `gitHub`,<br />  `bitbucketCloud`, `gitLab`, `azureDevOpsServices`, `gitHubEnterprise`, `bitbucketServer`,<br />  `gitLabEnterpriseEdition` and `awsCodeCommit`.<br />:param git_email: str (optional)<br />  The authenticating email associated with your Git provider user account. Used for authentication<br />  with the remote repository and also sets the author & committer identity for commits. Required for<br />  most Git providers except AWS CodeCommit. Learn more at<br />  https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider<br />:param git_username: str (optional)<br />  The username provided with your Git provider account and associated with the credential. For most<br />  Git providers it is only used to set the Git committer & author names for commits, however it may be<br />  required for authentication depending on your Git provider / token requirements. Required for AWS<br />  CodeCommit.<br />:param is_default_for_provider: bool (optional)<br />  if the credential is the default for the given provider<br />:param name: str (optional)<br />  the name of the git credential, used for identification and ease of lookup<br />:param personal_access_token: str (optional)<br />  The personal access token used to authenticate to the corresponding Git provider. For certain<br />  providers, support may exist for other types of scoped access tokens. [Learn more].<br /><br />  [Learn more]: https://docs.databricks.com/repos/get-access-tokens-from-git-provider.html<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.

```sql
UPDATE databricks_workspace.workspace.git_credentials
SET 
data__git_provider = '{{ git_provider }}',
data__git_email = '{{ git_email }}',
data__git_username = '{{ git_username }}',
data__is_default_for_provider = '{{ is_default_for_provider }}',
data__name = '{{ name }}',
data__personal_access_token = '{{ personal_access_token }}',
data__principal_id = '{{ principal_id }}'
WHERE 
credential_id = '{{ credential_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND data__git_provider = '{{ git_provider }}' --required;
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

Deletes the specified Git credential.<br /><br />:param credential_id: int<br />  The ID for the corresponding credential to access.<br />:param principal_id: int (optional)<br />  The ID of the service principal whose credentials will be modified. Only service principal managers<br />  can perform this action.

```sql
DELETE FROM databricks_workspace.workspace.git_credentials
WHERE credential_id = '{{ credential_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND principal_id = '{{ principal_id }}'
;
```
</TabItem>
</Tabs>
