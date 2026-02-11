---
title: all_cluster_library_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - all_cluster_library_statuses
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

Creates, updates, deletes, gets or lists an <code>all_cluster_library_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>all_cluster_library_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.all_cluster_library_statuses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "cluster_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "library_statuses",
    "type": "array",
    "description": "Status of all libraries on the cluster.",
    "children": [
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
        "description": "Status of installing the library on the cluster."
      }
    ]
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Get the status of all libraries on all clusters. A status is returned for all libraries installed on<br />this cluster via the API or the libraries UI.<br /><br /><br />:returns: Iterator over :class:`ClusterLibraryStatuses`</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks Workspace Deployment Name (default: dbc-abcd0123-a1bc)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get the status of all libraries on all clusters. A status is returned for all libraries installed on<br />this cluster via the API or the libraries UI.<br /><br /><br />:returns: Iterator over :class:`ClusterLibraryStatuses`

```sql
SELECT
cluster_id,
library_statuses
FROM databricks_workspace.compute.all_cluster_library_statuses
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
</Tabs>
