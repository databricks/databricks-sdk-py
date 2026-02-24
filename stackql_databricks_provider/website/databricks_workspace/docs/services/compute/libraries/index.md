---
title: libraries
hide_title: false
hide_table_of_contents: false
keywords:
  - libraries
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>libraries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="libraries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.libraries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "is_library_for_all_clusters",
    "type": "boolean",
    "description": "Whether the library was set to be installed on all clusters via the libraries UI."
  },
  {
    "name": "library",
    "type": "object",
    "description": "Unique identifier for the library.",
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
    "name": "messages",
    "type": "array",
    "description": "All the info and warning messages that have occurred so far for this library."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of installing the library on the cluster. (FAILED, INSTALLED, INSTALLING, PENDING, RESOLVING, RESTORED, SKIPPED, UNINSTALL_ON_RESTART)"
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
    <td><a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get the status of libraries on a cluster. A status is returned for all libraries installed on this</td>
</tr>
<tr>
    <td><a href="#install"><CopyableCode code="install" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-libraries"><code>libraries</code></a></td>
    <td></td>
    <td>Add libraries to install on a cluster. The installation is asynchronous; it happens in the background</td>
</tr>
<tr>
    <td><a href="#uninstall"><CopyableCode code="uninstall" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-libraries"><code>libraries</code></a></td>
    <td></td>
    <td>Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the cluster whose status should be retrieved.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the status of libraries on a cluster. A status is returned for all libraries installed on this

```sql
SELECT
is_library_for_all_clusters,
library,
messages,
status
FROM databricks_workspace.compute.libraries
WHERE cluster_id = '{{ cluster_id }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="install"
    values={[
        { label: 'install', value: 'install' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="install">

Add libraries to install on a cluster. The installation is asynchronous; it happens in the background

```sql
INSERT INTO databricks_workspace.compute.libraries (
cluster_id,
libraries,
workspace
)
SELECT 
'{{ cluster_id }}' /* required */,
'{{ libraries }}' /* required */,
'{{ workspace }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: libraries
  props:
    - name: workspace
      value: string
      description: Required parameter for the libraries resource.
    - name: cluster_id
      value: string
      description: |
        Unique identifier for the cluster on which to install these libraries.
    - name: libraries
      value: array
      description: |
        The libraries to install.
      props:
      - name: cran
        value: object
        props:
        - name: package
          value: string
        - name: repo
          value: string
          description: |
            The repository where the package can be found. If not specified, the default CRAN repo is used.
      - name: egg
        value: string
        description: |
          Deprecated. URI of the egg library to install. Installing Python egg files is deprecated and is not supported in Databricks Runtime 14.0 and above.
      - name: jar
        value: string
        description: |
          URI of the JAR library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `{ "jar": "/Workspace/path/to/library.jar" }`, `{ "jar" : "/Volumes/path/to/library.jar" }` or `{ "jar": "s3://my-bucket/library.jar" }`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI.
      - name: maven
        value: object
        description: |
          Specification of a maven library to be installed. For example: `{ "coordinates": "org.jsoup:jsoup:1.7.2" }`
        props:
        - name: coordinates
          value: string
        - name: exclusions
          value: array
          description: |
            List of dependences to exclude. For example: `["slf4j:slf4j", "*:hadoop-client"]`. Maven dependency exclusions: https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html.
          items:
            type: string
        - name: repo
          value: string
          description: |
            Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched.
      - name: pypi
        value: object
        description: |
          Specification of a PyPi library to be installed. For example: `{ "package": "simplejson" }`
        props:
        - name: package
          value: string
        - name: repo
          value: string
          description: |
            The repository where the package can be found. If not specified, the default pip index is used.
      - name: requirements
        value: string
        description: |
          URI of the requirements.txt file to install. Only Workspace paths and Unity Catalog Volumes paths are supported. For example: `{ "requirements": "/Workspace/path/to/requirements.txt" }` or `{ "requirements" : "/Volumes/path/to/requirements.txt" }`
      - name: whl
        value: string
        description: |
          URI of the wheel library to install. Supported URIs include Workspace paths, Unity Catalog Volumes paths, and S3 URIs. For example: `{ "whl": "/Workspace/path/to/library.whl" }`, `{ "whl" : "/Volumes/path/to/library.whl" }` or `{ "whl": "s3://my-bucket/library.whl" }`. If S3 is used, please make sure the cluster has read access on the library. You may need to launch the cluster with an IAM role to access the S3 URI.
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="uninstall"
    values={[
        { label: 'uninstall', value: 'uninstall' }
    ]}
>
<TabItem value="uninstall">

Set libraries to uninstall from a cluster. The libraries won't be uninstalled until the cluster is

```sql
EXEC databricks_workspace.compute.libraries.uninstall 
@workspace='{{ workspace }}' --required 
@@json=
'{
"cluster_id": "{{ cluster_id }}", 
"libraries": "{{ libraries }}"
}'
;
```
</TabItem>
</Tabs>
