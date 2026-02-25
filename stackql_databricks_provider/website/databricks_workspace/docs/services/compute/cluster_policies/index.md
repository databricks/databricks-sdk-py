---
title: cluster_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_policies
  - compute
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

Creates, updates, deletes, gets or lists a <code>cluster_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_policies" /></td></tr>
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
    "description": "Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100 characters."
  },
  {
    "name": "policy_family_id",
    "type": "string",
    "description": "ID of the policy family. The cluster policy's policy definition inherits the policy family's policy definition. Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the policy definition."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "Canonical unique identifier for the Cluster Policy."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "Creator user name. The field won't be included in the response if the user has already been deleted."
  },
  {
    "name": "created_at_timestamp",
    "type": "integer",
    "description": "Creation time. The timestamp (in millisecond) when this Cluster Policy was created."
  },
  {
    "name": "definition",
    "type": "string",
    "description": "Policy definition document expressed in [Databricks Cluster Policy Definition Language]. [Databricks Cluster Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html"
  },
  {
    "name": "description",
    "type": "string",
    "description": "Additional human-readable description of the cluster policy."
  },
  {
    "name": "is_default",
    "type": "boolean",
    "description": "If true, policy is a default policy created and managed by Databricks. Default policies cannot be deleted, and their policy families cannot be changed."
  },
  {
    "name": "libraries",
    "type": "array",
    "description": "A list of libraries to be installed on the next cluster restart that uses this policy. The maximum number of libraries is 500.",
    "children": [
      {
        "name": "cran",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "package",
            "type": "string",
            "description": ""
          },
          {
            "name": "repo",
            "type": "string",
            "description": "The repository where the package can be found. If not specified, the default CRAN repo is used."
          }
        ]
      },
      {
        "name": "egg",
        "type": "string",
        "description": "Deprecated. URI of the egg library to install. Installing Python egg files is deprecated and is not supported in Databricks Runtime 14.0 and above."
      },
      {
        "name": "jar",
        "type": "string",
        "description": "URI of the JAR library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `&#123; \"jar\": \"/Workspace/path/to/library.jar\" &#125;`, `&#123; \"jar\" : \"/Volumes/path/to/library.jar\" &#125;` or `&#123; \"jar\": \"s3://my-bucket/library.jar\" &#125;`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI."
      },
      {
        "name": "maven",
        "type": "object",
        "description": "Specification of a maven library to be installed. For example: `&#123; \"coordinates\": \"org.jsoup:jsoup:1.7.2\" &#125;`",
        "children": [
          {
            "name": "coordinates",
            "type": "string",
            "description": ""
          },
          {
            "name": "exclusions",
            "type": "array",
            "description": "List of dependences to exclude. For example: `[\"slf4j:slf4j\", \"*:hadoop-client\"]`. Maven dependency exclusions: https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html."
          },
          {
            "name": "repo",
            "type": "string",
            "description": "Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched."
          }
        ]
      },
      {
        "name": "pypi",
        "type": "object",
        "description": "Specification of a PyPi library to be installed. For example: `&#123; \"package\": \"simplejson\" &#125;`",
        "children": [
          {
            "name": "package",
            "type": "string",
            "description": ""
          },
          {
            "name": "repo",
            "type": "string",
            "description": "The repository where the package can be found. If not specified, the default pip index is used."
          }
        ]
      },
      {
        "name": "requirements",
        "type": "string",
        "description": "URI of the requirements.txt file to install. Only Workspace paths and Unity Catalog Volumes paths are supported. For example: `&#123; \"requirements\": \"/Workspace/path/to/requirements.txt\" &#125;` or `&#123; \"requirements\" : \"/Volumes/path/to/requirements.txt\" &#125;`"
      },
      {
        "name": "whl",
        "type": "string",
        "description": "URI of the wheel library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `&#123; \"whl\": \"/Workspace/path/to/library.whl\" &#125;`, `&#123; \"whl\" : \"/Volumes/path/to/library.whl\" &#125;` or `&#123; \"whl\": \"s3://my-bucket/library.whl\" &#125;`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI."
      }
    ]
  },
  {
    "name": "max_clusters_per_user",
    "type": "integer",
    "description": "Max number of clusters per user that can be active using this policy. If not present, there is no max limit."
  },
  {
    "name": "policy_family_definition_overrides",
    "type": "string",
    "description": "Policy definition JSON document expressed in [Databricks Policy Definition Language]. The JSON document must be passed as a string and cannot be embedded in the requests. You can use this to customize the policy definition inherited from the policy family. Policy rules specified here are merged into the inherited policy definition. [Databricks Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100 characters."
  },
  {
    "name": "policy_family_id",
    "type": "string",
    "description": "ID of the policy family. The cluster policy's policy definition inherits the policy family's policy definition. Cannot be used with `definition`. Use `policy_family_definition_overrides` instead to customize the policy definition."
  },
  {
    "name": "policy_id",
    "type": "string",
    "description": "Canonical unique identifier for the Cluster Policy."
  },
  {
    "name": "creator_user_name",
    "type": "string",
    "description": "Creator user name. The field won't be included in the response if the user has already been deleted."
  },
  {
    "name": "created_at_timestamp",
    "type": "integer",
    "description": "Creation time. The timestamp (in millisecond) when this Cluster Policy was created."
  },
  {
    "name": "definition",
    "type": "string",
    "description": "Policy definition document expressed in [Databricks Cluster Policy Definition Language]. [Databricks Cluster Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html"
  },
  {
    "name": "description",
    "type": "string",
    "description": "Additional human-readable description of the cluster policy."
  },
  {
    "name": "is_default",
    "type": "boolean",
    "description": "If true, policy is a default policy created and managed by Databricks. Default policies cannot be deleted, and their policy families cannot be changed."
  },
  {
    "name": "libraries",
    "type": "array",
    "description": "A list of libraries to be installed on the next cluster restart that uses this policy. The maximum number of libraries is 500.",
    "children": [
      {
        "name": "cran",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "package",
            "type": "string",
            "description": ""
          },
          {
            "name": "repo",
            "type": "string",
            "description": "The repository where the package can be found. If not specified, the default CRAN repo is used."
          }
        ]
      },
      {
        "name": "egg",
        "type": "string",
        "description": "Deprecated. URI of the egg library to install. Installing Python egg files is deprecated and is not supported in Databricks Runtime 14.0 and above."
      },
      {
        "name": "jar",
        "type": "string",
        "description": "URI of the JAR library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `&#123; \"jar\": \"/Workspace/path/to/library.jar\" &#125;`, `&#123; \"jar\" : \"/Volumes/path/to/library.jar\" &#125;` or `&#123; \"jar\": \"s3://my-bucket/library.jar\" &#125;`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI."
      },
      {
        "name": "maven",
        "type": "object",
        "description": "Specification of a maven library to be installed. For example: `&#123; \"coordinates\": \"org.jsoup:jsoup:1.7.2\" &#125;`",
        "children": [
          {
            "name": "coordinates",
            "type": "string",
            "description": ""
          },
          {
            "name": "exclusions",
            "type": "array",
            "description": "List of dependences to exclude. For example: `[\"slf4j:slf4j\", \"*:hadoop-client\"]`. Maven dependency exclusions: https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html."
          },
          {
            "name": "repo",
            "type": "string",
            "description": "Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched."
          }
        ]
      },
      {
        "name": "pypi",
        "type": "object",
        "description": "Specification of a PyPi library to be installed. For example: `&#123; \"package\": \"simplejson\" &#125;`",
        "children": [
          {
            "name": "package",
            "type": "string",
            "description": ""
          },
          {
            "name": "repo",
            "type": "string",
            "description": "The repository where the package can be found. If not specified, the default pip index is used."
          }
        ]
      },
      {
        "name": "requirements",
        "type": "string",
        "description": "URI of the requirements.txt file to install. Only Workspace paths and Unity Catalog Volumes paths are supported. For example: `&#123; \"requirements\": \"/Workspace/path/to/requirements.txt\" &#125;` or `&#123; \"requirements\" : \"/Volumes/path/to/requirements.txt\" &#125;`"
      },
      {
        "name": "whl",
        "type": "string",
        "description": "URI of the wheel library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `&#123; \"whl\": \"/Workspace/path/to/library.whl\" &#125;`, `&#123; \"whl\" : \"/Volumes/path/to/library.whl\" &#125;` or `&#123; \"whl\": \"s3://my-bucket/library.whl\" &#125;`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI."
      }
    ]
  },
  {
    "name": "max_clusters_per_user",
    "type": "integer",
    "description": "Max number of clusters per user that can be active using this policy. If not present, there is no max limit."
  },
  {
    "name": "policy_family_definition_overrides",
    "type": "string",
    "description": "Policy definition JSON document expressed in [Databricks Policy Definition Language]. The JSON document must be passed as a string and cannot be embedded in the requests. You can use this to customize the policy definition inherited from the policy family. Policy rules specified here are merged into the inherited policy definition. [Databricks Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html"
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
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get a cluster policy entity. Creation and editing is available to admins only.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-sort_column"><code>sort_column</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a></td>
    <td>Returns a list of policies accessible by the requesting user.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Creates a new policy with prescribed settings.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Update an existing policy for cluster. This operation may make some clusters governed by the previous</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>Canonical unique identifier for the Cluster Policy.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-sort_column">
    <td><CopyableCode code="sort_column" /></td>
    <td><code>string</code></td>
    <td>The cluster policy attribute to sort by. * `POLICY_CREATION_TIME` - Sort result list by policy creation time. * `POLICY_NAME` - Sort result list by policy name.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>The order in which the policies get listed. * `DESC` - Sort result list in descending order. * `ASC` - Sort result list in ascending order.</td>
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

Get a cluster policy entity. Creation and editing is available to admins only.

```sql
SELECT
name,
policy_family_id,
policy_id,
creator_user_name,
created_at_timestamp,
definition,
description,
is_default,
libraries,
max_clusters_per_user,
policy_family_definition_overrides
FROM databricks_workspace.compute.cluster_policies
WHERE policy_id = '{{ policy_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of policies accessible by the requesting user.

```sql
SELECT
name,
policy_family_id,
policy_id,
creator_user_name,
created_at_timestamp,
definition,
description,
is_default,
libraries,
max_clusters_per_user,
policy_family_definition_overrides
FROM databricks_workspace.compute.cluster_policies
WHERE workspace = '{{ workspace }}' -- required
AND sort_column = '{{ sort_column }}'
AND sort_order = '{{ sort_order }}'
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

Creates a new policy with prescribed settings.

```sql
INSERT INTO databricks_workspace.compute.cluster_policies (
definition,
description,
libraries,
max_clusters_per_user,
name,
policy_family_definition_overrides,
policy_family_id,
workspace
)
SELECT 
'{{ definition }}',
'{{ description }}',
'{{ libraries }}',
{{ max_clusters_per_user }},
'{{ name }}',
'{{ policy_family_definition_overrides }}',
'{{ policy_family_id }}',
'{{ workspace }}'
RETURNING
policy_id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cluster_policies
  props:
    - name: workspace
      value: "{{ workspace }}"
      description: Required parameter for the cluster_policies resource.
    - name: definition
      value: "{{ definition }}"
      description: |
        Policy definition document expressed in [Databricks Cluster Policy Definition Language]. [Databricks Cluster Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
    - name: description
      value: "{{ description }}"
      description: |
        Additional human-readable description of the cluster policy.
    - name: libraries
      description: |
        A list of libraries to be installed on the next cluster restart that uses this policy. The maximum number of libraries is 500.
      value:
        - cran:
            package: "{{ package }}"
            repo: "{{ repo }}"
          egg: "{{ egg }}"
          jar: "{{ jar }}"
          maven:
            coordinates: "{{ coordinates }}"
            exclusions:
              - "{{ exclusions }}"
            repo: "{{ repo }}"
          pypi:
            package: "{{ package }}"
            repo: "{{ repo }}"
          requirements: "{{ requirements }}"
          whl: "{{ whl }}"
    - name: max_clusters_per_user
      value: {{ max_clusters_per_user }}
      description: |
        Max number of clusters per user that can be active using this policy. If not present, there is no max limit.
    - name: name
      value: "{{ name }}"
      description: |
        Cluster Policy name requested by the user. This has to be unique. Length must be between 1 and 100 characters.
    - name: policy_family_definition_overrides
      value: "{{ policy_family_definition_overrides }}"
      description: |
        Policy definition JSON document expressed in [Databricks Policy Definition Language]. The JSON document must be passed as a string and cannot be embedded in the requests. You can use this to customize the policy definition inherited from the policy family. Policy rules specified here are merged into the inherited policy definition. [Databricks Policy Definition Language]: https://docs.databricks.com/administration-guide/clusters/policy-definition.html
    - name: policy_family_id
      value: "{{ policy_family_id }}"
      description: |
        ID of the policy family. The cluster policy's policy definition inherits the policy family's policy definition. Cannot be used with \`definition\`. Use \`policy_family_definition_overrides\` instead to customize the policy definition.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Update an existing policy for cluster. This operation may make some clusters governed by the previous

```sql
REPLACE databricks_workspace.compute.cluster_policies
SET 
policy_id = '{{ policy_id }}',
definition = '{{ definition }}',
description = '{{ description }}',
libraries = '{{ libraries }}',
max_clusters_per_user = {{ max_clusters_per_user }},
name = '{{ name }}',
policy_family_definition_overrides = '{{ policy_family_definition_overrides }}',
policy_family_id = '{{ policy_family_id }}'
WHERE 
workspace = '{{ workspace }}' --required
AND policy_id = '{{ policy_id }}' --required;
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

Delete a policy for a cluster. Clusters governed by this policy can still run, but cannot be edited.

```sql
DELETE FROM databricks_workspace.compute.cluster_policies
WHERE workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
