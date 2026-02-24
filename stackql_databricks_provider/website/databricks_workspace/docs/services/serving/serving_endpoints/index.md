---
title: serving_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_endpoints
  - serving
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

Creates, updates, deletes, gets or lists a <code>serving_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="serving_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.serving.serving_endpoints" /></td></tr>
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
    "description": "System-generated ID of the endpoint. This is used to refer to the endpoint in the Permissions API"
  },
  {
    "name": "name",
    "type": "string",
    "description": "The name of the serving endpoint."
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": "The budget policy associated with the endpoint."
  },
  {
    "name": "ai_gateway",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "fallback_config",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "guardrails",
        "type": "object",
        "description": "Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.",
        "children": [
          {
            "name": "input",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "invalid_keywords",
                "type": "array",
                "description": ""
              },
              {
                "name": "pii",
                "type": "object",
                "description": "Configuration for guardrail PII filter."
              },
              {
                "name": "safety",
                "type": "boolean",
                "description": "Indicates whether the safety filter is enabled."
              },
              {
                "name": "valid_topics",
                "type": "array",
                "description": "The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics."
              }
            ]
          },
          {
            "name": "output",
            "type": "object",
            "description": "Configuration for output guardrail filters.",
            "children": [
              {
                "name": "invalid_keywords",
                "type": "array",
                "description": ""
              },
              {
                "name": "pii",
                "type": "object",
                "description": "Configuration for guardrail PII filter."
              },
              {
                "name": "safety",
                "type": "boolean",
                "description": "Indicates whether the safety filter is enabled."
              },
              {
                "name": "valid_topics",
                "type": "array",
                "description": "The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics."
              }
            ]
          }
        ]
      },
      {
        "name": "inference_table_config",
        "type": "object",
        "description": "Configuration for payload logging using inference tables. Use these tables to monitor and audit data being sent to and received from model APIs and to improve model quality.",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "enabled",
            "type": "boolean",
            "description": "Indicates whether the inference table is enabled."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The name of the schema in Unity Catalog. Required when enabling inference tables. NOTE: On update, you have to disable inference table first in order to change the schema name."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "The prefix of the table in Unity Catalog. NOTE: On update, you have to disable inference table first in order to change the prefix name."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Configuration for rate limits which can be set to limit endpoint traffic.",
        "children": [
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (minute)"
          },
          {
            "name": "calls",
            "type": "integer",
            "description": "Used to specify how many calls are allowed for a key within the renewal_period."
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key field for a rate limit. Currently, 'user', 'user_group, 'service_principal', and 'endpoint' are supported, with 'endpoint' being the default if not specified. (endpoint, service_principal, user, user_group)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal field for a user, user group, or service principal to apply rate limiting to. Accepts a user email, group name, or service principal application ID."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Used to specify how many tokens are allowed for a key within the renewal_period."
          }
        ]
      },
      {
        "name": "usage_tracking_config",
        "type": "object",
        "description": "Configuration to enable usage tracking using system tables. These tables allow you to monitor operational usage on endpoints and their associated costs.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "config",
    "type": "object",
    "description": "The config that is currently being served by the endpoint.",
    "children": [
      {
        "name": "auto_capture_config",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "enabled",
            "type": "boolean",
            "description": "Indicates whether the inference table is enabled."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The name of the schema in Unity Catalog. NOTE: On update, you cannot change the schema name if the inference table is already enabled."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "payload_table",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "The prefix of the table in Unity Catalog. NOTE: On update, you cannot change the prefix name if the inference table is already enabled."
          }
        ]
      },
      {
        "name": "config_version",
        "type": "integer",
        "description": "The config version that the serving endpoint is currently serving."
      },
      {
        "name": "served_entities",
        "type": "array",
        "description": "The list of served entities under the serving endpoint config.",
        "children": [
          {
            "name": "burst_scaling_enabled",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "creation_timestamp",
            "type": "integer",
            "description": ""
          },
          {
            "name": "creator",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_name",
            "type": "string",
            "description": "The name of the entity to be served. The entity may be a model in the Databricks Model Registry, a model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC object, the full name of the object should be given in the form of **catalog_name.schema_name.model_name**."
          },
          {
            "name": "entity_version",
            "type": "string",
            "description": ""
          },
          {
            "name": "environment_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `&#123;\"OPENAI_API_KEY\": \"&#123;&#123;secrets/my_scope/my_key&#125;&#125;\", \"DATABRICKS_TOKEN\": \"&#123;&#123;secrets/my_scope2/my_key2&#125;&#125;\"&#125;`"
          },
          {
            "name": "external_model",
            "type": "object",
            "description": "The external model to be served. NOTE: Only one of external_model and (entity_name, entity_version, workload_size, workload_type, and scale_to_zero_enabled) can be specified with the latter set being used for custom model serving for a Databricks registered model. For an existing endpoint with external_model, it cannot be updated to an endpoint without external_model. If the endpoint is created without external_model, users cannot update it to add external_model later. The task type of all external models within an endpoint must be the same.",
            "children": [
              {
                "name": "provider",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ai21labs, amazon-bedrock, anthropic, cohere, custom, databricks-model-serving, google-cloud-vertex-ai, openai, palm)"
              },
              {
                "name": "name",
                "type": "string",
                "description": "The name of the external model."
              },
              {
                "name": "task",
                "type": "string",
                "description": "The task type of the external model."
              },
              {
                "name": "ai21labs_config",
                "type": "object",
                "description": "AI21Labs Config. Only required if the provider is 'ai21labs'."
              },
              {
                "name": "amazon_bedrock_config",
                "type": "object",
                "description": "Amazon Bedrock Config. Only required if the provider is 'amazon-bedrock'."
              },
              {
                "name": "anthropic_config",
                "type": "object",
                "description": "Anthropic Config. Only required if the provider is 'anthropic'."
              },
              {
                "name": "cohere_config",
                "type": "object",
                "description": "Cohere Config. Only required if the provider is 'cohere'."
              },
              {
                "name": "custom_provider_config",
                "type": "object",
                "description": "Custom Provider Config. Only required if the provider is 'custom'."
              },
              {
                "name": "databricks_model_serving_config",
                "type": "object",
                "description": "Databricks Model Serving Config. Only required if the provider is 'databricks-model-serving'."
              },
              {
                "name": "google_cloud_vertex_ai_config",
                "type": "object",
                "description": "Google Cloud Vertex AI Config. Only required if the provider is 'google-cloud-vertex-ai'."
              },
              {
                "name": "openai_config",
                "type": "object",
                "description": "OpenAI Config. Only required if the provider is 'openai'."
              },
              {
                "name": "palm_config",
                "type": "object",
                "description": "PaLM Config. Only required if the provider is 'palm'."
              }
            ]
          },
          {
            "name": "foundation_model",
            "type": "object",
            "description": "All fields are not sensitive as they are hard-coded in the system and made available to<br />    customers.",
            "children": [
              {
                "name": "description",
                "type": "string",
                "description": ""
              },
              {
                "name": "display_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "docs",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "ARN of the instance profile that the served entity uses to access AWS resources."
          },
          {
            "name": "max_provisioned_concurrency",
            "type": "integer",
            "description": "The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified."
          },
          {
            "name": "max_provisioned_throughput",
            "type": "integer",
            "description": "The maximum tokens per second that the endpoint can scale up to."
          },
          {
            "name": "min_provisioned_concurrency",
            "type": "integer",
            "description": "The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified."
          },
          {
            "name": "min_provisioned_throughput",
            "type": "integer",
            "description": "The minimum tokens per second that the endpoint can scale down to."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version."
          },
          {
            "name": "provisioned_model_units",
            "type": "integer",
            "description": "The number of model units provisioned."
          },
          {
            "name": "scale_to_zero_enabled",
            "type": "boolean",
            "description": "Whether the compute resources for the served entity should scale down to zero."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "deployment",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DEPLOYMENT_ABORTED, DEPLOYMENT_CREATING, DEPLOYMENT_FAILED, DEPLOYMENT_READY, DEPLOYMENT_RECOVERING)"
              },
              {
                "name": "deployment_state_message",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "workload_size",
            "type": "string",
            "description": "The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are \"Small\" (4 - 4 provisioned concurrency), \"Medium\" (8 - 16 provisioned concurrency), and \"Large\" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified."
          },
          {
            "name": "workload_type",
            "type": "string",
            "description": "The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is \"CPU\". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types (CPU, GPU_LARGE, GPU_MEDIUM, GPU_SMALL, MULTIGPU_MEDIUM)"
          }
        ]
      },
      {
        "name": "served_models",
        "type": "array",
        "description": "(Deprecated, use served_entities instead) The list of served models under the serving endpoint config.",
        "children": [
          {
            "name": "burst_scaling_enabled",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "creation_timestamp",
            "type": "integer",
            "description": ""
          },
          {
            "name": "creator",
            "type": "string",
            "description": ""
          },
          {
            "name": "environment_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `&#123;\"OPENAI_API_KEY\": \"&#123;&#123;secrets/my_scope/my_key&#125;&#125;\", \"DATABRICKS_TOKEN\": \"&#123;&#123;secrets/my_scope2/my_key2&#125;&#125;\"&#125;`"
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "ARN of the instance profile that the served entity uses to access AWS resources."
          },
          {
            "name": "max_provisioned_concurrency",
            "type": "integer",
            "description": "The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified."
          },
          {
            "name": "min_provisioned_concurrency",
            "type": "integer",
            "description": "The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified."
          },
          {
            "name": "model_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "model_version",
            "type": "string",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version."
          },
          {
            "name": "provisioned_model_units",
            "type": "integer",
            "description": "The number of model units provisioned."
          },
          {
            "name": "scale_to_zero_enabled",
            "type": "boolean",
            "description": "Whether the compute resources for the served entity should scale down to zero."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "deployment",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DEPLOYMENT_ABORTED, DEPLOYMENT_CREATING, DEPLOYMENT_FAILED, DEPLOYMENT_READY, DEPLOYMENT_RECOVERING)"
              },
              {
                "name": "deployment_state_message",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "workload_size",
            "type": "string",
            "description": "The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are \"Small\" (4 - 4 provisioned concurrency), \"Medium\" (8 - 16 provisioned concurrency), and \"Large\" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified."
          },
          {
            "name": "workload_type",
            "type": "string",
            "description": "The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is \"CPU\". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types (CPU, GPU_LARGE, GPU_MEDIUM, GPU_SMALL, MULTIGPU_MEDIUM)"
          }
        ]
      },
      {
        "name": "traffic_config",
        "type": "object",
        "description": "The traffic configuration associated with the serving endpoint config.",
        "children": [
          {
            "name": "routes",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": ""
              },
              {
                "name": "served_entity_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "served_model_name",
                "type": "string",
                "description": "The name of the served model this route configures traffic for."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": "The timestamp when the endpoint was created in Unix time."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user who created the serving endpoint."
  },
  {
    "name": "data_plane_info",
    "type": "object",
    "description": "Information required to query DataPlane APIs.",
    "children": [
      {
        "name": "query_info",
        "type": "object",
        "description": "Information required to query DataPlane API 'query' endpoint.",
        "children": [
          {
            "name": "authorization_details",
            "type": "string",
            "description": "Authorization details as a string."
          },
          {
            "name": "endpoint_url",
            "type": "string",
            "description": "The URL of the endpoint for this operation in the dataplane."
          }
        ]
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the serving model"
  },
  {
    "name": "email_notifications",
    "type": "object",
    "description": "Email notification settings.",
    "children": [
      {
        "name": "on_update_failure",
        "type": "array",
        "description": ""
      },
      {
        "name": "on_update_success",
        "type": "array",
        "description": "A list of email addresses to be notified when an endpoint successfully updates its configuration or state."
      }
    ]
  },
  {
    "name": "endpoint_url",
    "type": "string",
    "description": "Endpoint invocation url if route optimization is enabled for endpoint"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "The timestamp when the endpoint was last updated by a user in Unix time."
  },
  {
    "name": "pending_config",
    "type": "object",
    "description": "The config that the endpoint is attempting to update to.",
    "children": [
      {
        "name": "auto_capture_config",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "enabled",
            "type": "boolean",
            "description": "Indicates whether the inference table is enabled."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The name of the schema in Unity Catalog. NOTE: On update, you cannot change the schema name if the inference table is already enabled."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "payload_table",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "The prefix of the table in Unity Catalog. NOTE: On update, you cannot change the prefix name if the inference table is already enabled."
          }
        ]
      },
      {
        "name": "config_version",
        "type": "integer",
        "description": "The config version that the serving endpoint is currently serving."
      },
      {
        "name": "served_entities",
        "type": "array",
        "description": "The list of served entities belonging to the last issued update to the serving endpoint.",
        "children": [
          {
            "name": "burst_scaling_enabled",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "creation_timestamp",
            "type": "integer",
            "description": ""
          },
          {
            "name": "creator",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_name",
            "type": "string",
            "description": "The name of the entity to be served. The entity may be a model in the Databricks Model Registry, a model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC object, the full name of the object should be given in the form of **catalog_name.schema_name.model_name**."
          },
          {
            "name": "entity_version",
            "type": "string",
            "description": ""
          },
          {
            "name": "environment_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `&#123;\"OPENAI_API_KEY\": \"&#123;&#123;secrets/my_scope/my_key&#125;&#125;\", \"DATABRICKS_TOKEN\": \"&#123;&#123;secrets/my_scope2/my_key2&#125;&#125;\"&#125;`"
          },
          {
            "name": "external_model",
            "type": "object",
            "description": "The external model to be served. NOTE: Only one of external_model and (entity_name, entity_version, workload_size, workload_type, and scale_to_zero_enabled) can be specified with the latter set being used for custom model serving for a Databricks registered model. For an existing endpoint with external_model, it cannot be updated to an endpoint without external_model. If the endpoint is created without external_model, users cannot update it to add external_model later. The task type of all external models within an endpoint must be the same.",
            "children": [
              {
                "name": "provider",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ai21labs, amazon-bedrock, anthropic, cohere, custom, databricks-model-serving, google-cloud-vertex-ai, openai, palm)"
              },
              {
                "name": "name",
                "type": "string",
                "description": "The name of the external model."
              },
              {
                "name": "task",
                "type": "string",
                "description": "The task type of the external model."
              },
              {
                "name": "ai21labs_config",
                "type": "object",
                "description": "AI21Labs Config. Only required if the provider is 'ai21labs'."
              },
              {
                "name": "amazon_bedrock_config",
                "type": "object",
                "description": "Amazon Bedrock Config. Only required if the provider is 'amazon-bedrock'."
              },
              {
                "name": "anthropic_config",
                "type": "object",
                "description": "Anthropic Config. Only required if the provider is 'anthropic'."
              },
              {
                "name": "cohere_config",
                "type": "object",
                "description": "Cohere Config. Only required if the provider is 'cohere'."
              },
              {
                "name": "custom_provider_config",
                "type": "object",
                "description": "Custom Provider Config. Only required if the provider is 'custom'."
              },
              {
                "name": "databricks_model_serving_config",
                "type": "object",
                "description": "Databricks Model Serving Config. Only required if the provider is 'databricks-model-serving'."
              },
              {
                "name": "google_cloud_vertex_ai_config",
                "type": "object",
                "description": "Google Cloud Vertex AI Config. Only required if the provider is 'google-cloud-vertex-ai'."
              },
              {
                "name": "openai_config",
                "type": "object",
                "description": "OpenAI Config. Only required if the provider is 'openai'."
              },
              {
                "name": "palm_config",
                "type": "object",
                "description": "PaLM Config. Only required if the provider is 'palm'."
              }
            ]
          },
          {
            "name": "foundation_model",
            "type": "object",
            "description": "All fields are not sensitive as they are hard-coded in the system and made available to<br />    customers.",
            "children": [
              {
                "name": "description",
                "type": "string",
                "description": ""
              },
              {
                "name": "display_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "docs",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "ARN of the instance profile that the served entity uses to access AWS resources."
          },
          {
            "name": "max_provisioned_concurrency",
            "type": "integer",
            "description": "The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified."
          },
          {
            "name": "max_provisioned_throughput",
            "type": "integer",
            "description": "The maximum tokens per second that the endpoint can scale up to."
          },
          {
            "name": "min_provisioned_concurrency",
            "type": "integer",
            "description": "The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified."
          },
          {
            "name": "min_provisioned_throughput",
            "type": "integer",
            "description": "The minimum tokens per second that the endpoint can scale down to."
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version."
          },
          {
            "name": "provisioned_model_units",
            "type": "integer",
            "description": "The number of model units provisioned."
          },
          {
            "name": "scale_to_zero_enabled",
            "type": "boolean",
            "description": "Whether the compute resources for the served entity should scale down to zero."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "deployment",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DEPLOYMENT_ABORTED, DEPLOYMENT_CREATING, DEPLOYMENT_FAILED, DEPLOYMENT_READY, DEPLOYMENT_RECOVERING)"
              },
              {
                "name": "deployment_state_message",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "workload_size",
            "type": "string",
            "description": "The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are \"Small\" (4 - 4 provisioned concurrency), \"Medium\" (8 - 16 provisioned concurrency), and \"Large\" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified."
          },
          {
            "name": "workload_type",
            "type": "string",
            "description": "The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is \"CPU\". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types (CPU, GPU_LARGE, GPU_MEDIUM, GPU_SMALL, MULTIGPU_MEDIUM)"
          }
        ]
      },
      {
        "name": "served_models",
        "type": "array",
        "description": "(Deprecated, use served_entities instead) The list of served models belonging to the last issued update to the serving endpoint.",
        "children": [
          {
            "name": "burst_scaling_enabled",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "creation_timestamp",
            "type": "integer",
            "description": ""
          },
          {
            "name": "creator",
            "type": "string",
            "description": ""
          },
          {
            "name": "environment_vars",
            "type": "object",
            "description": "An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `&#123;\"OPENAI_API_KEY\": \"&#123;&#123;secrets/my_scope/my_key&#125;&#125;\", \"DATABRICKS_TOKEN\": \"&#123;&#123;secrets/my_scope2/my_key2&#125;&#125;\"&#125;`"
          },
          {
            "name": "instance_profile_arn",
            "type": "string",
            "description": "ARN of the instance profile that the served entity uses to access AWS resources."
          },
          {
            "name": "max_provisioned_concurrency",
            "type": "integer",
            "description": "The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified."
          },
          {
            "name": "min_provisioned_concurrency",
            "type": "integer",
            "description": "The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified."
          },
          {
            "name": "model_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "model_version",
            "type": "string",
            "description": ""
          },
          {
            "name": "name",
            "type": "string",
            "description": "The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version."
          },
          {
            "name": "provisioned_model_units",
            "type": "integer",
            "description": "The number of model units provisioned."
          },
          {
            "name": "scale_to_zero_enabled",
            "type": "boolean",
            "description": "Whether the compute resources for the served entity should scale down to zero."
          },
          {
            "name": "state",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "deployment",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (DEPLOYMENT_ABORTED, DEPLOYMENT_CREATING, DEPLOYMENT_FAILED, DEPLOYMENT_READY, DEPLOYMENT_RECOVERING)"
              },
              {
                "name": "deployment_state_message",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "workload_size",
            "type": "string",
            "description": "The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are \"Small\" (4 - 4 provisioned concurrency), \"Medium\" (8 - 16 provisioned concurrency), and \"Large\" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified."
          },
          {
            "name": "workload_type",
            "type": "string",
            "description": "The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is \"CPU\". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types (CPU, GPU_LARGE, GPU_MEDIUM, GPU_SMALL, MULTIGPU_MEDIUM)"
          }
        ]
      },
      {
        "name": "start_time",
        "type": "integer",
        "description": "The timestamp when the update to the pending config started."
      },
      {
        "name": "traffic_config",
        "type": "object",
        "description": "The traffic config defining how invocations to the serving endpoint should be routed.",
        "children": [
          {
            "name": "routes",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": ""
              },
              {
                "name": "served_entity_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "served_model_name",
                "type": "string",
                "description": "The name of the served model this route configures traffic for."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "permission_level",
    "type": "string",
    "description": "The permission level of the principal making the request. (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
  },
  {
    "name": "route_optimized",
    "type": "boolean",
    "description": "Boolean representing if route optimization has been enabled for the endpoint"
  },
  {
    "name": "state",
    "type": "object",
    "description": "Information corresponding to the state of the serving endpoint.",
    "children": [
      {
        "name": "config_update",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN_PROGRESS, NOT_UPDATING, UPDATE_CANCELED, UPDATE_FAILED)"
      },
      {
        "name": "ready",
        "type": "string",
        "description": "The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is READY if all of the served entities in its active configuration are ready. If any of the actively served entities are in a non-ready state, the endpoint state will be NOT_READY. (NOT_READY, READY)"
      }
    ]
  },
  {
    "name": "tags",
    "type": "array",
    "description": "Tags attached to the serving endpoint.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "Optional value field for a serving endpoint tag."
      }
    ]
  },
  {
    "name": "task",
    "type": "string",
    "description": "The task type of the serving endpoint."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "System-generated ID of the endpoint, included to be used by the Permissions API."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The name of the serving endpoint."
  },
  {
    "name": "budget_policy_id",
    "type": "string",
    "description": "The budget policy associated with the endpoint."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy associated with serving endpoint."
  },
  {
    "name": "ai_gateway",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "fallback_config",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "guardrails",
        "type": "object",
        "description": "Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.",
        "children": [
          {
            "name": "input",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "invalid_keywords",
                "type": "array",
                "description": ""
              },
              {
                "name": "pii",
                "type": "object",
                "description": "Configuration for guardrail PII filter."
              },
              {
                "name": "safety",
                "type": "boolean",
                "description": "Indicates whether the safety filter is enabled."
              },
              {
                "name": "valid_topics",
                "type": "array",
                "description": "The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics."
              }
            ]
          },
          {
            "name": "output",
            "type": "object",
            "description": "Configuration for output guardrail filters.",
            "children": [
              {
                "name": "invalid_keywords",
                "type": "array",
                "description": ""
              },
              {
                "name": "pii",
                "type": "object",
                "description": "Configuration for guardrail PII filter."
              },
              {
                "name": "safety",
                "type": "boolean",
                "description": "Indicates whether the safety filter is enabled."
              },
              {
                "name": "valid_topics",
                "type": "array",
                "description": "The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics."
              }
            ]
          }
        ]
      },
      {
        "name": "inference_table_config",
        "type": "object",
        "description": "Configuration for payload logging using inference tables. Use these tables to monitor and audit data being sent to and received from model APIs and to improve model quality.",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "enabled",
            "type": "boolean",
            "description": "Indicates whether the inference table is enabled."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The name of the schema in Unity Catalog. Required when enabling inference tables. NOTE: On update, you have to disable inference table first in order to change the schema name."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "The prefix of the table in Unity Catalog. NOTE: On update, you have to disable inference table first in order to change the prefix name."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Configuration for rate limits which can be set to limit endpoint traffic.",
        "children": [
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (minute)"
          },
          {
            "name": "calls",
            "type": "integer",
            "description": "Used to specify how many calls are allowed for a key within the renewal_period."
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key field for a rate limit. Currently, 'user', 'user_group, 'service_principal', and 'endpoint' are supported, with 'endpoint' being the default if not specified. (endpoint, service_principal, user, user_group)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal field for a user, user group, or service principal to apply rate limiting to. Accepts a user email, group name, or service principal application ID."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Used to specify how many tokens are allowed for a key within the renewal_period."
          }
        ]
      },
      {
        "name": "usage_tracking_config",
        "type": "object",
        "description": "Configuration to enable usage tracking using system tables. These tables allow you to monitor operational usage on endpoints and their associated costs.",
        "children": [
          {
            "name": "enabled",
            "type": "boolean",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "config",
    "type": "object",
    "description": "The config that is currently being served by the endpoint.",
    "children": [
      {
        "name": "served_entities",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "entity_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_version",
            "type": "string",
            "description": ""
          },
          {
            "name": "external_model",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "provider",
                "type": "string",
                "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (ai21labs, amazon-bedrock, anthropic, cohere, custom, databricks-model-serving, google-cloud-vertex-ai, openai, palm)"
              },
              {
                "name": "name",
                "type": "string",
                "description": "The name of the external model."
              },
              {
                "name": "task",
                "type": "string",
                "description": "The task type of the external model."
              },
              {
                "name": "ai21labs_config",
                "type": "object",
                "description": "AI21Labs Config. Only required if the provider is 'ai21labs'."
              },
              {
                "name": "amazon_bedrock_config",
                "type": "object",
                "description": "Amazon Bedrock Config. Only required if the provider is 'amazon-bedrock'."
              },
              {
                "name": "anthropic_config",
                "type": "object",
                "description": "Anthropic Config. Only required if the provider is 'anthropic'."
              },
              {
                "name": "cohere_config",
                "type": "object",
                "description": "Cohere Config. Only required if the provider is 'cohere'."
              },
              {
                "name": "custom_provider_config",
                "type": "object",
                "description": "Custom Provider Config. Only required if the provider is 'custom'."
              },
              {
                "name": "databricks_model_serving_config",
                "type": "object",
                "description": "Databricks Model Serving Config. Only required if the provider is 'databricks-model-serving'."
              },
              {
                "name": "google_cloud_vertex_ai_config",
                "type": "object",
                "description": "Google Cloud Vertex AI Config. Only required if the provider is 'google-cloud-vertex-ai'."
              },
              {
                "name": "openai_config",
                "type": "object",
                "description": "OpenAI Config. Only required if the provider is 'openai'."
              },
              {
                "name": "palm_config",
                "type": "object",
                "description": "PaLM Config. Only required if the provider is 'palm'."
              }
            ]
          },
          {
            "name": "foundation_model",
            "type": "object",
            "description": "All fields are not sensitive as they are hard-coded in the system and made available to<br />    customers.",
            "children": [
              {
                "name": "description",
                "type": "string",
                "description": ""
              },
              {
                "name": "display_name",
                "type": "string",
                "description": ""
              },
              {
                "name": "docs",
                "type": "string",
                "description": ""
              },
              {
                "name": "name",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "name",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "served_models",
        "type": "array",
        "description": "(Deprecated, use served_entities instead) The list of served models under the serving endpoint config.",
        "children": [
          {
            "name": "model_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "model_version",
            "type": "string",
            "description": "Only one of model_version and entity_version should be populated"
          },
          {
            "name": "name",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "creation_timestamp",
    "type": "integer",
    "description": "The timestamp when the endpoint was created in Unix time."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user who created the serving endpoint."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the endpoint"
  },
  {
    "name": "last_updated_timestamp",
    "type": "integer",
    "description": "The timestamp when the endpoint was last updated by a user in Unix time."
  },
  {
    "name": "state",
    "type": "object",
    "description": "Information corresponding to the state of the serving endpoint.",
    "children": [
      {
        "name": "config_update",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access::<br /><br />&gt;&gt;&gt; Color.RED<br />&lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />&gt;&gt;&gt; Color(1)<br />&lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />&gt;&gt;&gt; Color['RED']<br />&lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (IN_PROGRESS, NOT_UPDATING, UPDATE_CANCELED, UPDATE_FAILED)"
      },
      {
        "name": "ready",
        "type": "string",
        "description": "The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is READY if all of the served entities in its active configuration are ready. If any of the actively served entities are in a non-ready state, the endpoint state will be NOT_READY. (NOT_READY, READY)"
      }
    ]
  },
  {
    "name": "tags",
    "type": "array",
    "description": "Tags attached to the serving endpoint.",
    "children": [
      {
        "name": "key",
        "type": "string",
        "description": ""
      },
      {
        "name": "value",
        "type": "string",
        "description": "Optional value field for a serving endpoint tag."
      }
    ]
  },
  {
    "name": "task",
    "type": "string",
    "description": "The task type of the serving endpoint."
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
    <td>Retrieves the details for a single serving endpoint.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Get all serving endpoints.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace"><code>workspace</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a new serving endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Used to batch add and delete tags from a serving endpoint with a single API call.</td>
</tr>
<tr>
    <td><a href="#update_config"><CopyableCode code="update_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Updates any combination of the serving endpoint's served entities, the compute configuration of those</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Delete a serving endpoint.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workspace"><code>workspace</code></a></td>
    <td></td>
    <td>Query a serving endpoint</td>
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
    <td>The name of the serving endpoint. This field is required and is provided via the path parameter.</td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details for a single serving endpoint.

```sql
SELECT
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task
FROM databricks_workspace.serving.serving_endpoints
WHERE name = '{{ name }}' -- required
AND workspace = '{{ workspace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all serving endpoints.

```sql
SELECT
id,
name,
budget_policy_id,
usage_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
description,
last_updated_timestamp,
state,
tags,
task
FROM databricks_workspace.serving.serving_endpoints
WHERE workspace = '{{ workspace }}' -- required
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

Create a new serving endpoint.

```sql
INSERT INTO databricks_workspace.serving.serving_endpoints (
name,
ai_gateway,
budget_policy_id,
config,
description,
email_notifications,
rate_limits,
route_optimized,
tags,
workspace
)
SELECT 
'{{ name }}' /* required */,
'{{ ai_gateway }}',
'{{ budget_policy_id }}',
'{{ config }}',
'{{ description }}',
'{{ email_notifications }}',
'{{ rate_limits }}',
{{ route_optimized }},
'{{ tags }}',
'{{ workspace }}'
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: serving_endpoints
  props:
    - name: workspace
      value: string
      description: Required parameter for the serving_endpoints resource.
    - name: name
      value: string
      description: |
        The name of the serving endpoint. This field is required and must be unique across a Databricks workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
    - name: ai_gateway
      value: object
      description: |
        The AI Gateway configuration for the serving endpoint. NOTE: External model, provisioned throughput, and pay-per-token endpoints are fully supported; agent endpoints currently only support inference tables.
      props:
      - name: fallback_config
        value: object
        props:
        - name: enabled
          value: boolean
      - name: guardrails
        value: object
        description: |
          Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.
        props:
        - name: input
          value: object
          props:
          - name: invalid_keywords
            value: array
            items:
              type: string
          - name: pii
            value: object
            description: |
              Configuration for guardrail PII filter.
            props:
            - name: behavior
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
          - name: safety
            value: boolean
            description: |
              Indicates whether the safety filter is enabled.
          - name: valid_topics
            value: array
            description: |
              The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics.
            items:
              type: string
        - name: output
          value: object
          description: |
            Configuration for output guardrail filters.
          props:
          - name: invalid_keywords
            value: array
            items:
              type: string
          - name: pii
            value: object
            description: |
              Configuration for guardrail PII filter.
            props:
            - name: behavior
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
          - name: safety
            value: boolean
            description: |
              Indicates whether the safety filter is enabled.
          - name: valid_topics
            value: array
            description: |
              The list of allowed topics. Given a chat request, this guardrail flags the request if its topic is not in the allowed topics.
            items:
              type: string
      - name: inference_table_config
        value: object
        description: |
          Configuration for payload logging using inference tables. Use these tables to monitor and audit data being sent to and received from model APIs and to improve model quality.
        props:
        - name: catalog_name
          value: string
        - name: enabled
          value: boolean
          description: |
            Indicates whether the inference table is enabled.
        - name: schema_name
          value: string
          description: |
            The name of the schema in Unity Catalog. Required when enabling inference tables. NOTE: On update, you have to disable inference table first in order to change the schema name.
        - name: table_name_prefix
          value: string
          description: |
            The prefix of the table in Unity Catalog. NOTE: On update, you have to disable inference table first in order to change the prefix name.
      - name: rate_limits
        value: array
        description: |
          Configuration for rate limits which can be set to limit endpoint traffic.
        props:
        - name: renewal_period
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
        - name: calls
          value: integer
          description: |
            Used to specify how many calls are allowed for a key within the renewal_period.
        - name: key
          value: string
          description: |
            Key field for a rate limit. Currently, 'user', 'user_group, 'service_principal', and 'endpoint' are supported, with 'endpoint' being the default if not specified.
        - name: principal
          value: string
          description: |
            Principal field for a user, user group, or service principal to apply rate limiting to. Accepts a user email, group name, or service principal application ID.
        - name: tokens
          value: integer
          description: |
            Used to specify how many tokens are allowed for a key within the renewal_period.
      - name: usage_tracking_config
        value: object
        description: |
          Configuration to enable usage tracking using system tables. These tables allow you to monitor operational usage on endpoints and their associated costs.
        props:
        - name: enabled
          value: boolean
    - name: budget_policy_id
      value: string
      description: |
        The budget policy to be applied to the serving endpoint.
    - name: config
      value: object
      description: |
        The core config of the serving endpoint.
      props:
      - name: name
        value: string
      - name: auto_capture_config
        value: object
        description: |
          Configuration for Inference Tables which automatically logs requests and responses to Unity Catalog. Note: this field is deprecated for creating new provisioned throughput endpoints, or updating existing provisioned throughput endpoints that never have inference table configured; in these cases please use AI Gateway to manage inference tables.
        props:
        - name: catalog_name
          value: string
        - name: enabled
          value: boolean
          description: |
            Indicates whether the inference table is enabled.
        - name: schema_name
          value: string
          description: |
            The name of the schema in Unity Catalog. NOTE: On update, you cannot change the schema name if the inference table is already enabled.
        - name: table_name_prefix
          value: string
          description: |
            The prefix of the table in Unity Catalog. NOTE: On update, you cannot change the prefix name if the inference table is already enabled.
      - name: served_entities
        value: array
        description: |
          The list of served entities under the serving endpoint config.
        props:
        - name: burst_scaling_enabled
          value: boolean
        - name: entity_name
          value: string
          description: |
            The name of the entity to be served. The entity may be a model in the Databricks Model Registry, a model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC object, the full name of the object should be given in the form of **catalog_name.schema_name.model_name**.
        - name: entity_version
          value: string
        - name: environment_vars
          value: object
          description: |
            An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY": "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`
        - name: external_model
          value: object
          description: |
            The external model to be served. NOTE: Only one of external_model and (entity_name, entity_version, workload_size, workload_type, and scale_to_zero_enabled) can be specified with the latter set being used for custom model serving for a Databricks registered model. For an existing endpoint with external_model, it cannot be updated to an endpoint without external_model. If the endpoint is created without external_model, users cannot update it to add external_model later. The task type of all external models within an endpoint must be the same.
          props:
          - name: provider
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
          - name: name
            value: string
            description: |
              The name of the external model.
          - name: task
            value: string
            description: |
              The task type of the external model.
          - name: ai21labs_config
            value: object
            description: |
              AI21Labs Config. Only required if the provider is 'ai21labs'.
            props:
            - name: ai21labs_api_key
              value: string
            - name: ai21labs_api_key_plaintext
              value: string
              description: |
                An AI21 Labs API key provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `ai21labs_api_key`. You must provide an API key using one of the following fields: `ai21labs_api_key` or `ai21labs_api_key_plaintext`.
          - name: amazon_bedrock_config
            value: object
            description: |
              Amazon Bedrock Config. Only required if the provider is 'amazon-bedrock'.
            props:
            - name: aws_region
              value: string
            - name: bedrock_provider
              value: string
              description: |
                The underlying provider in Amazon Bedrock. Supported values (case insensitive) include: Anthropic, Cohere, AI21Labs, Amazon.
            - name: aws_access_key_id
              value: string
              description: |
                The Databricks secret key reference for an AWS access key ID with permissions to interact with Bedrock services. If you prefer to paste your API key directly, see `aws_access_key_id_plaintext`. You must provide an API key using one of the following fields: `aws_access_key_id` or `aws_access_key_id_plaintext`.
            - name: aws_access_key_id_plaintext
              value: string
              description: |
                An AWS access key ID with permissions to interact with Bedrock services provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `aws_access_key_id`. You must provide an API key using one of the following fields: `aws_access_key_id` or `aws_access_key_id_plaintext`.
            - name: aws_secret_access_key
              value: string
              description: |
                The Databricks secret key reference for an AWS secret access key paired with the access key ID, with permissions to interact with Bedrock services. If you prefer to paste your API key directly, see `aws_secret_access_key_plaintext`. You must provide an API key using one of the following fields: `aws_secret_access_key` or `aws_secret_access_key_plaintext`.
            - name: aws_secret_access_key_plaintext
              value: string
              description: |
                An AWS secret access key paired with the access key ID, with permissions to interact with Bedrock services provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `aws_secret_access_key`. You must provide an API key using one of the following fields: `aws_secret_access_key` or `aws_secret_access_key_plaintext`.
            - name: instance_profile_arn
              value: string
              description: |
                ARN of the instance profile that the external model will use to access AWS resources. You must authenticate using an instance profile or access keys. If you prefer to authenticate using access keys, see `aws_access_key_id`, `aws_access_key_id_plaintext`, `aws_secret_access_key` and `aws_secret_access_key_plaintext`.
          - name: anthropic_config
            value: object
            description: |
              Anthropic Config. Only required if the provider is 'anthropic'.
            props:
            - name: anthropic_api_key
              value: string
            - name: anthropic_api_key_plaintext
              value: string
              description: |
                The Anthropic API key provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `anthropic_api_key`. You must provide an API key using one of the following fields: `anthropic_api_key` or `anthropic_api_key_plaintext`.
          - name: cohere_config
            value: object
            description: |
              Cohere Config. Only required if the provider is 'cohere'.
            props:
            - name: cohere_api_base
              value: string
            - name: cohere_api_key
              value: string
              description: |
                The Databricks secret key reference for a Cohere API key. If you prefer to paste your API key directly, see `cohere_api_key_plaintext`. You must provide an API key using one of the following fields: `cohere_api_key` or `cohere_api_key_plaintext`.
            - name: cohere_api_key_plaintext
              value: string
              description: |
                The Cohere API key provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `cohere_api_key`. You must provide an API key using one of the following fields: `cohere_api_key` or `cohere_api_key_plaintext`.
          - name: custom_provider_config
            value: object
            description: |
              Custom Provider Config. Only required if the provider is 'custom'.
            props:
            - name: custom_provider_url
              value: string
              description: |
                This is a field to provide the URL of the custom provider API.
            - name: api_key_auth
              value: object
              description: |
                This is a field to provide API key authentication for the custom provider API. You can only specify one authentication method.
            - name: bearer_token_auth
              value: object
              description: |
                This is a field to provide bearer token authentication for the custom provider API. You can only specify one authentication method.
          - name: databricks_model_serving_config
            value: object
            description: |
              Databricks Model Serving Config. Only required if the provider is 'databricks-model-serving'.
            props:
            - name: databricks_workspace_url
              value: string
            - name: databricks_api_token
              value: string
              description: |
                The Databricks secret key reference for a Databricks API token that corresponds to a user or service principal with Can Query access to the model serving endpoint pointed to by this external model. If you prefer to paste your API key directly, see `databricks_api_token_plaintext`. You must provide an API key using one of the following fields: `databricks_api_token` or `databricks_api_token_plaintext`.
            - name: databricks_api_token_plaintext
              value: string
              description: |
                The Databricks API token that corresponds to a user or service principal with Can Query access to the model serving endpoint pointed to by this external model provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `databricks_api_token`. You must provide an API key using one of the following fields: `databricks_api_token` or `databricks_api_token_plaintext`.
          - name: google_cloud_vertex_ai_config
            value: object
            description: |
              Google Cloud Vertex AI Config. Only required if the provider is 'google-cloud-vertex-ai'.
            props:
            - name: project_id
              value: string
            - name: region
              value: string
              description: |
                This is the region for the Google Cloud Vertex AI Service. See [supported regions] for more details. Some models are only available in specific regions. [supported regions]: https://cloud.google.com/vertex-ai/docs/general/locations
            - name: private_key
              value: string
              description: |
                The Databricks secret key reference for a private key for the service account which has access to the Google Cloud Vertex AI Service. See [Best practices for managing service account keys]. If you prefer to paste your API key directly, see `private_key_plaintext`. You must provide an API key using one of the following fields: `private_key` or `private_key_plaintext` [Best practices for managing service account keys]: https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys
            - name: private_key_plaintext
              value: string
              description: |
                The private key for the service account which has access to the Google Cloud Vertex AI Service provided as a plaintext secret. See [Best practices for managing service account keys]. If you prefer to reference your key using Databricks Secrets, see `private_key`. You must provide an API key using one of the following fields: `private_key` or `private_key_plaintext`. [Best practices for managing service account keys]: https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys
          - name: openai_config
            value: object
            description: |
              OpenAI Config. Only required if the provider is 'openai'.
            props:
            - name: microsoft_entra_client_id
              value: string
              description: |
                This field is only required for Azure AD OpenAI and is the Microsoft Entra Client ID.
            - name: microsoft_entra_client_secret
              value: string
              description: |
                The Databricks secret key reference for a client secret used for Microsoft Entra ID authentication. If you prefer to paste your client secret directly, see `microsoft_entra_client_secret_plaintext`. You must provide an API key using one of the following fields: `microsoft_entra_client_secret` or `microsoft_entra_client_secret_plaintext`.
            - name: microsoft_entra_client_secret_plaintext
              value: string
              description: |
                The client secret used for Microsoft Entra ID authentication provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `microsoft_entra_client_secret`. You must provide an API key using one of the following fields: `microsoft_entra_client_secret` or `microsoft_entra_client_secret_plaintext`.
            - name: microsoft_entra_tenant_id
              value: string
              description: |
                This field is only required for Azure AD OpenAI and is the Microsoft Entra Tenant ID.
            - name: openai_api_base
              value: string
              description: |
                This is a field to provide a customized base URl for the OpenAI API. For Azure OpenAI, this field is required, and is the base URL for the Azure OpenAI API service provided by Azure. For other OpenAI API types, this field is optional, and if left unspecified, the standard OpenAI base URL is used.
            - name: openai_api_key
              value: string
              description: |
                The Databricks secret key reference for an OpenAI API key using the OpenAI or Azure service. If you prefer to paste your API key directly, see `openai_api_key_plaintext`. You must provide an API key using one of the following fields: `openai_api_key` or `openai_api_key_plaintext`.
            - name: openai_api_key_plaintext
              value: string
              description: |
                The OpenAI API key using the OpenAI or Azure service provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `openai_api_key`. You must provide an API key using one of the following fields: `openai_api_key` or `openai_api_key_plaintext`.
            - name: openai_api_type
              value: string
              description: |
                This is an optional field to specify the type of OpenAI API to use. For Azure OpenAI, this field is required, and adjust this parameter to represent the preferred security access validation protocol. For access token validation, use azure. For authentication using Azure Active Directory (Azure AD) use, azuread.
            - name: openai_api_version
              value: string
              description: |
                This is an optional field to specify the OpenAI API version. For Azure OpenAI, this field is required, and is the version of the Azure OpenAI service to utilize, specified by a date.
            - name: openai_deployment_name
              value: string
              description: |
                This field is only required for Azure OpenAI and is the name of the deployment resource for the Azure OpenAI service.
            - name: openai_organization
              value: string
              description: |
                This is an optional field to specify the organization in OpenAI or Azure OpenAI.
          - name: palm_config
            value: object
            description: |
              PaLM Config. Only required if the provider is 'palm'.
            props:
            - name: palm_api_key
              value: string
            - name: palm_api_key_plaintext
              value: string
              description: |
                The PaLM API key provided as a plaintext string. If you prefer to reference your key using Databricks Secrets, see `palm_api_key`. You must provide an API key using one of the following fields: `palm_api_key` or `palm_api_key_plaintext`.
        - name: instance_profile_arn
          value: string
          description: |
            ARN of the instance profile that the served entity uses to access AWS resources.
        - name: max_provisioned_concurrency
          value: integer
          description: |
            The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified.
        - name: max_provisioned_throughput
          value: integer
          description: |
            The maximum tokens per second that the endpoint can scale up to.
        - name: min_provisioned_concurrency
          value: integer
          description: |
            The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified.
        - name: min_provisioned_throughput
          value: integer
          description: |
            The minimum tokens per second that the endpoint can scale down to.
        - name: name
          value: string
          description: |
            The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version.
        - name: provisioned_model_units
          value: integer
          description: |
            The number of model units provisioned.
        - name: scale_to_zero_enabled
          value: boolean
          description: |
            Whether the compute resources for the served entity should scale down to zero.
        - name: workload_size
          value: string
          description: |
            The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified.
        - name: workload_type
          value: string
          description: |
            The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types
      - name: served_models
        value: array
        description: |
          (Deprecated, use served_entities instead) The list of served models under the serving endpoint config.
        props:
        - name: scale_to_zero_enabled
          value: boolean
        - name: model_name
          value: string
        - name: model_version
          value: string
        - name: burst_scaling_enabled
          value: boolean
          description: |
            Whether burst scaling is enabled. When enabled (default), the endpoint can automatically scale up beyond provisioned capacity to handle traffic spikes. When disabled, the endpoint maintains fixed capacity at provisioned_model_units.
        - name: environment_vars
          value: object
          description: |
            An object containing a set of optional, user-specified environment variable key-value pairs used for serving this entity. Note: this is an experimental feature and subject to change. Example entity environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY": "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`
        - name: instance_profile_arn
          value: string
          description: |
            ARN of the instance profile that the served entity uses to access AWS resources.
        - name: max_provisioned_concurrency
          value: integer
          description: |
            The maximum provisioned concurrency that the endpoint can scale up to. Do not use if workload_size is specified.
        - name: max_provisioned_throughput
          value: integer
          description: |
            The maximum tokens per second that the endpoint can scale up to.
        - name: min_provisioned_concurrency
          value: integer
          description: |
            The minimum provisioned concurrency that the endpoint can scale down to. Do not use if workload_size is specified.
        - name: min_provisioned_throughput
          value: integer
          description: |
            The minimum tokens per second that the endpoint can scale down to.
        - name: name
          value: string
          description: |
            The name of a served entity. It must be unique across an endpoint. A served entity name can consist of alphanumeric characters, dashes, and underscores. If not specified for an external model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if not specified for other entities, it defaults to entity_name-entity_version.
        - name: provisioned_model_units
          value: integer
          description: |
            The number of model units provisioned.
        - name: workload_size
          value: string
          description: |
            The workload size of the served entity. The workload size corresponds to a range of provisioned concurrency that the compute autoscales between. A single unit of provisioned concurrency can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned concurrency). Additional custom workload sizes can also be used when available in the workspace. If scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size is 0. Do not use if min_provisioned_concurrency and max_provisioned_concurrency are specified.
        - name: workload_type
          value: string
          description: |
            The workload type of the served entity. The workload type selects which type of compute to use in the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU acceleration is available by selecting workload types like GPU_SMALL and others. See the available [GPU types]. [GPU types]: https://docs.databricks.com/en/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types
      - name: traffic_config
        value: object
        description: |
          The traffic configuration associated with the serving endpoint config.
        props:
        - name: routes
          value: array
          props:
          - name: traffic_percentage
            value: integer
          - name: served_entity_name
            value: string
          - name: served_model_name
            value: string
            description: |
              The name of the served model this route configures traffic for.
    - name: description
      value: string
      description: |
        :param email_notifications: :class:`EmailNotifications` (optional) Email notification settings.
    - name: email_notifications
      value: object
      props:
      - name: on_update_failure
        value: array
        items:
          type: string
      - name: on_update_success
        value: array
        description: |
          A list of email addresses to be notified when an endpoint successfully updates its configuration or state.
        items:
          type: string
    - name: rate_limits
      value: array
      description: |
        Rate limits to be applied to the serving endpoint. NOTE: this field is deprecated, please use AI Gateway to manage rate limits.
      props:
      - name: calls
        value: integer
      - name: renewal_period
        value: string
        description: |
          Renewal period field for a serving endpoint rate limit. Currently, only 'minute' is supported.
      - name: key
        value: string
        description: |
          Key field for a serving endpoint rate limit. Currently, only 'user' and 'endpoint' are supported, with 'endpoint' being the default if not specified.
    - name: route_optimized
      value: boolean
      description: |
        Enable route optimization for the serving endpoint.
    - name: tags
      value: array
      description: |
        Tags to be attached to the serving endpoint and automatically propagated to billing logs.
      props:
      - name: key
        value: string
      - name: value
        value: string
        description: |
          Optional value field for a serving endpoint tag.
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

Used to batch add and delete tags from a serving endpoint with a single API call.

```sql
UPDATE databricks_workspace.serving.serving_endpoints
SET 
add_tags = '{{ add_tags }}',
delete_tags = '{{ delete_tags }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
tags;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_config"
    values={[
        { label: 'update_config', value: 'update_config' }
    ]}
>
<TabItem value="update_config">

Updates any combination of the serving endpoint's served entities, the compute configuration of those

```sql
REPLACE databricks_workspace.serving.serving_endpoints
SET 
auto_capture_config = '{{ auto_capture_config }}',
served_entities = '{{ served_entities }}',
served_models = '{{ served_models }}',
traffic_config = '{{ traffic_config }}'
WHERE 
name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
RETURNING
id,
name,
budget_policy_id,
ai_gateway,
config,
creation_timestamp,
creator,
data_plane_info,
description,
email_notifications,
endpoint_url,
last_updated_timestamp,
pending_config,
permission_level,
route_optimized,
state,
tags,
task;
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

Delete a serving endpoint.

```sql
DELETE FROM databricks_workspace.serving.serving_endpoints
WHERE name = '{{ name }}' --required
AND workspace = '{{ workspace }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="query">

Query a serving endpoint

```sql
EXEC databricks_workspace.serving.serving_endpoints.query 
@name='{{ name }}' --required, 
@workspace='{{ workspace }}' --required 
@@json=
'{
"client_request_id": "{{ client_request_id }}", 
"dataframe_records": "{{ dataframe_records }}", 
"dataframe_split": "{{ dataframe_split }}", 
"extra_params": "{{ extra_params }}", 
"input": "{{ input }}", 
"inputs": "{{ inputs }}", 
"instances": "{{ instances }}", 
"max_tokens": {{ max_tokens }}, 
"messages": "{{ messages }}", 
"n": {{ n }}, 
"prompt": "{{ prompt }}", 
"stop": "{{ stop }}", 
"stream": {{ stream }}, 
"temperature": {{ temperature }}, 
"usage_context": "{{ usage_context }}"
}'
;
```
</TabItem>
</Tabs>
