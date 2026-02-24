---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.apps" /></td></tr>
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
    "type": "string",
    "description": "The unique identifier of the app."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_integration_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "active_deployment",
    "type": "object",
    "description": "The active deployment of the app. A deployment is considered active when it has been deployed to the app compute.",
    "children": [
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
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
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
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
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
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "app_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the application. (CRASHED, DEPLOYING, RUNNING, UNAVAILABLE)"
      }
    ]
  },
  {
    "name": "compute_size",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (LARGE, MEDIUM)"
  },
  {
    "name": "compute_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "active_instances",
        "type": "integer",
        "description": ""
      },
      {
        "name": "message",
        "type": "string",
        "description": "Compute status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the app compute. (ACTIVE, DELETING, ERROR, STARTING, STOPPED, STOPPING, UPDATING)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app."
  },
  {
    "name": "default_source_code_path",
    "type": "string",
    "description": "The default workspace file system path of the source code from which app deployment are created. This field tracks the workspace source code path of the last active deployment."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "git_repository",
    "type": "object",
    "description": "Git repository configuration for app deployments. When specified, deployments can reference code from this repository by providing only the git reference (branch, tag, or commit).",
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
    "name": "pending_deployment",
    "type": "object",
    "description": "The pending deployment of the app. A deployment is considered pending when it is being prepared for deployment to the app compute.",
    "children": [
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
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
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
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
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
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
          }
        ]
      },
      {
        "name": "serving_endpoint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The URL of the app once it is deployed."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the app."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_budget_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "oauth2_app_integration_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": ""
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "active_deployment",
    "type": "object",
    "description": "The active deployment of the app. A deployment is considered active when it has been deployed to the app compute.",
    "children": [
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
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
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
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
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
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "app_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the application. (CRASHED, DEPLOYING, RUNNING, UNAVAILABLE)"
      }
    ]
  },
  {
    "name": "compute_size",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (LARGE, MEDIUM)"
  },
  {
    "name": "compute_status",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "active_instances",
        "type": "integer",
        "description": ""
      },
      {
        "name": "message",
        "type": "string",
        "description": "Compute status message"
      },
      {
        "name": "state",
        "type": "string",
        "description": "State of the app compute. (ACTIVE, DELETING, ERROR, STARTING, STOPPED, STOPPING, UPDATING)"
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The creation time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app."
  },
  {
    "name": "default_source_code_path",
    "type": "string",
    "description": "The default workspace file system path of the source code from which app deployment are created. This field tracks the workspace source code path of the last active deployment."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "git_repository",
    "type": "object",
    "description": "Git repository configuration for app deployments. When specified, deployments can reference code from this repository by providing only the git reference (branch, tag, or commit).",
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
    "name": "pending_deployment",
    "type": "object",
    "description": "The pending deployment of the app. A deployment is considered pending when it is being prepared for deployment to the app compute.",
    "children": [
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
        "name": "deployment_id",
        "type": "string",
        "description": "The unique id of the deployment."
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
        "description": "The mode of which the deployment will manage the source code. (AUTO_SYNC, SNAPSHOT)"
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
            "description": "State of the deployment. (CANCELLED, FAILED, IN_PROGRESS, SUCCEEDED)"
          }
        ]
      },
      {
        "name": "update_time",
        "type": "string",
        "description": "The update time of the deployment. Formatted timestamp in ISO 6801."
      }
    ]
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
          }
        ]
      },
      {
        "name": "serving_endpoint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The update time of the app. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app."
  },
  {
    "name": "url",
    "type": "string",
    "description": "The URL of the app once it is deployed."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": ""
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Retrieves information for the app with the supplied name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all apps in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-app"><code>app</code></a></td>
    <td><a href="#parameter-no_compute"><code>no_compute</code></a></td>
    <td>Creates a new app.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-app"><code>app</code></a></td>
    <td></td>
    <td>Updates the app with the supplied name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Deletes an app.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Start the last active deployment of the app in the workspace.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Stops the active deployment of the app in the workspace.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the app.</td>
</tr>
<tr id="parameter-workspace">
    <td><CopyableCode code="workspace" /></td>
    <td><code>string</code></td>
    <td>Your Databricks workspace name (default: your-workspace)</td>
</tr>
<tr id="parameter-no_compute">
    <td><CopyableCode code="no_compute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
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

Retrieves information for the app with the supplied name.

```sql
SELECT
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
update_time,
updater,
url,
user_api_scopes
FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all apps in the workspace.

```sql
SELECT
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
update_time,
updater,
url,
user_api_scopes
FROM databricks_workspace.apps.apps
WHERE workspace = '{{ workspace }}' -- required
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

Creates a new app.

```sql
INSERT INTO databricks_workspace.apps.apps (
app,
workspace,
no_compute
)
SELECT 
'{{ app }}' /* required */,
'{{ workspace }}',
'{{ no_compute }}'
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
update_time,
updater,
url,
user_api_scopes
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: apps
  props:
    - name: workspace
      value: string
      description: Required parameter for the apps resource.
    - name: app
      value: object
      description: |
        :param no_compute: bool (optional) If true, the app will not be started after creation.
      props:
      - name: name
        value: string
      - name: active_deployment
        value: object
        description: |
          The active deployment of the app. A deployment is considered active when it has been deployed to the app compute.
        props:
        - name: command
          value: array
          items:
            type: string
        - name: create_time
          value: string
          description: |
            The creation time of the deployment. Formatted timestamp in ISO 6801.
        - name: creator
          value: string
          description: |
            The email of the user creates the deployment.
        - name: deployment_artifacts
          value: object
          description: |
            The deployment artifacts for an app.
          props:
          - name: source_code_path
            value: string
        - name: deployment_id
          value: string
          description: |
            The unique id of the deployment.
        - name: env_vars
          value: array
          description: |
            The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.
          props:
          - name: name
            value: string
          - name: value
            value: string
            description: |
              The value for the environment variable.
          - name: value_from
            value: string
            description: |
              The name of an external Databricks resource that contains the value, such as a secret or a database table.
        - name: git_source
          value: object
          description: |
            Git repository to use as the source for the app deployment.
          props:
          - name: branch
            value: string
            description: |
              Git branch to checkout.
          - name: commit
            value: string
            description: |
              Git commit SHA to checkout.
          - name: git_repository
            value: object
            description: |
              Git repository configuration. Populated from the app's git_repository configuration.
            props:
            - name: url
              value: string
              description: |
                URL of the Git repository.
            - name: provider
              value: string
              description: |
                Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit.
          - name: resolved_commit
            value: string
            description: |
              The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time.
          - name: source_code_path
            value: string
            description: |
              Relative path to the app source code within the Git repository. If not specified, the root of the repository is used.
          - name: tag
            value: string
            description: |
              Git tag to checkout.
        - name: mode
          value: string
          description: |
            The mode of which the deployment will manage the source code.
        - name: source_code_path
          value: string
          description: |
            The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment.
        - name: status
          value: object
          description: |
            Status and status message of the deployment
          props:
          - name: message
            value: string
          - name: state
            value: string
            description: |
              State of the deployment.
        - name: update_time
          value: string
          description: |
            The update time of the deployment. Formatted timestamp in ISO 6801.
      - name: app_status
        value: object
        props:
        - name: message
          value: string
        - name: state
          value: string
          description: |
            State of the application.
      - name: budget_policy_id
        value: string
      - name: compute_size
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
      - name: compute_status
        value: object
        props:
        - name: active_instances
          value: integer
        - name: message
          value: string
          description: |
            Compute status message
        - name: state
          value: string
          description: |
            State of the app compute.
      - name: create_time
        value: string
        description: |
          The creation time of the app. Formatted timestamp in ISO 6801.
      - name: creator
        value: string
        description: |
          The email of the user that created the app.
      - name: default_source_code_path
        value: string
        description: |
          The default workspace file system path of the source code from which app deployment are created. This field tracks the workspace source code path of the last active deployment.
      - name: description
        value: string
        description: |
          The description of the app.
      - name: effective_budget_policy_id
        value: string
      - name: effective_usage_policy_id
        value: string
      - name: effective_user_api_scopes
        value: array
        description: |
          The effective api scopes granted to the user access token.
        items:
          type: string
      - name: git_repository
        value: object
        description: |
          Git repository configuration for app deployments. When specified, deployments can reference code from this repository by providing only the git reference (branch, tag, or commit).
        props:
        - name: url
          value: string
          description: |
            URL of the Git repository.
        - name: provider
          value: string
          description: |
            Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit.
      - name: id
        value: string
        description: |
          The unique identifier of the app.
      - name: oauth2_app_client_id
        value: string
      - name: oauth2_app_integration_id
        value: string
      - name: pending_deployment
        value: object
        description: |
          The pending deployment of the app. A deployment is considered pending when it is being prepared for deployment to the app compute.
        props:
        - name: command
          value: array
          items:
            type: string
        - name: create_time
          value: string
          description: |
            The creation time of the deployment. Formatted timestamp in ISO 6801.
        - name: creator
          value: string
          description: |
            The email of the user creates the deployment.
        - name: deployment_artifacts
          value: object
          description: |
            The deployment artifacts for an app.
          props:
          - name: source_code_path
            value: string
        - name: deployment_id
          value: string
          description: |
            The unique id of the deployment.
        - name: env_vars
          value: array
          description: |
            The environment variables to set in the app runtime environment. This will override the environment variables specified in the app.yaml file.
          props:
          - name: name
            value: string
          - name: value
            value: string
            description: |
              The value for the environment variable.
          - name: value_from
            value: string
            description: |
              The name of an external Databricks resource that contains the value, such as a secret or a database table.
        - name: git_source
          value: object
          description: |
            Git repository to use as the source for the app deployment.
          props:
          - name: branch
            value: string
            description: |
              Git branch to checkout.
          - name: commit
            value: string
            description: |
              Git commit SHA to checkout.
          - name: git_repository
            value: object
            description: |
              Git repository configuration. Populated from the app's git_repository configuration.
            props:
            - name: url
              value: string
              description: |
                URL of the Git repository.
            - name: provider
              value: string
              description: |
                Git provider. Case insensitive. Supported values: gitHub, gitHubEnterprise, bitbucketCloud, bitbucketServer, azureDevOpsServices, gitLab, gitLabEnterpriseEdition, awsCodeCommit.
          - name: resolved_commit
            value: string
            description: |
              The resolved commit SHA that was actually used for the deployment. This is populated by the system after resolving the reference (branch, tag, or commit). If commit is specified directly, this will match commit. If a branch or tag is specified, this contains the commit SHA that the branch or tag pointed to at deployment time.
          - name: source_code_path
            value: string
            description: |
              Relative path to the app source code within the Git repository. If not specified, the root of the repository is used.
          - name: tag
            value: string
            description: |
              Git tag to checkout.
        - name: mode
          value: string
          description: |
            The mode of which the deployment will manage the source code.
        - name: source_code_path
          value: string
          description: |
            The workspace file system path of the source code used to create the app deployment. This is different from `deployment_artifacts.source_code_path`, which is the path used by the deployed app. The former refers to the original source code location of the app in the workspace during deployment creation, whereas the latter provides a system generated stable snapshotted source code path used by the deployment.
        - name: status
          value: object
          description: |
            Status and status message of the deployment
          props:
          - name: message
            value: string
          - name: state
            value: string
            description: |
              State of the deployment.
        - name: update_time
          value: string
          description: |
            The update time of the deployment. Formatted timestamp in ISO 6801.
      - name: resources
        value: array
        description: |
          Resources for the app.
        props:
        - name: name
          value: string
        - name: database
          value: object
          props:
          - name: instance_name
            value: string
          - name: database_name
            value: string
          - name: permission
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
        - name: description
          value: string
          description: |
            Description of the App Resource.
        - name: experiment
          value: object
          props:
          - name: experiment_id
            value: string
          - name: permission
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
        - name: genie_space
          value: object
          props:
          - name: name
            value: string
          - name: space_id
            value: string
          - name: permission
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
        - name: job
          value: object
          props:
          - name: id
            value: string
          - name: permission
            value: string
            description: |
              Permissions to grant on the Job. Supported permissions are: "CAN_MANAGE", "IS_OWNER", "CAN_MANAGE_RUN", "CAN_VIEW".
        - name: secret
          value: object
          props:
          - name: scope
            value: string
          - name: key
            value: string
            description: |
              Key of the secret to grant permission on.
          - name: permission
            value: string
            description: |
              Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: "READ", "WRITE", "MANAGE".
        - name: serving_endpoint
          value: object
          props:
          - name: name
            value: string
          - name: permission
            value: string
            description: |
              Permission to grant on the serving endpoint. Supported permissions are: "CAN_MANAGE", "CAN_QUERY", "CAN_VIEW".
        - name: sql_warehouse
          value: object
          props:
          - name: id
            value: string
          - name: permission
            value: string
            description: |
              Permission to grant on the SQL warehouse. Supported permissions are: "CAN_MANAGE", "CAN_USE", "IS_OWNER".
        - name: uc_securable
          value: object
          props:
          - name: securable_full_name
            value: string
          - name: securable_type
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
          - name: permission
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
      - name: service_principal_client_id
        value: string
      - name: service_principal_id
        value: integer
      - name: service_principal_name
        value: string
      - name: update_time
        value: string
        description: |
          The update time of the app. Formatted timestamp in ISO 6801.
      - name: updater
        value: string
        description: |
          The email of the user that last updated the app.
      - name: url
        value: string
        description: |
          The URL of the app once it is deployed.
      - name: usage_policy_id
        value: string
      - name: user_api_scopes
        value: array
        items:
          type: string
    - name: no_compute
      value: boolean
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

Updates the app with the supplied name.

```sql
UPDATE databricks_workspace.apps.apps
SET 
app = '{{ app }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
AND app = '{{ app }}' --required
RETURNING
id,
name,
budget_policy_id,
effective_budget_policy_id,
effective_usage_policy_id,
oauth2_app_client_id,
oauth2_app_integration_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
active_deployment,
app_status,
compute_size,
compute_status,
create_time,
creator,
default_source_code_path,
description,
effective_user_api_scopes,
git_repository,
pending_deployment,
resources,
update_time,
updater,
url,
user_api_scopes;
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

Deletes an app.

```sql
DELETE FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Start the last active deployment of the app in the workspace.

```sql
EXEC databricks_workspace.apps.apps.start 
@name='{{ name }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops the active deployment of the app in the workspace.

```sql
EXEC databricks_workspace.apps.apps.stop 
@name='{{ name }}' --required, 
@workspace='{{ workspace }}' --required
;
```
</TabItem>
</Tabs>
