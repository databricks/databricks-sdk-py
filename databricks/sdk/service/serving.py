# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, BinaryIO, Callable, Dict, Iterator, List, Optional

import requests

from ..data_plane import DataPlaneService
from ..errors import OperationFailed
from ._internal import Wait, _enum, _from_dict, _repeated_dict

_LOG = logging.getLogger('databricks.sdk')

from databricks.sdk.service import oauth2

# all definitions in this file are in alphabetical order


@dataclass
class Ai21LabsConfig:
    ai21labs_api_key: Optional[str] = None
    """The Databricks secret key reference for an AI21 Labs API key. If you prefer to paste your API
    key directly, see `ai21labs_api_key_plaintext`. You must provide an API key using one of the
    following fields: `ai21labs_api_key` or `ai21labs_api_key_plaintext`."""

    ai21labs_api_key_plaintext: Optional[str] = None
    """An AI21 Labs API key provided as a plaintext string. If you prefer to reference your key using
    Databricks Secrets, see `ai21labs_api_key`. You must provide an API key using one of the
    following fields: `ai21labs_api_key` or `ai21labs_api_key_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the Ai21LabsConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ai21labs_api_key is not None: body['ai21labs_api_key'] = self.ai21labs_api_key
        if self.ai21labs_api_key_plaintext is not None:
            body['ai21labs_api_key_plaintext'] = self.ai21labs_api_key_plaintext
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Ai21LabsConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ai21labs_api_key is not None: body['ai21labs_api_key'] = self.ai21labs_api_key
        if self.ai21labs_api_key_plaintext is not None:
            body['ai21labs_api_key_plaintext'] = self.ai21labs_api_key_plaintext
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Ai21LabsConfig:
        """Deserializes the Ai21LabsConfig from a dictionary."""
        return cls(ai21labs_api_key=d.get('ai21labs_api_key', None),
                   ai21labs_api_key_plaintext=d.get('ai21labs_api_key_plaintext', None))


@dataclass
class AiGatewayConfig:
    guardrails: Optional[AiGatewayGuardrails] = None
    """Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and
    responses."""

    inference_table_config: Optional[AiGatewayInferenceTableConfig] = None
    """Configuration for payload logging using inference tables. Use these tables to monitor and audit
    data being sent to and received from model APIs and to improve model quality."""

    rate_limits: Optional[List[AiGatewayRateLimit]] = None
    """Configuration for rate limits which can be set to limit endpoint traffic."""

    usage_tracking_config: Optional[AiGatewayUsageTrackingConfig] = None
    """Configuration to enable usage tracking using system tables. These tables allow you to monitor
    operational usage on endpoints and their associated costs."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.guardrails: body['guardrails'] = self.guardrails.as_dict()
        if self.inference_table_config: body['inference_table_config'] = self.inference_table_config.as_dict()
        if self.rate_limits: body['rate_limits'] = [v.as_dict() for v in self.rate_limits]
        if self.usage_tracking_config: body['usage_tracking_config'] = self.usage_tracking_config.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.guardrails: body['guardrails'] = self.guardrails
        if self.inference_table_config: body['inference_table_config'] = self.inference_table_config
        if self.rate_limits: body['rate_limits'] = self.rate_limits
        if self.usage_tracking_config: body['usage_tracking_config'] = self.usage_tracking_config
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayConfig:
        """Deserializes the AiGatewayConfig from a dictionary."""
        return cls(guardrails=_from_dict(d, 'guardrails', AiGatewayGuardrails),
                   inference_table_config=_from_dict(d, 'inference_table_config',
                                                     AiGatewayInferenceTableConfig),
                   rate_limits=_repeated_dict(d, 'rate_limits', AiGatewayRateLimit),
                   usage_tracking_config=_from_dict(d, 'usage_tracking_config', AiGatewayUsageTrackingConfig))


@dataclass
class AiGatewayGuardrailParameters:
    invalid_keywords: Optional[List[str]] = None
    """List of invalid keywords. AI guardrail uses keyword or string matching to decide if the keyword
    exists in the request or response content."""

    pii: Optional[AiGatewayGuardrailPiiBehavior] = None
    """Configuration for guardrail PII filter."""

    safety: Optional[bool] = None
    """Indicates whether the safety filter is enabled."""

    valid_topics: Optional[List[str]] = None
    """The list of allowed topics. Given a chat request, this guardrail flags the request if its topic
    is not in the allowed topics."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayGuardrailParameters into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.invalid_keywords: body['invalid_keywords'] = [v for v in self.invalid_keywords]
        if self.pii: body['pii'] = self.pii.as_dict()
        if self.safety is not None: body['safety'] = self.safety
        if self.valid_topics: body['valid_topics'] = [v for v in self.valid_topics]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayGuardrailParameters into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.invalid_keywords: body['invalid_keywords'] = self.invalid_keywords
        if self.pii: body['pii'] = self.pii
        if self.safety is not None: body['safety'] = self.safety
        if self.valid_topics: body['valid_topics'] = self.valid_topics
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayGuardrailParameters:
        """Deserializes the AiGatewayGuardrailParameters from a dictionary."""
        return cls(invalid_keywords=d.get('invalid_keywords', None),
                   pii=_from_dict(d, 'pii', AiGatewayGuardrailPiiBehavior),
                   safety=d.get('safety', None),
                   valid_topics=d.get('valid_topics', None))


@dataclass
class AiGatewayGuardrailPiiBehavior:
    behavior: AiGatewayGuardrailPiiBehaviorBehavior
    """Behavior for PII filter. Currently only 'BLOCK' is supported. If 'BLOCK' is set for the input
    guardrail and the request contains PII, the request is not sent to the model server and 400
    status code is returned; if 'BLOCK' is set for the output guardrail and the model response
    contains PII, the PII info in the response is redacted and 400 status code is returned."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayGuardrailPiiBehavior into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.behavior is not None: body['behavior'] = self.behavior.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayGuardrailPiiBehavior into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.behavior is not None: body['behavior'] = self.behavior
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayGuardrailPiiBehavior:
        """Deserializes the AiGatewayGuardrailPiiBehavior from a dictionary."""
        return cls(behavior=_enum(d, 'behavior', AiGatewayGuardrailPiiBehaviorBehavior))


class AiGatewayGuardrailPiiBehaviorBehavior(Enum):
    """Behavior for PII filter. Currently only 'BLOCK' is supported. If 'BLOCK' is set for the input
    guardrail and the request contains PII, the request is not sent to the model server and 400
    status code is returned; if 'BLOCK' is set for the output guardrail and the model response
    contains PII, the PII info in the response is redacted and 400 status code is returned."""

    BLOCK = 'BLOCK'
    NONE = 'NONE'


@dataclass
class AiGatewayGuardrails:
    input: Optional[AiGatewayGuardrailParameters] = None
    """Configuration for input guardrail filters."""

    output: Optional[AiGatewayGuardrailParameters] = None
    """Configuration for output guardrail filters."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayGuardrails into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.input: body['input'] = self.input.as_dict()
        if self.output: body['output'] = self.output.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayGuardrails into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.input: body['input'] = self.input
        if self.output: body['output'] = self.output
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayGuardrails:
        """Deserializes the AiGatewayGuardrails from a dictionary."""
        return cls(input=_from_dict(d, 'input', AiGatewayGuardrailParameters),
                   output=_from_dict(d, 'output', AiGatewayGuardrailParameters))


@dataclass
class AiGatewayInferenceTableConfig:
    catalog_name: Optional[str] = None
    """The name of the catalog in Unity Catalog. Required when enabling inference tables. NOTE: On
    update, you have to disable inference table first in order to change the catalog name."""

    enabled: Optional[bool] = None
    """Indicates whether the inference table is enabled."""

    schema_name: Optional[str] = None
    """The name of the schema in Unity Catalog. Required when enabling inference tables. NOTE: On
    update, you have to disable inference table first in order to change the schema name."""

    table_name_prefix: Optional[str] = None
    """The prefix of the table in Unity Catalog. NOTE: On update, you have to disable inference table
    first in order to change the prefix name."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayInferenceTableConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayInferenceTableConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayInferenceTableConfig:
        """Deserializes the AiGatewayInferenceTableConfig from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   enabled=d.get('enabled', None),
                   schema_name=d.get('schema_name', None),
                   table_name_prefix=d.get('table_name_prefix', None))


@dataclass
class AiGatewayRateLimit:
    calls: int
    """Used to specify how many calls are allowed for a key within the renewal_period."""

    renewal_period: AiGatewayRateLimitRenewalPeriod
    """Renewal period field for a rate limit. Currently, only 'minute' is supported."""

    key: Optional[AiGatewayRateLimitKey] = None
    """Key field for a rate limit. Currently, only 'user' and 'endpoint' are supported, with 'endpoint'
    being the default if not specified."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayRateLimit into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.calls is not None: body['calls'] = self.calls
        if self.key is not None: body['key'] = self.key.value
        if self.renewal_period is not None: body['renewal_period'] = self.renewal_period.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayRateLimit into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.calls is not None: body['calls'] = self.calls
        if self.key is not None: body['key'] = self.key
        if self.renewal_period is not None: body['renewal_period'] = self.renewal_period
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayRateLimit:
        """Deserializes the AiGatewayRateLimit from a dictionary."""
        return cls(calls=d.get('calls', None),
                   key=_enum(d, 'key', AiGatewayRateLimitKey),
                   renewal_period=_enum(d, 'renewal_period', AiGatewayRateLimitRenewalPeriod))


class AiGatewayRateLimitKey(Enum):
    """Key field for a rate limit. Currently, only 'user' and 'endpoint' are supported, with 'endpoint'
    being the default if not specified."""

    ENDPOINT = 'endpoint'
    USER = 'user'


class AiGatewayRateLimitRenewalPeriod(Enum):
    """Renewal period field for a rate limit. Currently, only 'minute' is supported."""

    MINUTE = 'minute'


@dataclass
class AiGatewayUsageTrackingConfig:
    enabled: Optional[bool] = None
    """Whether to enable usage tracking."""

    def as_dict(self) -> dict:
        """Serializes the AiGatewayUsageTrackingConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiGatewayUsageTrackingConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enabled is not None: body['enabled'] = self.enabled
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AiGatewayUsageTrackingConfig:
        """Deserializes the AiGatewayUsageTrackingConfig from a dictionary."""
        return cls(enabled=d.get('enabled', None))


@dataclass
class AmazonBedrockConfig:
    aws_region: str
    """The AWS region to use. Bedrock has to be enabled there."""

    bedrock_provider: AmazonBedrockConfigBedrockProvider
    """The underlying provider in Amazon Bedrock. Supported values (case insensitive) include:
    Anthropic, Cohere, AI21Labs, Amazon."""

    aws_access_key_id: Optional[str] = None
    """The Databricks secret key reference for an AWS access key ID with permissions to interact with
    Bedrock services. If you prefer to paste your API key directly, see `aws_access_key_id`. You
    must provide an API key using one of the following fields: `aws_access_key_id` or
    `aws_access_key_id_plaintext`."""

    aws_access_key_id_plaintext: Optional[str] = None
    """An AWS access key ID with permissions to interact with Bedrock services provided as a plaintext
    string. If you prefer to reference your key using Databricks Secrets, see `aws_access_key_id`.
    You must provide an API key using one of the following fields: `aws_access_key_id` or
    `aws_access_key_id_plaintext`."""

    aws_secret_access_key: Optional[str] = None
    """The Databricks secret key reference for an AWS secret access key paired with the access key ID,
    with permissions to interact with Bedrock services. If you prefer to paste your API key
    directly, see `aws_secret_access_key_plaintext`. You must provide an API key using one of the
    following fields: `aws_secret_access_key` or `aws_secret_access_key_plaintext`."""

    aws_secret_access_key_plaintext: Optional[str] = None
    """An AWS secret access key paired with the access key ID, with permissions to interact with
    Bedrock services provided as a plaintext string. If you prefer to reference your key using
    Databricks Secrets, see `aws_secret_access_key`. You must provide an API key using one of the
    following fields: `aws_secret_access_key` or `aws_secret_access_key_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the AmazonBedrockConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.aws_access_key_id is not None: body['aws_access_key_id'] = self.aws_access_key_id
        if self.aws_access_key_id_plaintext is not None:
            body['aws_access_key_id_plaintext'] = self.aws_access_key_id_plaintext
        if self.aws_region is not None: body['aws_region'] = self.aws_region
        if self.aws_secret_access_key is not None: body['aws_secret_access_key'] = self.aws_secret_access_key
        if self.aws_secret_access_key_plaintext is not None:
            body['aws_secret_access_key_plaintext'] = self.aws_secret_access_key_plaintext
        if self.bedrock_provider is not None: body['bedrock_provider'] = self.bedrock_provider.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AmazonBedrockConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.aws_access_key_id is not None: body['aws_access_key_id'] = self.aws_access_key_id
        if self.aws_access_key_id_plaintext is not None:
            body['aws_access_key_id_plaintext'] = self.aws_access_key_id_plaintext
        if self.aws_region is not None: body['aws_region'] = self.aws_region
        if self.aws_secret_access_key is not None: body['aws_secret_access_key'] = self.aws_secret_access_key
        if self.aws_secret_access_key_plaintext is not None:
            body['aws_secret_access_key_plaintext'] = self.aws_secret_access_key_plaintext
        if self.bedrock_provider is not None: body['bedrock_provider'] = self.bedrock_provider
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AmazonBedrockConfig:
        """Deserializes the AmazonBedrockConfig from a dictionary."""
        return cls(aws_access_key_id=d.get('aws_access_key_id', None),
                   aws_access_key_id_plaintext=d.get('aws_access_key_id_plaintext', None),
                   aws_region=d.get('aws_region', None),
                   aws_secret_access_key=d.get('aws_secret_access_key', None),
                   aws_secret_access_key_plaintext=d.get('aws_secret_access_key_plaintext', None),
                   bedrock_provider=_enum(d, 'bedrock_provider', AmazonBedrockConfigBedrockProvider))


class AmazonBedrockConfigBedrockProvider(Enum):
    """The underlying provider in Amazon Bedrock. Supported values (case insensitive) include:
    Anthropic, Cohere, AI21Labs, Amazon."""

    AI21LABS = 'ai21labs'
    AMAZON = 'amazon'
    ANTHROPIC = 'anthropic'
    COHERE = 'cohere'


@dataclass
class AnthropicConfig:
    anthropic_api_key: Optional[str] = None
    """The Databricks secret key reference for an Anthropic API key. If you prefer to paste your API
    key directly, see `anthropic_api_key_plaintext`. You must provide an API key using one of the
    following fields: `anthropic_api_key` or `anthropic_api_key_plaintext`."""

    anthropic_api_key_plaintext: Optional[str] = None
    """The Anthropic API key provided as a plaintext string. If you prefer to reference your key using
    Databricks Secrets, see `anthropic_api_key`. You must provide an API key using one of the
    following fields: `anthropic_api_key` or `anthropic_api_key_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the AnthropicConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.anthropic_api_key is not None: body['anthropic_api_key'] = self.anthropic_api_key
        if self.anthropic_api_key_plaintext is not None:
            body['anthropic_api_key_plaintext'] = self.anthropic_api_key_plaintext
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AnthropicConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.anthropic_api_key is not None: body['anthropic_api_key'] = self.anthropic_api_key
        if self.anthropic_api_key_plaintext is not None:
            body['anthropic_api_key_plaintext'] = self.anthropic_api_key_plaintext
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AnthropicConfig:
        """Deserializes the AnthropicConfig from a dictionary."""
        return cls(anthropic_api_key=d.get('anthropic_api_key', None),
                   anthropic_api_key_plaintext=d.get('anthropic_api_key_plaintext', None))


@dataclass
class AutoCaptureConfigInput:
    catalog_name: Optional[str] = None
    """The name of the catalog in Unity Catalog. NOTE: On update, you cannot change the catalog name if
    the inference table is already enabled."""

    enabled: Optional[bool] = None
    """Indicates whether the inference table is enabled."""

    schema_name: Optional[str] = None
    """The name of the schema in Unity Catalog. NOTE: On update, you cannot change the schema name if
    the inference table is already enabled."""

    table_name_prefix: Optional[str] = None
    """The prefix of the table in Unity Catalog. NOTE: On update, you cannot change the prefix name if
    the inference table is already enabled."""

    def as_dict(self) -> dict:
        """Serializes the AutoCaptureConfigInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoCaptureConfigInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AutoCaptureConfigInput:
        """Deserializes the AutoCaptureConfigInput from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   enabled=d.get('enabled', None),
                   schema_name=d.get('schema_name', None),
                   table_name_prefix=d.get('table_name_prefix', None))


@dataclass
class AutoCaptureConfigOutput:
    catalog_name: Optional[str] = None
    """The name of the catalog in Unity Catalog."""

    enabled: Optional[bool] = None
    """Indicates whether the inference table is enabled."""

    schema_name: Optional[str] = None
    """The name of the schema in Unity Catalog."""

    state: Optional[AutoCaptureState] = None

    table_name_prefix: Optional[str] = None
    """The prefix of the table in Unity Catalog."""

    def as_dict(self) -> dict:
        """Serializes the AutoCaptureConfigOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.state: body['state'] = self.state.as_dict()
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoCaptureConfigOutput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.catalog_name is not None: body['catalog_name'] = self.catalog_name
        if self.enabled is not None: body['enabled'] = self.enabled
        if self.schema_name is not None: body['schema_name'] = self.schema_name
        if self.state: body['state'] = self.state
        if self.table_name_prefix is not None: body['table_name_prefix'] = self.table_name_prefix
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AutoCaptureConfigOutput:
        """Deserializes the AutoCaptureConfigOutput from a dictionary."""
        return cls(catalog_name=d.get('catalog_name', None),
                   enabled=d.get('enabled', None),
                   schema_name=d.get('schema_name', None),
                   state=_from_dict(d, 'state', AutoCaptureState),
                   table_name_prefix=d.get('table_name_prefix', None))


@dataclass
class AutoCaptureState:
    payload_table: Optional[PayloadTable] = None

    def as_dict(self) -> dict:
        """Serializes the AutoCaptureState into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.payload_table: body['payload_table'] = self.payload_table.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AutoCaptureState into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.payload_table: body['payload_table'] = self.payload_table
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> AutoCaptureState:
        """Deserializes the AutoCaptureState from a dictionary."""
        return cls(payload_table=_from_dict(d, 'payload_table', PayloadTable))


@dataclass
class BuildLogsResponse:
    logs: str
    """The logs associated with building the served entity's environment."""

    def as_dict(self) -> dict:
        """Serializes the BuildLogsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the BuildLogsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> BuildLogsResponse:
        """Deserializes the BuildLogsResponse from a dictionary."""
        return cls(logs=d.get('logs', None))


@dataclass
class ChatMessage:
    content: Optional[str] = None
    """The content of the message."""

    role: Optional[ChatMessageRole] = None
    """The role of the message. One of [system, user, assistant]."""

    def as_dict(self) -> dict:
        """Serializes the ChatMessage into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.role is not None: body['role'] = self.role.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ChatMessage into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.content is not None: body['content'] = self.content
        if self.role is not None: body['role'] = self.role
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ChatMessage:
        """Deserializes the ChatMessage from a dictionary."""
        return cls(content=d.get('content', None), role=_enum(d, 'role', ChatMessageRole))


class ChatMessageRole(Enum):
    """The role of the message. One of [system, user, assistant]."""

    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


@dataclass
class CohereConfig:
    cohere_api_base: Optional[str] = None
    """This is an optional field to provide a customized base URL for the Cohere API. If left
    unspecified, the standard Cohere base URL is used."""

    cohere_api_key: Optional[str] = None
    """The Databricks secret key reference for a Cohere API key. If you prefer to paste your API key
    directly, see `cohere_api_key_plaintext`. You must provide an API key using one of the following
    fields: `cohere_api_key` or `cohere_api_key_plaintext`."""

    cohere_api_key_plaintext: Optional[str] = None
    """The Cohere API key provided as a plaintext string. If you prefer to reference your key using
    Databricks Secrets, see `cohere_api_key`. You must provide an API key using one of the following
    fields: `cohere_api_key` or `cohere_api_key_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the CohereConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.cohere_api_base is not None: body['cohere_api_base'] = self.cohere_api_base
        if self.cohere_api_key is not None: body['cohere_api_key'] = self.cohere_api_key
        if self.cohere_api_key_plaintext is not None:
            body['cohere_api_key_plaintext'] = self.cohere_api_key_plaintext
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CohereConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.cohere_api_base is not None: body['cohere_api_base'] = self.cohere_api_base
        if self.cohere_api_key is not None: body['cohere_api_key'] = self.cohere_api_key
        if self.cohere_api_key_plaintext is not None:
            body['cohere_api_key_plaintext'] = self.cohere_api_key_plaintext
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CohereConfig:
        """Deserializes the CohereConfig from a dictionary."""
        return cls(cohere_api_base=d.get('cohere_api_base', None),
                   cohere_api_key=d.get('cohere_api_key', None),
                   cohere_api_key_plaintext=d.get('cohere_api_key_plaintext', None))


@dataclass
class CreateServingEndpoint:
    name: str
    """The name of the serving endpoint. This field is required and must be unique across a Databricks
    workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores."""

    config: EndpointCoreConfigInput
    """The core config of the serving endpoint."""

    ai_gateway: Optional[AiGatewayConfig] = None
    """The AI Gateway configuration for the serving endpoint. NOTE: only external model endpoints are
    supported as of now."""

    rate_limits: Optional[List[RateLimit]] = None
    """Rate limits to be applied to the serving endpoint. NOTE: this field is deprecated, please use AI
    Gateway to manage rate limits."""

    route_optimized: Optional[bool] = None
    """Enable route optimization for the serving endpoint."""

    tags: Optional[List[EndpointTag]] = None
    """Tags to be attached to the serving endpoint and automatically propagated to billing logs."""

    def as_dict(self) -> dict:
        """Serializes the CreateServingEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway.as_dict()
        if self.config: body['config'] = self.config.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.rate_limits: body['rate_limits'] = [v.as_dict() for v in self.rate_limits]
        if self.route_optimized is not None: body['route_optimized'] = self.route_optimized
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the CreateServingEndpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway
        if self.config: body['config'] = self.config
        if self.name is not None: body['name'] = self.name
        if self.rate_limits: body['rate_limits'] = self.rate_limits
        if self.route_optimized is not None: body['route_optimized'] = self.route_optimized
        if self.tags: body['tags'] = self.tags
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> CreateServingEndpoint:
        """Deserializes the CreateServingEndpoint from a dictionary."""
        return cls(ai_gateway=_from_dict(d, 'ai_gateway', AiGatewayConfig),
                   config=_from_dict(d, 'config', EndpointCoreConfigInput),
                   name=d.get('name', None),
                   rate_limits=_repeated_dict(d, 'rate_limits', RateLimit),
                   route_optimized=d.get('route_optimized', None),
                   tags=_repeated_dict(d, 'tags', EndpointTag))


@dataclass
class DatabricksModelServingConfig:
    databricks_workspace_url: str
    """The URL of the Databricks workspace containing the model serving endpoint pointed to by this
    external model."""

    databricks_api_token: Optional[str] = None
    """The Databricks secret key reference for a Databricks API token that corresponds to a user or
    service principal with Can Query access to the model serving endpoint pointed to by this
    external model. If you prefer to paste your API key directly, see
    `databricks_api_token_plaintext`. You must provide an API key using one of the following fields:
    `databricks_api_token` or `databricks_api_token_plaintext`."""

    databricks_api_token_plaintext: Optional[str] = None
    """The Databricks API token that corresponds to a user or service principal with Can Query access
    to the model serving endpoint pointed to by this external model provided as a plaintext string.
    If you prefer to reference your key using Databricks Secrets, see `databricks_api_token`. You
    must provide an API key using one of the following fields: `databricks_api_token` or
    `databricks_api_token_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the DatabricksModelServingConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.databricks_api_token is not None: body['databricks_api_token'] = self.databricks_api_token
        if self.databricks_api_token_plaintext is not None:
            body['databricks_api_token_plaintext'] = self.databricks_api_token_plaintext
        if self.databricks_workspace_url is not None:
            body['databricks_workspace_url'] = self.databricks_workspace_url
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DatabricksModelServingConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.databricks_api_token is not None: body['databricks_api_token'] = self.databricks_api_token
        if self.databricks_api_token_plaintext is not None:
            body['databricks_api_token_plaintext'] = self.databricks_api_token_plaintext
        if self.databricks_workspace_url is not None:
            body['databricks_workspace_url'] = self.databricks_workspace_url
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DatabricksModelServingConfig:
        """Deserializes the DatabricksModelServingConfig from a dictionary."""
        return cls(databricks_api_token=d.get('databricks_api_token', None),
                   databricks_api_token_plaintext=d.get('databricks_api_token_plaintext', None),
                   databricks_workspace_url=d.get('databricks_workspace_url', None))


@dataclass
class DataframeSplitInput:
    columns: Optional[List[Any]] = None

    data: Optional[List[Any]] = None

    index: Optional[List[int]] = None

    def as_dict(self) -> dict:
        """Serializes the DataframeSplitInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.columns: body['columns'] = [v for v in self.columns]
        if self.data: body['data'] = [v for v in self.data]
        if self.index: body['index'] = [v for v in self.index]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DataframeSplitInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.columns: body['columns'] = self.columns
        if self.data: body['data'] = self.data
        if self.index: body['index'] = self.index
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DataframeSplitInput:
        """Deserializes the DataframeSplitInput from a dictionary."""
        return cls(columns=d.get('columns', None), data=d.get('data', None), index=d.get('index', None))


@dataclass
class DeleteResponse:

    def as_dict(self) -> dict:
        """Serializes the DeleteResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the DeleteResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> DeleteResponse:
        """Deserializes the DeleteResponse from a dictionary."""
        return cls()


@dataclass
class EmbeddingsV1ResponseEmbeddingElement:
    embedding: Optional[List[float]] = None

    index: Optional[int] = None
    """The index of the embedding in the response."""

    object: Optional[EmbeddingsV1ResponseEmbeddingElementObject] = None
    """This will always be 'embedding'."""

    def as_dict(self) -> dict:
        """Serializes the EmbeddingsV1ResponseEmbeddingElement into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.embedding: body['embedding'] = [v for v in self.embedding]
        if self.index is not None: body['index'] = self.index
        if self.object is not None: body['object'] = self.object.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EmbeddingsV1ResponseEmbeddingElement into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.embedding: body['embedding'] = self.embedding
        if self.index is not None: body['index'] = self.index
        if self.object is not None: body['object'] = self.object
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EmbeddingsV1ResponseEmbeddingElement:
        """Deserializes the EmbeddingsV1ResponseEmbeddingElement from a dictionary."""
        return cls(embedding=d.get('embedding', None),
                   index=d.get('index', None),
                   object=_enum(d, 'object', EmbeddingsV1ResponseEmbeddingElementObject))


class EmbeddingsV1ResponseEmbeddingElementObject(Enum):
    """This will always be 'embedding'."""

    EMBEDDING = 'embedding'


@dataclass
class EndpointCoreConfigInput:
    auto_capture_config: Optional[AutoCaptureConfigInput] = None
    """Configuration for Inference Tables which automatically logs requests and responses to Unity
    Catalog."""

    name: Optional[str] = None
    """The name of the serving endpoint to update. This field is required."""

    served_entities: Optional[List[ServedEntityInput]] = None
    """A list of served entities for the endpoint to serve. A serving endpoint can have up to 15 served
    entities."""

    served_models: Optional[List[ServedModelInput]] = None
    """(Deprecated, use served_entities instead) A list of served models for the endpoint to serve. A
    serving endpoint can have up to 15 served models."""

    traffic_config: Optional[TrafficConfig] = None
    """The traffic config defining how invocations to the serving endpoint should be routed."""

    def as_dict(self) -> dict:
        """Serializes the EndpointCoreConfigInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.served_entities: body['served_entities'] = [v.as_dict() for v in self.served_entities]
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointCoreConfigInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config
        if self.name is not None: body['name'] = self.name
        if self.served_entities: body['served_entities'] = self.served_entities
        if self.served_models: body['served_models'] = self.served_models
        if self.traffic_config: body['traffic_config'] = self.traffic_config
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointCoreConfigInput:
        """Deserializes the EndpointCoreConfigInput from a dictionary."""
        return cls(auto_capture_config=_from_dict(d, 'auto_capture_config', AutoCaptureConfigInput),
                   name=d.get('name', None),
                   served_entities=_repeated_dict(d, 'served_entities', ServedEntityInput),
                   served_models=_repeated_dict(d, 'served_models', ServedModelInput),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointCoreConfigOutput:
    auto_capture_config: Optional[AutoCaptureConfigOutput] = None
    """Configuration for Inference Tables which automatically logs requests and responses to Unity
    Catalog."""

    config_version: Optional[int] = None
    """The config version that the serving endpoint is currently serving."""

    served_entities: Optional[List[ServedEntityOutput]] = None
    """The list of served entities under the serving endpoint config."""

    served_models: Optional[List[ServedModelOutput]] = None
    """(Deprecated, use served_entities instead) The list of served models under the serving endpoint
    config."""

    traffic_config: Optional[TrafficConfig] = None
    """The traffic configuration associated with the serving endpoint config."""

    def as_dict(self) -> dict:
        """Serializes the EndpointCoreConfigOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config.as_dict()
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_entities: body['served_entities'] = [v.as_dict() for v in self.served_entities]
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointCoreConfigOutput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_entities: body['served_entities'] = self.served_entities
        if self.served_models: body['served_models'] = self.served_models
        if self.traffic_config: body['traffic_config'] = self.traffic_config
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointCoreConfigOutput:
        """Deserializes the EndpointCoreConfigOutput from a dictionary."""
        return cls(auto_capture_config=_from_dict(d, 'auto_capture_config', AutoCaptureConfigOutput),
                   config_version=d.get('config_version', None),
                   served_entities=_repeated_dict(d, 'served_entities', ServedEntityOutput),
                   served_models=_repeated_dict(d, 'served_models', ServedModelOutput),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointCoreConfigSummary:
    served_entities: Optional[List[ServedEntitySpec]] = None
    """The list of served entities under the serving endpoint config."""

    served_models: Optional[List[ServedModelSpec]] = None
    """(Deprecated, use served_entities instead) The list of served models under the serving endpoint
    config."""

    def as_dict(self) -> dict:
        """Serializes the EndpointCoreConfigSummary into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.served_entities: body['served_entities'] = [v.as_dict() for v in self.served_entities]
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointCoreConfigSummary into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.served_entities: body['served_entities'] = self.served_entities
        if self.served_models: body['served_models'] = self.served_models
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointCoreConfigSummary:
        """Deserializes the EndpointCoreConfigSummary from a dictionary."""
        return cls(served_entities=_repeated_dict(d, 'served_entities', ServedEntitySpec),
                   served_models=_repeated_dict(d, 'served_models', ServedModelSpec))


@dataclass
class EndpointPendingConfig:
    auto_capture_config: Optional[AutoCaptureConfigOutput] = None
    """Configuration for Inference Tables which automatically logs requests and responses to Unity
    Catalog."""

    config_version: Optional[int] = None
    """The config version that the serving endpoint is currently serving."""

    served_entities: Optional[List[ServedEntityOutput]] = None
    """The list of served entities belonging to the last issued update to the serving endpoint."""

    served_models: Optional[List[ServedModelOutput]] = None
    """(Deprecated, use served_entities instead) The list of served models belonging to the last issued
    update to the serving endpoint."""

    start_time: Optional[int] = None
    """The timestamp when the update to the pending config started."""

    traffic_config: Optional[TrafficConfig] = None
    """The traffic config defining how invocations to the serving endpoint should be routed."""

    def as_dict(self) -> dict:
        """Serializes the EndpointPendingConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config.as_dict()
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_entities: body['served_entities'] = [v.as_dict() for v in self.served_entities]
        if self.served_models: body['served_models'] = [v.as_dict() for v in self.served_models]
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.traffic_config: body['traffic_config'] = self.traffic_config.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointPendingConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.auto_capture_config: body['auto_capture_config'] = self.auto_capture_config
        if self.config_version is not None: body['config_version'] = self.config_version
        if self.served_entities: body['served_entities'] = self.served_entities
        if self.served_models: body['served_models'] = self.served_models
        if self.start_time is not None: body['start_time'] = self.start_time
        if self.traffic_config: body['traffic_config'] = self.traffic_config
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointPendingConfig:
        """Deserializes the EndpointPendingConfig from a dictionary."""
        return cls(auto_capture_config=_from_dict(d, 'auto_capture_config', AutoCaptureConfigOutput),
                   config_version=d.get('config_version', None),
                   served_entities=_repeated_dict(d, 'served_entities', ServedEntityOutput),
                   served_models=_repeated_dict(d, 'served_models', ServedModelOutput),
                   start_time=d.get('start_time', None),
                   traffic_config=_from_dict(d, 'traffic_config', TrafficConfig))


@dataclass
class EndpointState:
    config_update: Optional[EndpointStateConfigUpdate] = None
    """The state of an endpoint's config update. This informs the user if the pending_config is in
    progress, if the update failed, or if there is no update in progress. Note that if the
    endpoint's config_update state value is IN_PROGRESS, another update can not be made until the
    update completes or fails."""

    ready: Optional[EndpointStateReady] = None
    """The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is
    READY if all of the served entities in its active configuration are ready. If any of the
    actively served entities are in a non-ready state, the endpoint state will be NOT_READY."""

    def as_dict(self) -> dict:
        """Serializes the EndpointState into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.config_update is not None: body['config_update'] = self.config_update.value
        if self.ready is not None: body['ready'] = self.ready.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointState into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.config_update is not None: body['config_update'] = self.config_update
        if self.ready is not None: body['ready'] = self.ready
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointState:
        """Deserializes the EndpointState from a dictionary."""
        return cls(config_update=_enum(d, 'config_update', EndpointStateConfigUpdate),
                   ready=_enum(d, 'ready', EndpointStateReady))


class EndpointStateConfigUpdate(Enum):
    """The state of an endpoint's config update. This informs the user if the pending_config is in
    progress, if the update failed, or if there is no update in progress. Note that if the
    endpoint's config_update state value is IN_PROGRESS, another update can not be made until the
    update completes or fails."""

    IN_PROGRESS = 'IN_PROGRESS'
    NOT_UPDATING = 'NOT_UPDATING'
    UPDATE_CANCELED = 'UPDATE_CANCELED'
    UPDATE_FAILED = 'UPDATE_FAILED'


class EndpointStateReady(Enum):
    """The state of an endpoint, indicating whether or not the endpoint is queryable. An endpoint is
    READY if all of the served entities in its active configuration are ready. If any of the
    actively served entities are in a non-ready state, the endpoint state will be NOT_READY."""

    NOT_READY = 'NOT_READY'
    READY = 'READY'


@dataclass
class EndpointTag:
    key: str
    """Key field for a serving endpoint tag."""

    value: Optional[str] = None
    """Optional value field for a serving endpoint tag."""

    def as_dict(self) -> dict:
        """Serializes the EndpointTag into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the EndpointTag into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.key is not None: body['key'] = self.key
        if self.value is not None: body['value'] = self.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> EndpointTag:
        """Deserializes the EndpointTag from a dictionary."""
        return cls(key=d.get('key', None), value=d.get('value', None))


@dataclass
class ExportMetricsResponse:
    contents: Optional[BinaryIO] = None

    def as_dict(self) -> dict:
        """Serializes the ExportMetricsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.contents: body['contents'] = self.contents
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExportMetricsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.contents: body['contents'] = self.contents
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExportMetricsResponse:
        """Deserializes the ExportMetricsResponse from a dictionary."""
        return cls(contents=d.get('contents', None))


@dataclass
class ExternalModel:
    provider: ExternalModelProvider
    """The name of the provider for the external model. Currently, the supported providers are
    'ai21labs', 'anthropic', 'amazon-bedrock', 'cohere', 'databricks-model-serving',
    'google-cloud-vertex-ai', 'openai', and 'palm'.","""

    name: str
    """The name of the external model."""

    task: str
    """The task type of the external model."""

    ai21labs_config: Optional[Ai21LabsConfig] = None
    """AI21Labs Config. Only required if the provider is 'ai21labs'."""

    amazon_bedrock_config: Optional[AmazonBedrockConfig] = None
    """Amazon Bedrock Config. Only required if the provider is 'amazon-bedrock'."""

    anthropic_config: Optional[AnthropicConfig] = None
    """Anthropic Config. Only required if the provider is 'anthropic'."""

    cohere_config: Optional[CohereConfig] = None
    """Cohere Config. Only required if the provider is 'cohere'."""

    databricks_model_serving_config: Optional[DatabricksModelServingConfig] = None
    """Databricks Model Serving Config. Only required if the provider is 'databricks-model-serving'."""

    google_cloud_vertex_ai_config: Optional[GoogleCloudVertexAiConfig] = None
    """Google Cloud Vertex AI Config. Only required if the provider is 'google-cloud-vertex-ai'."""

    openai_config: Optional[OpenAiConfig] = None
    """OpenAI Config. Only required if the provider is 'openai'."""

    palm_config: Optional[PaLmConfig] = None
    """PaLM Config. Only required if the provider is 'palm'."""

    def as_dict(self) -> dict:
        """Serializes the ExternalModel into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ai21labs_config: body['ai21labs_config'] = self.ai21labs_config.as_dict()
        if self.amazon_bedrock_config: body['amazon_bedrock_config'] = self.amazon_bedrock_config.as_dict()
        if self.anthropic_config: body['anthropic_config'] = self.anthropic_config.as_dict()
        if self.cohere_config: body['cohere_config'] = self.cohere_config.as_dict()
        if self.databricks_model_serving_config:
            body['databricks_model_serving_config'] = self.databricks_model_serving_config.as_dict()
        if self.google_cloud_vertex_ai_config:
            body['google_cloud_vertex_ai_config'] = self.google_cloud_vertex_ai_config.as_dict()
        if self.name is not None: body['name'] = self.name
        if self.openai_config: body['openai_config'] = self.openai_config.as_dict()
        if self.palm_config: body['palm_config'] = self.palm_config.as_dict()
        if self.provider is not None: body['provider'] = self.provider.value
        if self.task is not None: body['task'] = self.task
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalModel into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ai21labs_config: body['ai21labs_config'] = self.ai21labs_config
        if self.amazon_bedrock_config: body['amazon_bedrock_config'] = self.amazon_bedrock_config
        if self.anthropic_config: body['anthropic_config'] = self.anthropic_config
        if self.cohere_config: body['cohere_config'] = self.cohere_config
        if self.databricks_model_serving_config:
            body['databricks_model_serving_config'] = self.databricks_model_serving_config
        if self.google_cloud_vertex_ai_config:
            body['google_cloud_vertex_ai_config'] = self.google_cloud_vertex_ai_config
        if self.name is not None: body['name'] = self.name
        if self.openai_config: body['openai_config'] = self.openai_config
        if self.palm_config: body['palm_config'] = self.palm_config
        if self.provider is not None: body['provider'] = self.provider
        if self.task is not None: body['task'] = self.task
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExternalModel:
        """Deserializes the ExternalModel from a dictionary."""
        return cls(ai21labs_config=_from_dict(d, 'ai21labs_config', Ai21LabsConfig),
                   amazon_bedrock_config=_from_dict(d, 'amazon_bedrock_config', AmazonBedrockConfig),
                   anthropic_config=_from_dict(d, 'anthropic_config', AnthropicConfig),
                   cohere_config=_from_dict(d, 'cohere_config', CohereConfig),
                   databricks_model_serving_config=_from_dict(d, 'databricks_model_serving_config',
                                                              DatabricksModelServingConfig),
                   google_cloud_vertex_ai_config=_from_dict(d, 'google_cloud_vertex_ai_config',
                                                            GoogleCloudVertexAiConfig),
                   name=d.get('name', None),
                   openai_config=_from_dict(d, 'openai_config', OpenAiConfig),
                   palm_config=_from_dict(d, 'palm_config', PaLmConfig),
                   provider=_enum(d, 'provider', ExternalModelProvider),
                   task=d.get('task', None))


class ExternalModelProvider(Enum):
    """The name of the provider for the external model. Currently, the supported providers are
    'ai21labs', 'anthropic', 'amazon-bedrock', 'cohere', 'databricks-model-serving',
    'google-cloud-vertex-ai', 'openai', and 'palm'.","""

    AI21LABS = 'ai21labs'
    AMAZON_BEDROCK = 'amazon-bedrock'
    ANTHROPIC = 'anthropic'
    COHERE = 'cohere'
    DATABRICKS_MODEL_SERVING = 'databricks-model-serving'
    GOOGLE_CLOUD_VERTEX_AI = 'google-cloud-vertex-ai'
    OPENAI = 'openai'
    PALM = 'palm'


@dataclass
class ExternalModelUsageElement:
    completion_tokens: Optional[int] = None
    """The number of tokens in the chat/completions response."""

    prompt_tokens: Optional[int] = None
    """The number of tokens in the prompt."""

    total_tokens: Optional[int] = None
    """The total number of tokens in the prompt and response."""

    def as_dict(self) -> dict:
        """Serializes the ExternalModelUsageElement into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.completion_tokens is not None: body['completion_tokens'] = self.completion_tokens
        if self.prompt_tokens is not None: body['prompt_tokens'] = self.prompt_tokens
        if self.total_tokens is not None: body['total_tokens'] = self.total_tokens
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ExternalModelUsageElement into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.completion_tokens is not None: body['completion_tokens'] = self.completion_tokens
        if self.prompt_tokens is not None: body['prompt_tokens'] = self.prompt_tokens
        if self.total_tokens is not None: body['total_tokens'] = self.total_tokens
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ExternalModelUsageElement:
        """Deserializes the ExternalModelUsageElement from a dictionary."""
        return cls(completion_tokens=d.get('completion_tokens', None),
                   prompt_tokens=d.get('prompt_tokens', None),
                   total_tokens=d.get('total_tokens', None))


@dataclass
class FoundationModel:
    description: Optional[str] = None
    """The description of the foundation model."""

    display_name: Optional[str] = None
    """The display name of the foundation model."""

    docs: Optional[str] = None
    """The URL to the documentation of the foundation model."""

    name: Optional[str] = None
    """The name of the foundation model."""

    def as_dict(self) -> dict:
        """Serializes the FoundationModel into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.docs is not None: body['docs'] = self.docs
        if self.name is not None: body['name'] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the FoundationModel into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.docs is not None: body['docs'] = self.docs
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> FoundationModel:
        """Deserializes the FoundationModel from a dictionary."""
        return cls(description=d.get('description', None),
                   display_name=d.get('display_name', None),
                   docs=d.get('docs', None),
                   name=d.get('name', None))


@dataclass
class GetOpenApiResponse:
    """The response is an OpenAPI spec in JSON format that typically includes fields like openapi,
    info, servers and paths, etc."""

    def as_dict(self) -> dict:
        """Serializes the GetOpenApiResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetOpenApiResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetOpenApiResponse:
        """Deserializes the GetOpenApiResponse from a dictionary."""
        return cls()


@dataclass
class GetServingEndpointPermissionLevelsResponse:
    permission_levels: Optional[List[ServingEndpointPermissionsDescription]] = None
    """Specific permission levels"""

    def as_dict(self) -> dict:
        """Serializes the GetServingEndpointPermissionLevelsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.permission_levels: body['permission_levels'] = [v.as_dict() for v in self.permission_levels]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GetServingEndpointPermissionLevelsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.permission_levels: body['permission_levels'] = self.permission_levels
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GetServingEndpointPermissionLevelsResponse:
        """Deserializes the GetServingEndpointPermissionLevelsResponse from a dictionary."""
        return cls(
            permission_levels=_repeated_dict(d, 'permission_levels', ServingEndpointPermissionsDescription))


@dataclass
class GoogleCloudVertexAiConfig:
    private_key: Optional[str] = None
    """The Databricks secret key reference for a private key for the service account which has access
    to the Google Cloud Vertex AI Service. See [Best practices for managing service account keys].
    If you prefer to paste your API key directly, see `private_key_plaintext`. You must provide an
    API key using one of the following fields: `private_key` or `private_key_plaintext`
    
    [Best practices for managing service account keys]: https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys"""

    private_key_plaintext: Optional[str] = None
    """The private key for the service account which has access to the Google Cloud Vertex AI Service
    provided as a plaintext secret. See [Best practices for managing service account keys]. If you
    prefer to reference your key using Databricks Secrets, see `private_key`. You must provide an
    API key using one of the following fields: `private_key` or `private_key_plaintext`.
    
    [Best practices for managing service account keys]: https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys"""

    project_id: Optional[str] = None
    """This is the Google Cloud project id that the service account is associated with."""

    region: Optional[str] = None
    """This is the region for the Google Cloud Vertex AI Service. See [supported regions] for more
    details. Some models are only available in specific regions.
    
    [supported regions]: https://cloud.google.com/vertex-ai/docs/general/locations"""

    def as_dict(self) -> dict:
        """Serializes the GoogleCloudVertexAiConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.private_key is not None: body['private_key'] = self.private_key
        if self.private_key_plaintext is not None: body['private_key_plaintext'] = self.private_key_plaintext
        if self.project_id is not None: body['project_id'] = self.project_id
        if self.region is not None: body['region'] = self.region
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the GoogleCloudVertexAiConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.private_key is not None: body['private_key'] = self.private_key
        if self.private_key_plaintext is not None: body['private_key_plaintext'] = self.private_key_plaintext
        if self.project_id is not None: body['project_id'] = self.project_id
        if self.region is not None: body['region'] = self.region
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> GoogleCloudVertexAiConfig:
        """Deserializes the GoogleCloudVertexAiConfig from a dictionary."""
        return cls(private_key=d.get('private_key', None),
                   private_key_plaintext=d.get('private_key_plaintext', None),
                   project_id=d.get('project_id', None),
                   region=d.get('region', None))


@dataclass
class ListEndpointsResponse:
    endpoints: Optional[List[ServingEndpoint]] = None
    """The list of endpoints."""

    def as_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.endpoints: body['endpoints'] = [v.as_dict() for v in self.endpoints]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ListEndpointsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.endpoints: body['endpoints'] = self.endpoints
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ListEndpointsResponse:
        """Deserializes the ListEndpointsResponse from a dictionary."""
        return cls(endpoints=_repeated_dict(d, 'endpoints', ServingEndpoint))


@dataclass
class ModelDataPlaneInfo:
    query_info: Optional[oauth2.DataPlaneInfo] = None
    """Information required to query DataPlane API 'query' endpoint."""

    def as_dict(self) -> dict:
        """Serializes the ModelDataPlaneInfo into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.query_info: body['query_info'] = self.query_info.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ModelDataPlaneInfo into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.query_info: body['query_info'] = self.query_info
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ModelDataPlaneInfo:
        """Deserializes the ModelDataPlaneInfo from a dictionary."""
        return cls(query_info=_from_dict(d, 'query_info', oauth2.DataPlaneInfo))


@dataclass
class OpenAiConfig:
    microsoft_entra_client_id: Optional[str] = None
    """This field is only required for Azure AD OpenAI and is the Microsoft Entra Client ID."""

    microsoft_entra_client_secret: Optional[str] = None
    """The Databricks secret key reference for a client secret used for Microsoft Entra ID
    authentication. If you prefer to paste your client secret directly, see
    `microsoft_entra_client_secret_plaintext`. You must provide an API key using one of the
    following fields: `microsoft_entra_client_secret` or `microsoft_entra_client_secret_plaintext`."""

    microsoft_entra_client_secret_plaintext: Optional[str] = None
    """The client secret used for Microsoft Entra ID authentication provided as a plaintext string. If
    you prefer to reference your key using Databricks Secrets, see `microsoft_entra_client_secret`.
    You must provide an API key using one of the following fields: `microsoft_entra_client_secret`
    or `microsoft_entra_client_secret_plaintext`."""

    microsoft_entra_tenant_id: Optional[str] = None
    """This field is only required for Azure AD OpenAI and is the Microsoft Entra Tenant ID."""

    openai_api_base: Optional[str] = None
    """This is a field to provide a customized base URl for the OpenAI API. For Azure OpenAI, this
    field is required, and is the base URL for the Azure OpenAI API service provided by Azure. For
    other OpenAI API types, this field is optional, and if left unspecified, the standard OpenAI
    base URL is used."""

    openai_api_key: Optional[str] = None
    """The Databricks secret key reference for an OpenAI API key using the OpenAI or Azure service. If
    you prefer to paste your API key directly, see `openai_api_key_plaintext`. You must provide an
    API key using one of the following fields: `openai_api_key` or `openai_api_key_plaintext`."""

    openai_api_key_plaintext: Optional[str] = None
    """The OpenAI API key using the OpenAI or Azure service provided as a plaintext string. If you
    prefer to reference your key using Databricks Secrets, see `openai_api_key`. You must provide an
    API key using one of the following fields: `openai_api_key` or `openai_api_key_plaintext`."""

    openai_api_type: Optional[str] = None
    """This is an optional field to specify the type of OpenAI API to use. For Azure OpenAI, this field
    is required, and adjust this parameter to represent the preferred security access validation
    protocol. For access token validation, use azure. For authentication using Azure Active
    Directory (Azure AD) use, azuread."""

    openai_api_version: Optional[str] = None
    """This is an optional field to specify the OpenAI API version. For Azure OpenAI, this field is
    required, and is the version of the Azure OpenAI service to utilize, specified by a date."""

    openai_deployment_name: Optional[str] = None
    """This field is only required for Azure OpenAI and is the name of the deployment resource for the
    Azure OpenAI service."""

    openai_organization: Optional[str] = None
    """This is an optional field to specify the organization in OpenAI or Azure OpenAI."""

    def as_dict(self) -> dict:
        """Serializes the OpenAiConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.microsoft_entra_client_id is not None:
            body['microsoft_entra_client_id'] = self.microsoft_entra_client_id
        if self.microsoft_entra_client_secret is not None:
            body['microsoft_entra_client_secret'] = self.microsoft_entra_client_secret
        if self.microsoft_entra_client_secret_plaintext is not None:
            body['microsoft_entra_client_secret_plaintext'] = self.microsoft_entra_client_secret_plaintext
        if self.microsoft_entra_tenant_id is not None:
            body['microsoft_entra_tenant_id'] = self.microsoft_entra_tenant_id
        if self.openai_api_base is not None: body['openai_api_base'] = self.openai_api_base
        if self.openai_api_key is not None: body['openai_api_key'] = self.openai_api_key
        if self.openai_api_key_plaintext is not None:
            body['openai_api_key_plaintext'] = self.openai_api_key_plaintext
        if self.openai_api_type is not None: body['openai_api_type'] = self.openai_api_type
        if self.openai_api_version is not None: body['openai_api_version'] = self.openai_api_version
        if self.openai_deployment_name is not None:
            body['openai_deployment_name'] = self.openai_deployment_name
        if self.openai_organization is not None: body['openai_organization'] = self.openai_organization
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the OpenAiConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.microsoft_entra_client_id is not None:
            body['microsoft_entra_client_id'] = self.microsoft_entra_client_id
        if self.microsoft_entra_client_secret is not None:
            body['microsoft_entra_client_secret'] = self.microsoft_entra_client_secret
        if self.microsoft_entra_client_secret_plaintext is not None:
            body['microsoft_entra_client_secret_plaintext'] = self.microsoft_entra_client_secret_plaintext
        if self.microsoft_entra_tenant_id is not None:
            body['microsoft_entra_tenant_id'] = self.microsoft_entra_tenant_id
        if self.openai_api_base is not None: body['openai_api_base'] = self.openai_api_base
        if self.openai_api_key is not None: body['openai_api_key'] = self.openai_api_key
        if self.openai_api_key_plaintext is not None:
            body['openai_api_key_plaintext'] = self.openai_api_key_plaintext
        if self.openai_api_type is not None: body['openai_api_type'] = self.openai_api_type
        if self.openai_api_version is not None: body['openai_api_version'] = self.openai_api_version
        if self.openai_deployment_name is not None:
            body['openai_deployment_name'] = self.openai_deployment_name
        if self.openai_organization is not None: body['openai_organization'] = self.openai_organization
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> OpenAiConfig:
        """Deserializes the OpenAiConfig from a dictionary."""
        return cls(microsoft_entra_client_id=d.get('microsoft_entra_client_id', None),
                   microsoft_entra_client_secret=d.get('microsoft_entra_client_secret', None),
                   microsoft_entra_client_secret_plaintext=d.get('microsoft_entra_client_secret_plaintext',
                                                                 None),
                   microsoft_entra_tenant_id=d.get('microsoft_entra_tenant_id', None),
                   openai_api_base=d.get('openai_api_base', None),
                   openai_api_key=d.get('openai_api_key', None),
                   openai_api_key_plaintext=d.get('openai_api_key_plaintext', None),
                   openai_api_type=d.get('openai_api_type', None),
                   openai_api_version=d.get('openai_api_version', None),
                   openai_deployment_name=d.get('openai_deployment_name', None),
                   openai_organization=d.get('openai_organization', None))


@dataclass
class PaLmConfig:
    palm_api_key: Optional[str] = None
    """The Databricks secret key reference for a PaLM API key. If you prefer to paste your API key
    directly, see `palm_api_key_plaintext`. You must provide an API key using one of the following
    fields: `palm_api_key` or `palm_api_key_plaintext`."""

    palm_api_key_plaintext: Optional[str] = None
    """The PaLM API key provided as a plaintext string. If you prefer to reference your key using
    Databricks Secrets, see `palm_api_key`. You must provide an API key using one of the following
    fields: `palm_api_key` or `palm_api_key_plaintext`."""

    def as_dict(self) -> dict:
        """Serializes the PaLmConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.palm_api_key is not None: body['palm_api_key'] = self.palm_api_key
        if self.palm_api_key_plaintext is not None:
            body['palm_api_key_plaintext'] = self.palm_api_key_plaintext
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PaLmConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.palm_api_key is not None: body['palm_api_key'] = self.palm_api_key
        if self.palm_api_key_plaintext is not None:
            body['palm_api_key_plaintext'] = self.palm_api_key_plaintext
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PaLmConfig:
        """Deserializes the PaLmConfig from a dictionary."""
        return cls(palm_api_key=d.get('palm_api_key', None),
                   palm_api_key_plaintext=d.get('palm_api_key_plaintext', None))


@dataclass
class PatchServingEndpointTags:
    add_tags: Optional[List[EndpointTag]] = None
    """List of endpoint tags to add"""

    delete_tags: Optional[List[str]] = None
    """List of tag keys to delete"""

    name: Optional[str] = None
    """The name of the serving endpoint who's tags to patch. This field is required."""

    def as_dict(self) -> dict:
        """Serializes the PatchServingEndpointTags into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.add_tags: body['add_tags'] = [v.as_dict() for v in self.add_tags]
        if self.delete_tags: body['delete_tags'] = [v for v in self.delete_tags]
        if self.name is not None: body['name'] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PatchServingEndpointTags into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.add_tags: body['add_tags'] = self.add_tags
        if self.delete_tags: body['delete_tags'] = self.delete_tags
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PatchServingEndpointTags:
        """Deserializes the PatchServingEndpointTags from a dictionary."""
        return cls(add_tags=_repeated_dict(d, 'add_tags', EndpointTag),
                   delete_tags=d.get('delete_tags', None),
                   name=d.get('name', None))


@dataclass
class PayloadTable:
    name: Optional[str] = None
    """The name of the payload table."""

    status: Optional[str] = None
    """The status of the payload table."""

    status_message: Optional[str] = None
    """The status message of the payload table."""

    def as_dict(self) -> dict:
        """Serializes the PayloadTable into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.status is not None: body['status'] = self.status
        if self.status_message is not None: body['status_message'] = self.status_message
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PayloadTable into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.name is not None: body['name'] = self.name
        if self.status is not None: body['status'] = self.status
        if self.status_message is not None: body['status_message'] = self.status_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PayloadTable:
        """Deserializes the PayloadTable from a dictionary."""
        return cls(name=d.get('name', None),
                   status=d.get('status', None),
                   status_message=d.get('status_message', None))


@dataclass
class PutAiGatewayResponse:
    guardrails: Optional[AiGatewayGuardrails] = None
    """Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and
    responses."""

    inference_table_config: Optional[AiGatewayInferenceTableConfig] = None
    """Configuration for payload logging using inference tables. Use these tables to monitor and audit
    data being sent to and received from model APIs and to improve model quality ."""

    rate_limits: Optional[List[AiGatewayRateLimit]] = None
    """Configuration for rate limits which can be set to limit endpoint traffic."""

    usage_tracking_config: Optional[AiGatewayUsageTrackingConfig] = None
    """Configuration to enable usage tracking using system tables. These tables allow you to monitor
    operational usage on endpoints and their associated costs."""

    def as_dict(self) -> dict:
        """Serializes the PutAiGatewayResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.guardrails: body['guardrails'] = self.guardrails.as_dict()
        if self.inference_table_config: body['inference_table_config'] = self.inference_table_config.as_dict()
        if self.rate_limits: body['rate_limits'] = [v.as_dict() for v in self.rate_limits]
        if self.usage_tracking_config: body['usage_tracking_config'] = self.usage_tracking_config.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PutAiGatewayResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.guardrails: body['guardrails'] = self.guardrails
        if self.inference_table_config: body['inference_table_config'] = self.inference_table_config
        if self.rate_limits: body['rate_limits'] = self.rate_limits
        if self.usage_tracking_config: body['usage_tracking_config'] = self.usage_tracking_config
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PutAiGatewayResponse:
        """Deserializes the PutAiGatewayResponse from a dictionary."""
        return cls(guardrails=_from_dict(d, 'guardrails', AiGatewayGuardrails),
                   inference_table_config=_from_dict(d, 'inference_table_config',
                                                     AiGatewayInferenceTableConfig),
                   rate_limits=_repeated_dict(d, 'rate_limits', AiGatewayRateLimit),
                   usage_tracking_config=_from_dict(d, 'usage_tracking_config', AiGatewayUsageTrackingConfig))


@dataclass
class PutResponse:
    rate_limits: Optional[List[RateLimit]] = None
    """The list of endpoint rate limits."""

    def as_dict(self) -> dict:
        """Serializes the PutResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.rate_limits: body['rate_limits'] = [v.as_dict() for v in self.rate_limits]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the PutResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.rate_limits: body['rate_limits'] = self.rate_limits
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> PutResponse:
        """Deserializes the PutResponse from a dictionary."""
        return cls(rate_limits=_repeated_dict(d, 'rate_limits', RateLimit))


@dataclass
class QueryEndpointInput:
    dataframe_records: Optional[List[Any]] = None
    """Pandas Dataframe input in the records orientation."""

    dataframe_split: Optional[DataframeSplitInput] = None
    """Pandas Dataframe input in the split orientation."""

    extra_params: Optional[Dict[str, str]] = None
    """The extra parameters field used ONLY for __completions, chat,__ and __embeddings external &
    foundation model__ serving endpoints. This is a map of strings and should only be used with
    other external/foundation model query fields."""

    input: Optional[Any] = None
    """The input string (or array of strings) field used ONLY for __embeddings external & foundation
    model__ serving endpoints and is the only field (along with extra_params if needed) used by
    embeddings queries."""

    inputs: Optional[Any] = None
    """Tensor-based input in columnar format."""

    instances: Optional[List[Any]] = None
    """Tensor-based input in row format."""

    max_tokens: Optional[int] = None
    """The max tokens field used ONLY for __completions__ and __chat external & foundation model__
    serving endpoints. This is an integer and should only be used with other chat/completions query
    fields."""

    messages: Optional[List[ChatMessage]] = None
    """The messages field used ONLY for __chat external & foundation model__ serving endpoints. This is
    a map of strings and should only be used with other chat query fields."""

    n: Optional[int] = None
    """The n (number of candidates) field used ONLY for __completions__ and __chat external &
    foundation model__ serving endpoints. This is an integer between 1 and 5 with a default of 1 and
    should only be used with other chat/completions query fields."""

    name: Optional[str] = None
    """The name of the serving endpoint. This field is required."""

    prompt: Optional[Any] = None
    """The prompt string (or array of strings) field used ONLY for __completions external & foundation
    model__ serving endpoints and should only be used with other completions query fields."""

    stop: Optional[List[str]] = None
    """The stop sequences field used ONLY for __completions__ and __chat external & foundation model__
    serving endpoints. This is a list of strings and should only be used with other chat/completions
    query fields."""

    stream: Optional[bool] = None
    """The stream field used ONLY for __completions__ and __chat external & foundation model__ serving
    endpoints. This is a boolean defaulting to false and should only be used with other
    chat/completions query fields."""

    temperature: Optional[float] = None
    """The temperature field used ONLY for __completions__ and __chat external & foundation model__
    serving endpoints. This is a float between 0.0 and 2.0 with a default of 1.0 and should only be
    used with other chat/completions query fields."""

    def as_dict(self) -> dict:
        """Serializes the QueryEndpointInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.dataframe_records: body['dataframe_records'] = [v for v in self.dataframe_records]
        if self.dataframe_split: body['dataframe_split'] = self.dataframe_split.as_dict()
        if self.extra_params: body['extra_params'] = self.extra_params
        if self.input: body['input'] = self.input
        if self.inputs: body['inputs'] = self.inputs
        if self.instances: body['instances'] = [v for v in self.instances]
        if self.max_tokens is not None: body['max_tokens'] = self.max_tokens
        if self.messages: body['messages'] = [v.as_dict() for v in self.messages]
        if self.n is not None: body['n'] = self.n
        if self.name is not None: body['name'] = self.name
        if self.prompt: body['prompt'] = self.prompt
        if self.stop: body['stop'] = [v for v in self.stop]
        if self.stream is not None: body['stream'] = self.stream
        if self.temperature is not None: body['temperature'] = self.temperature
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryEndpointInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.dataframe_records: body['dataframe_records'] = self.dataframe_records
        if self.dataframe_split: body['dataframe_split'] = self.dataframe_split
        if self.extra_params: body['extra_params'] = self.extra_params
        if self.input: body['input'] = self.input
        if self.inputs: body['inputs'] = self.inputs
        if self.instances: body['instances'] = self.instances
        if self.max_tokens is not None: body['max_tokens'] = self.max_tokens
        if self.messages: body['messages'] = self.messages
        if self.n is not None: body['n'] = self.n
        if self.name is not None: body['name'] = self.name
        if self.prompt: body['prompt'] = self.prompt
        if self.stop: body['stop'] = self.stop
        if self.stream is not None: body['stream'] = self.stream
        if self.temperature is not None: body['temperature'] = self.temperature
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryEndpointInput:
        """Deserializes the QueryEndpointInput from a dictionary."""
        return cls(dataframe_records=d.get('dataframe_records', None),
                   dataframe_split=_from_dict(d, 'dataframe_split', DataframeSplitInput),
                   extra_params=d.get('extra_params', None),
                   input=d.get('input', None),
                   inputs=d.get('inputs', None),
                   instances=d.get('instances', None),
                   max_tokens=d.get('max_tokens', None),
                   messages=_repeated_dict(d, 'messages', ChatMessage),
                   n=d.get('n', None),
                   name=d.get('name', None),
                   prompt=d.get('prompt', None),
                   stop=d.get('stop', None),
                   stream=d.get('stream', None),
                   temperature=d.get('temperature', None))


@dataclass
class QueryEndpointResponse:
    choices: Optional[List[V1ResponseChoiceElement]] = None
    """The list of choices returned by the __chat or completions external/foundation model__ serving
    endpoint."""

    created: Optional[int] = None
    """The timestamp in seconds when the query was created in Unix time returned by a __completions or
    chat external/foundation model__ serving endpoint."""

    data: Optional[List[EmbeddingsV1ResponseEmbeddingElement]] = None
    """The list of the embeddings returned by the __embeddings external/foundation model__ serving
    endpoint."""

    id: Optional[str] = None
    """The ID of the query that may be returned by a __completions or chat external/foundation model__
    serving endpoint."""

    model: Optional[str] = None
    """The name of the __external/foundation model__ used for querying. This is the name of the model
    that was specified in the endpoint config."""

    object: Optional[QueryEndpointResponseObject] = None
    """The type of object returned by the __external/foundation model__ serving endpoint, one of
    [text_completion, chat.completion, list (of embeddings)]."""

    predictions: Optional[List[Any]] = None
    """The predictions returned by the serving endpoint."""

    served_model_name: Optional[str] = None
    """The name of the served model that served the request. This is useful when there are multiple
    models behind the same endpoint with traffic split."""

    usage: Optional[ExternalModelUsageElement] = None
    """The usage object that may be returned by the __external/foundation model__ serving endpoint.
    This contains information about the number of tokens used in the prompt and response."""

    def as_dict(self) -> dict:
        """Serializes the QueryEndpointResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.choices: body['choices'] = [v.as_dict() for v in self.choices]
        if self.created is not None: body['created'] = self.created
        if self.data: body['data'] = [v.as_dict() for v in self.data]
        if self.id is not None: body['id'] = self.id
        if self.model is not None: body['model'] = self.model
        if self.object is not None: body['object'] = self.object.value
        if self.predictions: body['predictions'] = [v for v in self.predictions]
        if self.served_model_name is not None: body['served-model-name'] = self.served_model_name
        if self.usage: body['usage'] = self.usage.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the QueryEndpointResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.choices: body['choices'] = self.choices
        if self.created is not None: body['created'] = self.created
        if self.data: body['data'] = self.data
        if self.id is not None: body['id'] = self.id
        if self.model is not None: body['model'] = self.model
        if self.object is not None: body['object'] = self.object
        if self.predictions: body['predictions'] = self.predictions
        if self.served_model_name is not None: body['served-model-name'] = self.served_model_name
        if self.usage: body['usage'] = self.usage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> QueryEndpointResponse:
        """Deserializes the QueryEndpointResponse from a dictionary."""
        return cls(choices=_repeated_dict(d, 'choices', V1ResponseChoiceElement),
                   created=d.get('created', None),
                   data=_repeated_dict(d, 'data', EmbeddingsV1ResponseEmbeddingElement),
                   id=d.get('id', None),
                   model=d.get('model', None),
                   object=_enum(d, 'object', QueryEndpointResponseObject),
                   predictions=d.get('predictions', None),
                   served_model_name=d.get('served-model-name', None),
                   usage=_from_dict(d, 'usage', ExternalModelUsageElement))


class QueryEndpointResponseObject(Enum):
    """The type of object returned by the __external/foundation model__ serving endpoint, one of
    [text_completion, chat.completion, list (of embeddings)]."""

    CHAT_COMPLETION = 'chat.completion'
    LIST = 'list'
    TEXT_COMPLETION = 'text_completion'


@dataclass
class RateLimit:
    calls: int
    """Used to specify how many calls are allowed for a key within the renewal_period."""

    renewal_period: RateLimitRenewalPeriod
    """Renewal period field for a serving endpoint rate limit. Currently, only 'minute' is supported."""

    key: Optional[RateLimitKey] = None
    """Key field for a serving endpoint rate limit. Currently, only 'user' and 'endpoint' are
    supported, with 'endpoint' being the default if not specified."""

    def as_dict(self) -> dict:
        """Serializes the RateLimit into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.calls is not None: body['calls'] = self.calls
        if self.key is not None: body['key'] = self.key.value
        if self.renewal_period is not None: body['renewal_period'] = self.renewal_period.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the RateLimit into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.calls is not None: body['calls'] = self.calls
        if self.key is not None: body['key'] = self.key
        if self.renewal_period is not None: body['renewal_period'] = self.renewal_period
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> RateLimit:
        """Deserializes the RateLimit from a dictionary."""
        return cls(calls=d.get('calls', None),
                   key=_enum(d, 'key', RateLimitKey),
                   renewal_period=_enum(d, 'renewal_period', RateLimitRenewalPeriod))


class RateLimitKey(Enum):
    """Key field for a serving endpoint rate limit. Currently, only 'user' and 'endpoint' are
    supported, with 'endpoint' being the default if not specified."""

    ENDPOINT = 'endpoint'
    USER = 'user'


class RateLimitRenewalPeriod(Enum):
    """Renewal period field for a serving endpoint rate limit. Currently, only 'minute' is supported."""

    MINUTE = 'minute'


@dataclass
class Route:
    served_model_name: str
    """The name of the served model this route configures traffic for."""

    traffic_percentage: int
    """The percentage of endpoint traffic to send to this route. It must be an integer between 0 and
    100 inclusive."""

    def as_dict(self) -> dict:
        """Serializes the Route into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.served_model_name is not None: body['served_model_name'] = self.served_model_name
        if self.traffic_percentage is not None: body['traffic_percentage'] = self.traffic_percentage
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the Route into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.served_model_name is not None: body['served_model_name'] = self.served_model_name
        if self.traffic_percentage is not None: body['traffic_percentage'] = self.traffic_percentage
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> Route:
        """Deserializes the Route from a dictionary."""
        return cls(served_model_name=d.get('served_model_name', None),
                   traffic_percentage=d.get('traffic_percentage', None))


@dataclass
class ServedEntityInput:
    entity_name: Optional[str] = None
    """The name of the entity to be served. The entity may be a model in the Databricks Model Registry,
    a model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC
    object, the full name of the object should be given in the form of
    __catalog_name__.__schema_name__.__model_name__."""

    entity_version: Optional[str] = None
    """The version of the model in Databricks Model Registry to be served or empty if the entity is a
    FEATURE_SPEC."""

    environment_vars: Optional[Dict[str, str]] = None
    """An object containing a set of optional, user-specified environment variable key-value pairs used
    for serving this entity. Note: this is an experimental feature and subject to change. Example
    entity environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY":
    "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`"""

    external_model: Optional[ExternalModel] = None
    """The external model to be served. NOTE: Only one of external_model and (entity_name,
    entity_version, workload_size, workload_type, and scale_to_zero_enabled) can be specified with
    the latter set being used for custom model serving for a Databricks registered model. For an
    existing endpoint with external_model, it cannot be updated to an endpoint without
    external_model. If the endpoint is created without external_model, users cannot update it to add
    external_model later. The task type of all external models within an endpoint must be the same."""

    instance_profile_arn: Optional[str] = None
    """ARN of the instance profile that the served entity uses to access AWS resources."""

    max_provisioned_throughput: Optional[int] = None
    """The maximum tokens per second that the endpoint can scale up to."""

    min_provisioned_throughput: Optional[int] = None
    """The minimum tokens per second that the endpoint can scale down to."""

    name: Optional[str] = None
    """The name of a served entity. It must be unique across an endpoint. A served entity name can
    consist of alphanumeric characters, dashes, and underscores. If not specified for an external
    model, this field defaults to external_model.name, with '.' and ':' replaced with '-', and if
    not specified for other entities, it defaults to <entity-name>-<entity-version>."""

    scale_to_zero_enabled: Optional[bool] = None
    """Whether the compute resources for the served entity should scale down to zero."""

    workload_size: Optional[str] = None
    """The workload size of the served entity. The workload size corresponds to a range of provisioned
    concurrency that the compute autoscales between. A single unit of provisioned concurrency can
    process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned concurrency),
    "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned concurrency). If
    scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size
    is 0."""

    workload_type: Optional[str] = None
    """The workload type of the served entity. The workload type selects which type of compute to use
    in the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU
    acceleration is available by selecting workload types like GPU_SMALL and others. See the
    available [GPU types].
    
    [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types"""

    def as_dict(self) -> dict:
        """Serializes the ServedEntityInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.external_model: body['external_model'] = self.external_model.as_dict()
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedEntityInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.external_model: body['external_model'] = self.external_model
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedEntityInput:
        """Deserializes the ServedEntityInput from a dictionary."""
        return cls(entity_name=d.get('entity_name', None),
                   entity_version=d.get('entity_version', None),
                   environment_vars=d.get('environment_vars', None),
                   external_model=_from_dict(d, 'external_model', ExternalModel),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_provisioned_throughput=d.get('max_provisioned_throughput', None),
                   min_provisioned_throughput=d.get('min_provisioned_throughput', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   workload_size=d.get('workload_size', None),
                   workload_type=d.get('workload_type', None))


@dataclass
class ServedEntityOutput:
    creation_timestamp: Optional[int] = None
    """The creation timestamp of the served entity in Unix time."""

    creator: Optional[str] = None
    """The email of the user who created the served entity."""

    entity_name: Optional[str] = None
    """The name of the entity served. The entity may be a model in the Databricks Model Registry, a
    model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC
    object, the full name of the object is given in the form of
    __catalog_name__.__schema_name__.__model_name__."""

    entity_version: Optional[str] = None
    """The version of the served entity in Databricks Model Registry or empty if the entity is a
    FEATURE_SPEC."""

    environment_vars: Optional[Dict[str, str]] = None
    """An object containing a set of optional, user-specified environment variable key-value pairs used
    for serving this entity. Note: this is an experimental feature and subject to change. Example
    entity environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY":
    "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`"""

    external_model: Optional[ExternalModel] = None
    """The external model that is served. NOTE: Only one of external_model, foundation_model, and
    (entity_name, entity_version, workload_size, workload_type, and scale_to_zero_enabled) is
    returned based on the endpoint type."""

    foundation_model: Optional[FoundationModel] = None
    """The foundation model that is served. NOTE: Only one of foundation_model, external_model, and
    (entity_name, entity_version, workload_size, workload_type, and scale_to_zero_enabled) is
    returned based on the endpoint type."""

    instance_profile_arn: Optional[str] = None
    """ARN of the instance profile that the served entity uses to access AWS resources."""

    max_provisioned_throughput: Optional[int] = None
    """The maximum tokens per second that the endpoint can scale up to."""

    min_provisioned_throughput: Optional[int] = None
    """The minimum tokens per second that the endpoint can scale down to."""

    name: Optional[str] = None
    """The name of the served entity."""

    scale_to_zero_enabled: Optional[bool] = None
    """Whether the compute resources for the served entity should scale down to zero."""

    state: Optional[ServedModelState] = None
    """Information corresponding to the state of the served entity."""

    workload_size: Optional[str] = None
    """The workload size of the served entity. The workload size corresponds to a range of provisioned
    concurrency that the compute autoscales between. A single unit of provisioned concurrency can
    process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned concurrency),
    "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned concurrency). If
    scale-to-zero is enabled, the lower bound of the provisioned concurrency for each workload size
    will be 0."""

    workload_type: Optional[str] = None
    """The workload type of the served entity. The workload type selects which type of compute to use
    in the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU
    acceleration is available by selecting workload types like GPU_SMALL and others. See the
    available [GPU types].
    
    [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types"""

    def as_dict(self) -> dict:
        """Serializes the ServedEntityOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.external_model: body['external_model'] = self.external_model.as_dict()
        if self.foundation_model: body['foundation_model'] = self.foundation_model.as_dict()
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state.as_dict()
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedEntityOutput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.external_model: body['external_model'] = self.external_model
        if self.foundation_model: body['foundation_model'] = self.foundation_model
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedEntityOutput:
        """Deserializes the ServedEntityOutput from a dictionary."""
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   entity_name=d.get('entity_name', None),
                   entity_version=d.get('entity_version', None),
                   environment_vars=d.get('environment_vars', None),
                   external_model=_from_dict(d, 'external_model', ExternalModel),
                   foundation_model=_from_dict(d, 'foundation_model', FoundationModel),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_provisioned_throughput=d.get('max_provisioned_throughput', None),
                   min_provisioned_throughput=d.get('min_provisioned_throughput', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   state=_from_dict(d, 'state', ServedModelState),
                   workload_size=d.get('workload_size', None),
                   workload_type=d.get('workload_type', None))


@dataclass
class ServedEntitySpec:
    entity_name: Optional[str] = None
    """The name of the entity served. The entity may be a model in the Databricks Model Registry, a
    model in the Unity Catalog (UC), or a function of type FEATURE_SPEC in the UC. If it is a UC
    object, the full name of the object is given in the form of
    __catalog_name__.__schema_name__.__model_name__."""

    entity_version: Optional[str] = None
    """The version of the served entity in Databricks Model Registry or empty if the entity is a
    FEATURE_SPEC."""

    external_model: Optional[ExternalModel] = None
    """The external model that is served. NOTE: Only one of external_model, foundation_model, and
    (entity_name, entity_version) is returned based on the endpoint type."""

    foundation_model: Optional[FoundationModel] = None
    """The foundation model that is served. NOTE: Only one of foundation_model, external_model, and
    (entity_name, entity_version) is returned based on the endpoint type."""

    name: Optional[str] = None
    """The name of the served entity."""

    def as_dict(self) -> dict:
        """Serializes the ServedEntitySpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.external_model: body['external_model'] = self.external_model.as_dict()
        if self.foundation_model: body['foundation_model'] = self.foundation_model.as_dict()
        if self.name is not None: body['name'] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedEntitySpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.entity_name is not None: body['entity_name'] = self.entity_name
        if self.entity_version is not None: body['entity_version'] = self.entity_version
        if self.external_model: body['external_model'] = self.external_model
        if self.foundation_model: body['foundation_model'] = self.foundation_model
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedEntitySpec:
        """Deserializes the ServedEntitySpec from a dictionary."""
        return cls(entity_name=d.get('entity_name', None),
                   entity_version=d.get('entity_version', None),
                   external_model=_from_dict(d, 'external_model', ExternalModel),
                   foundation_model=_from_dict(d, 'foundation_model', FoundationModel),
                   name=d.get('name', None))


@dataclass
class ServedModelInput:
    model_name: str
    """The name of the model in Databricks Model Registry to be served or if the model resides in Unity
    Catalog, the full name of model, in the form of __catalog_name__.__schema_name__.__model_name__."""

    model_version: str
    """The version of the model in Databricks Model Registry or Unity Catalog to be served."""

    scale_to_zero_enabled: bool
    """Whether the compute resources for the served model should scale down to zero."""

    environment_vars: Optional[Dict[str, str]] = None
    """An object containing a set of optional, user-specified environment variable key-value pairs used
    for serving this model. Note: this is an experimental feature and subject to change. Example
    model environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY":
    "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`"""

    instance_profile_arn: Optional[str] = None
    """ARN of the instance profile that the served model will use to access AWS resources."""

    max_provisioned_throughput: Optional[int] = None
    """The maximum tokens per second that the endpoint can scale up to."""

    min_provisioned_throughput: Optional[int] = None
    """The minimum tokens per second that the endpoint can scale down to."""

    name: Optional[str] = None
    """The name of a served model. It must be unique across an endpoint. If not specified, this field
    will default to <model-name>-<model-version>. A served model name can consist of alphanumeric
    characters, dashes, and underscores."""

    workload_size: Optional[ServedModelInputWorkloadSize] = None
    """The workload size of the served model. The workload size corresponds to a range of provisioned
    concurrency that the compute will autoscale between. A single unit of provisioned concurrency
    can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned
    concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned
    concurrency). If scale-to-zero is enabled, the lower bound of the provisioned concurrency for
    each workload size will be 0."""

    workload_type: Optional[ServedModelInputWorkloadType] = None
    """The workload type of the served model. The workload type selects which type of compute to use in
    the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU
    acceleration is available by selecting workload types like GPU_SMALL and others. See the
    available [GPU types].
    
    [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types"""

    def as_dict(self) -> dict:
        """Serializes the ServedModelInput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size is not None: body['workload_size'] = self.workload_size.value
        if self.workload_type is not None: body['workload_type'] = self.workload_type.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedModelInput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.max_provisioned_throughput is not None:
            body['max_provisioned_throughput'] = self.max_provisioned_throughput
        if self.min_provisioned_throughput is not None:
            body['min_provisioned_throughput'] = self.min_provisioned_throughput
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedModelInput:
        """Deserializes the ServedModelInput from a dictionary."""
        return cls(environment_vars=d.get('environment_vars', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   max_provisioned_throughput=d.get('max_provisioned_throughput', None),
                   min_provisioned_throughput=d.get('min_provisioned_throughput', None),
                   model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   workload_size=_enum(d, 'workload_size', ServedModelInputWorkloadSize),
                   workload_type=_enum(d, 'workload_type', ServedModelInputWorkloadType))


class ServedModelInputWorkloadSize(Enum):
    """The workload size of the served model. The workload size corresponds to a range of provisioned
    concurrency that the compute will autoscale between. A single unit of provisioned concurrency
    can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned
    concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned
    concurrency). If scale-to-zero is enabled, the lower bound of the provisioned concurrency for
    each workload size will be 0."""

    LARGE = 'Large'
    MEDIUM = 'Medium'
    SMALL = 'Small'


class ServedModelInputWorkloadType(Enum):
    """The workload type of the served model. The workload type selects which type of compute to use in
    the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU
    acceleration is available by selecting workload types like GPU_SMALL and others. See the
    available [GPU types].
    
    [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types"""

    CPU = 'CPU'
    GPU_LARGE = 'GPU_LARGE'
    GPU_MEDIUM = 'GPU_MEDIUM'
    GPU_SMALL = 'GPU_SMALL'
    MULTIGPU_MEDIUM = 'MULTIGPU_MEDIUM'


@dataclass
class ServedModelOutput:
    creation_timestamp: Optional[int] = None
    """The creation timestamp of the served model in Unix time."""

    creator: Optional[str] = None
    """The email of the user who created the served model."""

    environment_vars: Optional[Dict[str, str]] = None
    """An object containing a set of optional, user-specified environment variable key-value pairs used
    for serving this model. Note: this is an experimental feature and subject to change. Example
    model environment variables that refer to Databricks secrets: `{"OPENAI_API_KEY":
    "{{secrets/my_scope/my_key}}", "DATABRICKS_TOKEN": "{{secrets/my_scope2/my_key2}}"}`"""

    instance_profile_arn: Optional[str] = None
    """ARN of the instance profile that the served model will use to access AWS resources."""

    model_name: Optional[str] = None
    """The name of the model in Databricks Model Registry or the full name of the model in Unity
    Catalog."""

    model_version: Optional[str] = None
    """The version of the model in Databricks Model Registry or Unity Catalog to be served."""

    name: Optional[str] = None
    """The name of the served model."""

    scale_to_zero_enabled: Optional[bool] = None
    """Whether the compute resources for the Served Model should scale down to zero."""

    state: Optional[ServedModelState] = None
    """Information corresponding to the state of the Served Model."""

    workload_size: Optional[str] = None
    """The workload size of the served model. The workload size corresponds to a range of provisioned
    concurrency that the compute will autoscale between. A single unit of provisioned concurrency
    can process one request at a time. Valid workload sizes are "Small" (4 - 4 provisioned
    concurrency), "Medium" (8 - 16 provisioned concurrency), and "Large" (16 - 64 provisioned
    concurrency). If scale-to-zero is enabled, the lower bound of the provisioned concurrency for
    each workload size will be 0."""

    workload_type: Optional[str] = None
    """The workload type of the served model. The workload type selects which type of compute to use in
    the endpoint. The default value for this parameter is "CPU". For deep learning workloads, GPU
    acceleration is available by selecting workload types like GPU_SMALL and others. See the
    available [GPU types].
    
    [GPU types]: https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html#gpu-workload-types"""

    def as_dict(self) -> dict:
        """Serializes the ServedModelOutput into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state.as_dict()
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedModelOutput into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.environment_vars: body['environment_vars'] = self.environment_vars
        if self.instance_profile_arn is not None: body['instance_profile_arn'] = self.instance_profile_arn
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        if self.scale_to_zero_enabled is not None: body['scale_to_zero_enabled'] = self.scale_to_zero_enabled
        if self.state: body['state'] = self.state
        if self.workload_size is not None: body['workload_size'] = self.workload_size
        if self.workload_type is not None: body['workload_type'] = self.workload_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedModelOutput:
        """Deserializes the ServedModelOutput from a dictionary."""
        return cls(creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   environment_vars=d.get('environment_vars', None),
                   instance_profile_arn=d.get('instance_profile_arn', None),
                   model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None),
                   scale_to_zero_enabled=d.get('scale_to_zero_enabled', None),
                   state=_from_dict(d, 'state', ServedModelState),
                   workload_size=d.get('workload_size', None),
                   workload_type=d.get('workload_type', None))


@dataclass
class ServedModelSpec:
    model_name: Optional[str] = None
    """The name of the model in Databricks Model Registry or the full name of the model in Unity
    Catalog."""

    model_version: Optional[str] = None
    """The version of the model in Databricks Model Registry or Unity Catalog to be served."""

    name: Optional[str] = None
    """The name of the served model."""

    def as_dict(self) -> dict:
        """Serializes the ServedModelSpec into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedModelSpec into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.model_name is not None: body['model_name'] = self.model_name
        if self.model_version is not None: body['model_version'] = self.model_version
        if self.name is not None: body['name'] = self.name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedModelSpec:
        """Deserializes the ServedModelSpec from a dictionary."""
        return cls(model_name=d.get('model_name', None),
                   model_version=d.get('model_version', None),
                   name=d.get('name', None))


@dataclass
class ServedModelState:
    deployment: Optional[ServedModelStateDeployment] = None
    """The state of the served entity deployment. DEPLOYMENT_CREATING indicates that the served entity
    is not ready yet because the deployment is still being created (i.e container image is building,
    model server is deploying for the first time, etc.). DEPLOYMENT_RECOVERING indicates that the
    served entity was previously in a ready state but no longer is and is attempting to recover.
    DEPLOYMENT_READY indicates that the served entity is ready to receive traffic. DEPLOYMENT_FAILED
    indicates that there was an error trying to bring up the served entity (e.g container image
    build failed, the model server failed to start due to a model loading error, etc.)
    DEPLOYMENT_ABORTED indicates that the deployment was terminated likely due to a failure in
    bringing up another served entity under the same endpoint and config version."""

    deployment_state_message: Optional[str] = None
    """More information about the state of the served entity, if available."""

    def as_dict(self) -> dict:
        """Serializes the ServedModelState into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.deployment is not None: body['deployment'] = self.deployment.value
        if self.deployment_state_message is not None:
            body['deployment_state_message'] = self.deployment_state_message
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServedModelState into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.deployment is not None: body['deployment'] = self.deployment
        if self.deployment_state_message is not None:
            body['deployment_state_message'] = self.deployment_state_message
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServedModelState:
        """Deserializes the ServedModelState from a dictionary."""
        return cls(deployment=_enum(d, 'deployment', ServedModelStateDeployment),
                   deployment_state_message=d.get('deployment_state_message', None))


class ServedModelStateDeployment(Enum):
    """The state of the served entity deployment. DEPLOYMENT_CREATING indicates that the served entity
    is not ready yet because the deployment is still being created (i.e container image is building,
    model server is deploying for the first time, etc.). DEPLOYMENT_RECOVERING indicates that the
    served entity was previously in a ready state but no longer is and is attempting to recover.
    DEPLOYMENT_READY indicates that the served entity is ready to receive traffic. DEPLOYMENT_FAILED
    indicates that there was an error trying to bring up the served entity (e.g container image
    build failed, the model server failed to start due to a model loading error, etc.)
    DEPLOYMENT_ABORTED indicates that the deployment was terminated likely due to a failure in
    bringing up another served entity under the same endpoint and config version."""

    ABORTED = 'DEPLOYMENT_ABORTED'
    CREATING = 'DEPLOYMENT_CREATING'
    FAILED = 'DEPLOYMENT_FAILED'
    READY = 'DEPLOYMENT_READY'
    RECOVERING = 'DEPLOYMENT_RECOVERING'


@dataclass
class ServerLogsResponse:
    logs: str
    """The most recent log lines of the model server processing invocation requests."""

    def as_dict(self) -> dict:
        """Serializes the ServerLogsResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServerLogsResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.logs is not None: body['logs'] = self.logs
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServerLogsResponse:
        """Deserializes the ServerLogsResponse from a dictionary."""
        return cls(logs=d.get('logs', None))


@dataclass
class ServingEndpoint:
    ai_gateway: Optional[AiGatewayConfig] = None
    """The AI Gateway configuration for the serving endpoint. NOTE: Only external model endpoints are
    currently supported."""

    config: Optional[EndpointCoreConfigSummary] = None
    """The config that is currently being served by the endpoint."""

    creation_timestamp: Optional[int] = None
    """The timestamp when the endpoint was created in Unix time."""

    creator: Optional[str] = None
    """The email of the user who created the serving endpoint."""

    id: Optional[str] = None
    """System-generated ID of the endpoint. This is used to refer to the endpoint in the Permissions
    API"""

    last_updated_timestamp: Optional[int] = None
    """The timestamp when the endpoint was last updated by a user in Unix time."""

    name: Optional[str] = None
    """The name of the serving endpoint."""

    state: Optional[EndpointState] = None
    """Information corresponding to the state of the serving endpoint."""

    tags: Optional[List[EndpointTag]] = None
    """Tags attached to the serving endpoint."""

    task: Optional[str] = None
    """The task type of the serving endpoint."""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpoint into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway.as_dict()
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.state: body['state'] = self.state.as_dict()
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.task is not None: body['task'] = self.task
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpoint into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway
        if self.config: body['config'] = self.config
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.state: body['state'] = self.state
        if self.tags: body['tags'] = self.tags
        if self.task is not None: body['task'] = self.task
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpoint:
        """Deserializes the ServingEndpoint from a dictionary."""
        return cls(ai_gateway=_from_dict(d, 'ai_gateway', AiGatewayConfig),
                   config=_from_dict(d, 'config', EndpointCoreConfigSummary),
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   state=_from_dict(d, 'state', EndpointState),
                   tags=_repeated_dict(d, 'tags', EndpointTag),
                   task=d.get('task', None))


@dataclass
class ServingEndpointAccessControlRequest:
    group_name: Optional[str] = None
    """name of the group"""

    permission_level: Optional[ServingEndpointPermissionLevel] = None
    """Permission level"""

    service_principal_name: Optional[str] = None
    """application ID of a service principal"""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointAccessControlRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointAccessControlRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.permission_level is not None: body['permission_level'] = self.permission_level
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointAccessControlRequest:
        """Deserializes the ServingEndpointAccessControlRequest from a dictionary."""
        return cls(group_name=d.get('group_name', None),
                   permission_level=_enum(d, 'permission_level', ServingEndpointPermissionLevel),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ServingEndpointAccessControlResponse:
    all_permissions: Optional[List[ServingEndpointPermission]] = None
    """All permissions."""

    display_name: Optional[str] = None
    """Display name of the user or service principal."""

    group_name: Optional[str] = None
    """name of the group"""

    service_principal_name: Optional[str] = None
    """Name of the service principal."""

    user_name: Optional[str] = None
    """name of the user"""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointAccessControlResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.all_permissions: body['all_permissions'] = [v.as_dict() for v in self.all_permissions]
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointAccessControlResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.all_permissions: body['all_permissions'] = self.all_permissions
        if self.display_name is not None: body['display_name'] = self.display_name
        if self.group_name is not None: body['group_name'] = self.group_name
        if self.service_principal_name is not None:
            body['service_principal_name'] = self.service_principal_name
        if self.user_name is not None: body['user_name'] = self.user_name
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointAccessControlResponse:
        """Deserializes the ServingEndpointAccessControlResponse from a dictionary."""
        return cls(all_permissions=_repeated_dict(d, 'all_permissions', ServingEndpointPermission),
                   display_name=d.get('display_name', None),
                   group_name=d.get('group_name', None),
                   service_principal_name=d.get('service_principal_name', None),
                   user_name=d.get('user_name', None))


@dataclass
class ServingEndpointDetailed:
    ai_gateway: Optional[AiGatewayConfig] = None
    """The AI Gateway configuration for the serving endpoint. NOTE: Only external model endpoints are
    currently supported."""

    config: Optional[EndpointCoreConfigOutput] = None
    """The config that is currently being served by the endpoint."""

    creation_timestamp: Optional[int] = None
    """The timestamp when the endpoint was created in Unix time."""

    creator: Optional[str] = None
    """The email of the user who created the serving endpoint."""

    data_plane_info: Optional[ModelDataPlaneInfo] = None
    """Information required to query DataPlane APIs."""

    endpoint_url: Optional[str] = None
    """Endpoint invocation url if route optimization is enabled for endpoint"""

    id: Optional[str] = None
    """System-generated ID of the endpoint. This is used to refer to the endpoint in the Permissions
    API"""

    last_updated_timestamp: Optional[int] = None
    """The timestamp when the endpoint was last updated by a user in Unix time."""

    name: Optional[str] = None
    """The name of the serving endpoint."""

    pending_config: Optional[EndpointPendingConfig] = None
    """The config that the endpoint is attempting to update to."""

    permission_level: Optional[ServingEndpointDetailedPermissionLevel] = None
    """The permission level of the principal making the request."""

    route_optimized: Optional[bool] = None
    """Boolean representing if route optimization has been enabled for the endpoint"""

    state: Optional[EndpointState] = None
    """Information corresponding to the state of the serving endpoint."""

    tags: Optional[List[EndpointTag]] = None
    """Tags attached to the serving endpoint."""

    task: Optional[str] = None
    """The task type of the serving endpoint."""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointDetailed into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway.as_dict()
        if self.config: body['config'] = self.config.as_dict()
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.data_plane_info: body['data_plane_info'] = self.data_plane_info.as_dict()
        if self.endpoint_url is not None: body['endpoint_url'] = self.endpoint_url
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.pending_config: body['pending_config'] = self.pending_config.as_dict()
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        if self.route_optimized is not None: body['route_optimized'] = self.route_optimized
        if self.state: body['state'] = self.state.as_dict()
        if self.tags: body['tags'] = [v.as_dict() for v in self.tags]
        if self.task is not None: body['task'] = self.task
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointDetailed into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.ai_gateway: body['ai_gateway'] = self.ai_gateway
        if self.config: body['config'] = self.config
        if self.creation_timestamp is not None: body['creation_timestamp'] = self.creation_timestamp
        if self.creator is not None: body['creator'] = self.creator
        if self.data_plane_info: body['data_plane_info'] = self.data_plane_info
        if self.endpoint_url is not None: body['endpoint_url'] = self.endpoint_url
        if self.id is not None: body['id'] = self.id
        if self.last_updated_timestamp is not None:
            body['last_updated_timestamp'] = self.last_updated_timestamp
        if self.name is not None: body['name'] = self.name
        if self.pending_config: body['pending_config'] = self.pending_config
        if self.permission_level is not None: body['permission_level'] = self.permission_level
        if self.route_optimized is not None: body['route_optimized'] = self.route_optimized
        if self.state: body['state'] = self.state
        if self.tags: body['tags'] = self.tags
        if self.task is not None: body['task'] = self.task
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointDetailed:
        """Deserializes the ServingEndpointDetailed from a dictionary."""
        return cls(ai_gateway=_from_dict(d, 'ai_gateway', AiGatewayConfig),
                   config=_from_dict(d, 'config', EndpointCoreConfigOutput),
                   creation_timestamp=d.get('creation_timestamp', None),
                   creator=d.get('creator', None),
                   data_plane_info=_from_dict(d, 'data_plane_info', ModelDataPlaneInfo),
                   endpoint_url=d.get('endpoint_url', None),
                   id=d.get('id', None),
                   last_updated_timestamp=d.get('last_updated_timestamp', None),
                   name=d.get('name', None),
                   pending_config=_from_dict(d, 'pending_config', EndpointPendingConfig),
                   permission_level=_enum(d, 'permission_level', ServingEndpointDetailedPermissionLevel),
                   route_optimized=d.get('route_optimized', None),
                   state=_from_dict(d, 'state', EndpointState),
                   tags=_repeated_dict(d, 'tags', EndpointTag),
                   task=d.get('task', None))


class ServingEndpointDetailedPermissionLevel(Enum):
    """The permission level of the principal making the request."""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_QUERY = 'CAN_QUERY'
    CAN_VIEW = 'CAN_VIEW'


@dataclass
class ServingEndpointPermission:
    inherited: Optional[bool] = None

    inherited_from_object: Optional[List[str]] = None

    permission_level: Optional[ServingEndpointPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointPermission into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = [v for v in self.inherited_from_object]
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointPermission into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.inherited is not None: body['inherited'] = self.inherited
        if self.inherited_from_object: body['inherited_from_object'] = self.inherited_from_object
        if self.permission_level is not None: body['permission_level'] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointPermission:
        """Deserializes the ServingEndpointPermission from a dictionary."""
        return cls(inherited=d.get('inherited', None),
                   inherited_from_object=d.get('inherited_from_object', None),
                   permission_level=_enum(d, 'permission_level', ServingEndpointPermissionLevel))


class ServingEndpointPermissionLevel(Enum):
    """Permission level"""

    CAN_MANAGE = 'CAN_MANAGE'
    CAN_QUERY = 'CAN_QUERY'
    CAN_VIEW = 'CAN_VIEW'


@dataclass
class ServingEndpointPermissions:
    access_control_list: Optional[List[ServingEndpointAccessControlResponse]] = None

    object_id: Optional[str] = None

    object_type: Optional[str] = None

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointPermissions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointPermissions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list: body['access_control_list'] = self.access_control_list
        if self.object_id is not None: body['object_id'] = self.object_id
        if self.object_type is not None: body['object_type'] = self.object_type
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointPermissions:
        """Deserializes the ServingEndpointPermissions from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list',
                                                      ServingEndpointAccessControlResponse),
                   object_id=d.get('object_id', None),
                   object_type=d.get('object_type', None))


@dataclass
class ServingEndpointPermissionsDescription:
    description: Optional[str] = None

    permission_level: Optional[ServingEndpointPermissionLevel] = None
    """Permission level"""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointPermissionsDescription into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level.value
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointPermissionsDescription into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description is not None: body['description'] = self.description
        if self.permission_level is not None: body['permission_level'] = self.permission_level
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointPermissionsDescription:
        """Deserializes the ServingEndpointPermissionsDescription from a dictionary."""
        return cls(description=d.get('description', None),
                   permission_level=_enum(d, 'permission_level', ServingEndpointPermissionLevel))


@dataclass
class ServingEndpointPermissionsRequest:
    access_control_list: Optional[List[ServingEndpointAccessControlRequest]] = None

    serving_endpoint_id: Optional[str] = None
    """The serving endpoint for which to get or manage permissions."""

    def as_dict(self) -> dict:
        """Serializes the ServingEndpointPermissionsRequest into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.access_control_list:
            body['access_control_list'] = [v.as_dict() for v in self.access_control_list]
        if self.serving_endpoint_id is not None: body['serving_endpoint_id'] = self.serving_endpoint_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the ServingEndpointPermissionsRequest into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.access_control_list: body['access_control_list'] = self.access_control_list
        if self.serving_endpoint_id is not None: body['serving_endpoint_id'] = self.serving_endpoint_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> ServingEndpointPermissionsRequest:
        """Deserializes the ServingEndpointPermissionsRequest from a dictionary."""
        return cls(access_control_list=_repeated_dict(d, 'access_control_list',
                                                      ServingEndpointAccessControlRequest),
                   serving_endpoint_id=d.get('serving_endpoint_id', None))


@dataclass
class TrafficConfig:
    routes: Optional[List[Route]] = None
    """The list of routes that define traffic to each served entity."""

    def as_dict(self) -> dict:
        """Serializes the TrafficConfig into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.routes: body['routes'] = [v.as_dict() for v in self.routes]
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the TrafficConfig into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.routes: body['routes'] = self.routes
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> TrafficConfig:
        """Deserializes the TrafficConfig from a dictionary."""
        return cls(routes=_repeated_dict(d, 'routes', Route))


@dataclass
class V1ResponseChoiceElement:
    finish_reason: Optional[str] = None
    """The finish reason returned by the endpoint."""

    index: Optional[int] = None
    """The index of the choice in the __chat or completions__ response."""

    logprobs: Optional[int] = None
    """The logprobs returned only by the __completions__ endpoint."""

    message: Optional[ChatMessage] = None
    """The message response from the __chat__ endpoint."""

    text: Optional[str] = None
    """The text response from the __completions__ endpoint."""

    def as_dict(self) -> dict:
        """Serializes the V1ResponseChoiceElement into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.finish_reason is not None: body['finishReason'] = self.finish_reason
        if self.index is not None: body['index'] = self.index
        if self.logprobs is not None: body['logprobs'] = self.logprobs
        if self.message: body['message'] = self.message.as_dict()
        if self.text is not None: body['text'] = self.text
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the V1ResponseChoiceElement into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.finish_reason is not None: body['finishReason'] = self.finish_reason
        if self.index is not None: body['index'] = self.index
        if self.logprobs is not None: body['logprobs'] = self.logprobs
        if self.message: body['message'] = self.message
        if self.text is not None: body['text'] = self.text
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> V1ResponseChoiceElement:
        """Deserializes the V1ResponseChoiceElement from a dictionary."""
        return cls(finish_reason=d.get('finishReason', None),
                   index=d.get('index', None),
                   logprobs=d.get('logprobs', None),
                   message=_from_dict(d, 'message', ChatMessage),
                   text=d.get('text', None))


class ServingEndpointsAPI:
    """The Serving Endpoints API allows you to create, update, and delete model serving endpoints.
    
    You can use a serving endpoint to serve models from the Databricks Model Registry or from Unity Catalog.
    Endpoints expose the underlying models as scalable REST API endpoints using serverless compute. This means
    the endpoints and associated compute resources are fully managed by Databricks and will not appear in your
    cloud account. A serving endpoint can consist of one or more MLflow models from the Databricks Model
    Registry, called served entities. A serving endpoint can have at most ten served entities. You can
    configure traffic settings to define how requests should be routed to your served entities behind an
    endpoint. Additionally, you can configure the scale of resources that should be applied to each served
    entity."""

    def __init__(self, api_client):
        self._api = api_client

    def wait_get_serving_endpoint_not_updating(
            self,
            name: str,
            timeout=timedelta(minutes=20),
            callback: Optional[Callable[[ServingEndpointDetailed], None]] = None) -> ServingEndpointDetailed:
        deadline = time.time() + timeout.total_seconds()
        target_states = (EndpointStateConfigUpdate.NOT_UPDATING, )
        failure_states = (EndpointStateConfigUpdate.UPDATE_FAILED, EndpointStateConfigUpdate.UPDATE_CANCELED,
                          )
        status_message = 'polling...'
        attempt = 1
        while time.time() < deadline:
            poll = self.get(name=name)
            status = poll.state.config_update
            status_message = f'current status: {status}'
            if status in target_states:
                return poll
            if callback:
                callback(poll)
            if status in failure_states:
                msg = f'failed to reach NOT_UPDATING, got {status}: {status_message}'
                raise OperationFailed(msg)
            prefix = f"name={name}"
            sleep = attempt
            if sleep > 10:
                # sleep 10s max per attempt
                sleep = 10
            _LOG.debug(f'{prefix}: ({status}) {status_message} (sleeping ~{sleep}s)')
            time.sleep(sleep + random.random())
            attempt += 1
        raise TimeoutError(f'timed out after {timeout}: {status_message}')

    def build_logs(self, name: str, served_model_name: str) -> BuildLogsResponse:
        """Get build logs for a served model.
        
        Retrieves the build logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that build logs will be retrieved for. This field is required.
        
        :returns: :class:`BuildLogsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/serving-endpoints/{name}/served-models/{served_model_name}/build-logs',
                           headers=headers)
        return BuildLogsResponse.from_dict(res)

    def create(self,
               name: str,
               config: EndpointCoreConfigInput,
               *,
               ai_gateway: Optional[AiGatewayConfig] = None,
               rate_limits: Optional[List[RateLimit]] = None,
               route_optimized: Optional[bool] = None,
               tags: Optional[List[EndpointTag]] = None) -> Wait[ServingEndpointDetailed]:
        """Create a new serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required and must be unique across a Databricks
          workspace. An endpoint name can consist of alphanumeric characters, dashes, and underscores.
        :param config: :class:`EndpointCoreConfigInput`
          The core config of the serving endpoint.
        :param ai_gateway: :class:`AiGatewayConfig` (optional)
          The AI Gateway configuration for the serving endpoint. NOTE: only external model endpoints are
          supported as of now.
        :param rate_limits: List[:class:`RateLimit`] (optional)
          Rate limits to be applied to the serving endpoint. NOTE: this field is deprecated, please use AI
          Gateway to manage rate limits.
        :param route_optimized: bool (optional)
          Enable route optimization for the serving endpoint.
        :param tags: List[:class:`EndpointTag`] (optional)
          Tags to be attached to the serving endpoint and automatically propagated to billing logs.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        """
        body = {}
        if ai_gateway is not None: body['ai_gateway'] = ai_gateway.as_dict()
        if config is not None: body['config'] = config.as_dict()
        if name is not None: body['name'] = name
        if rate_limits is not None: body['rate_limits'] = [v.as_dict() for v in rate_limits]
        if route_optimized is not None: body['route_optimized'] = route_optimized
        if tags is not None: body['tags'] = [v.as_dict() for v in tags]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('POST', '/api/2.0/serving-endpoints', body=body, headers=headers)
        return Wait(self.wait_get_serving_endpoint_not_updating,
                    response=ServingEndpointDetailed.from_dict(op_response),
                    name=op_response['name'])

    def create_and_wait(
        self,
        name: str,
        config: EndpointCoreConfigInput,
        *,
        ai_gateway: Optional[AiGatewayConfig] = None,
        rate_limits: Optional[List[RateLimit]] = None,
        route_optimized: Optional[bool] = None,
        tags: Optional[List[EndpointTag]] = None,
        timeout=timedelta(minutes=20)) -> ServingEndpointDetailed:
        return self.create(ai_gateway=ai_gateway,
                           config=config,
                           name=name,
                           rate_limits=rate_limits,
                           route_optimized=route_optimized,
                           tags=tags).result(timeout=timeout)

    def delete(self, name: str):
        """Delete a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('DELETE', f'/api/2.0/serving-endpoints/{name}', headers=headers)

    def export_metrics(self, name: str) -> ExportMetricsResponse:
        """Get metrics of a serving endpoint.
        
        Retrieves the metrics associated with the provided serving endpoint in either Prometheus or
        OpenMetrics exposition format.
        
        :param name: str
          The name of the serving endpoint to retrieve metrics for. This field is required.
        
        :returns: :class:`ExportMetricsResponse`
        """

        headers = {'Accept': 'text/plain', }

        res = self._api.do('GET', f'/api/2.0/serving-endpoints/{name}/metrics', headers=headers, raw=True)
        return ExportMetricsResponse.from_dict(res)

    def get(self, name: str) -> ServingEndpointDetailed:
        """Get a single serving endpoint.
        
        Retrieves the details for a single serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        
        :returns: :class:`ServingEndpointDetailed`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET', f'/api/2.0/serving-endpoints/{name}', headers=headers)
        return ServingEndpointDetailed.from_dict(res)

    def get_open_api(self, name: str):
        """Get the schema for a serving endpoint.
        
        Get the query schema of the serving endpoint in OpenAPI format. The schema contains information for
        the supported paths, input and output format and datatypes.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        
        
        """

        headers = {'Accept': 'application/json', }

        self._api.do('GET', f'/api/2.0/serving-endpoints/{name}/openapi', headers=headers)

    def get_permission_levels(self, serving_endpoint_id: str) -> GetServingEndpointPermissionLevelsResponse:
        """Get serving endpoint permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`GetServingEndpointPermissionLevelsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/permissions/serving-endpoints/{serving_endpoint_id}/permissionLevels',
                           headers=headers)
        return GetServingEndpointPermissionLevelsResponse.from_dict(res)

    def get_permissions(self, serving_endpoint_id: str) -> ServingEndpointPermissions:
        """Get serving endpoint permissions.
        
        Gets the permissions of a serving endpoint. Serving endpoints can inherit permissions from their root
        object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        
        :returns: :class:`ServingEndpointPermissions`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/permissions/serving-endpoints/{serving_endpoint_id}',
                           headers=headers)
        return ServingEndpointPermissions.from_dict(res)

    def list(self) -> Iterator[ServingEndpoint]:
        """Get all serving endpoints.
        
        :returns: Iterator over :class:`ServingEndpoint`
        """

        headers = {'Accept': 'application/json', }

        json = self._api.do('GET', '/api/2.0/serving-endpoints', headers=headers)
        parsed = ListEndpointsResponse.from_dict(json).endpoints
        return parsed if parsed is not None else []

    def logs(self, name: str, served_model_name: str) -> ServerLogsResponse:
        """Get the latest logs for a served model.
        
        Retrieves the service logs associated with the provided served model.
        
        :param name: str
          The name of the serving endpoint that the served model belongs to. This field is required.
        :param served_model_name: str
          The name of the served model that logs will be retrieved for. This field is required.
        
        :returns: :class:`ServerLogsResponse`
        """

        headers = {'Accept': 'application/json', }

        res = self._api.do('GET',
                           f'/api/2.0/serving-endpoints/{name}/served-models/{served_model_name}/logs',
                           headers=headers)
        return ServerLogsResponse.from_dict(res)

    def patch(self,
              name: str,
              *,
              add_tags: Optional[List[EndpointTag]] = None,
              delete_tags: Optional[List[str]] = None) -> Iterator[EndpointTag]:
        """Update tags of a serving endpoint.
        
        Used to batch add and delete tags from a serving endpoint with a single API call.
        
        :param name: str
          The name of the serving endpoint who's tags to patch. This field is required.
        :param add_tags: List[:class:`EndpointTag`] (optional)
          List of endpoint tags to add
        :param delete_tags: List[str] (optional)
          List of tag keys to delete
        
        :returns: Iterator over :class:`EndpointTag`
        """
        body = {}
        if add_tags is not None: body['add_tags'] = [v.as_dict() for v in add_tags]
        if delete_tags is not None: body['delete_tags'] = [v for v in delete_tags]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH', f'/api/2.0/serving-endpoints/{name}/tags', body=body, headers=headers)
        return [EndpointTag.from_dict(v) for v in res]

    def put(self, name: str, *, rate_limits: Optional[List[RateLimit]] = None) -> PutResponse:
        """Update rate limits of a serving endpoint.
        
        Used to update the rate limits of a serving endpoint. NOTE: Only foundation model endpoints are
        currently supported. For external models, use AI Gateway to manage rate limits.
        
        :param name: str
          The name of the serving endpoint whose rate limits are being updated. This field is required.
        :param rate_limits: List[:class:`RateLimit`] (optional)
          The list of endpoint rate limits.
        
        :returns: :class:`PutResponse`
        """
        body = {}
        if rate_limits is not None: body['rate_limits'] = [v.as_dict() for v in rate_limits]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.0/serving-endpoints/{name}/rate-limits',
                           body=body,
                           headers=headers)
        return PutResponse.from_dict(res)

    def put_ai_gateway(
            self,
            name: str,
            *,
            guardrails: Optional[AiGatewayGuardrails] = None,
            inference_table_config: Optional[AiGatewayInferenceTableConfig] = None,
            rate_limits: Optional[List[AiGatewayRateLimit]] = None,
            usage_tracking_config: Optional[AiGatewayUsageTrackingConfig] = None) -> PutAiGatewayResponse:
        """Update AI Gateway of a serving endpoint.
        
        Used to update the AI Gateway of a serving endpoint. NOTE: Only external model endpoints are currently
        supported.
        
        :param name: str
          The name of the serving endpoint whose AI Gateway is being updated. This field is required.
        :param guardrails: :class:`AiGatewayGuardrails` (optional)
          Configuration for AI Guardrails to prevent unwanted data and unsafe data in requests and responses.
        :param inference_table_config: :class:`AiGatewayInferenceTableConfig` (optional)
          Configuration for payload logging using inference tables. Use these tables to monitor and audit data
          being sent to and received from model APIs and to improve model quality.
        :param rate_limits: List[:class:`AiGatewayRateLimit`] (optional)
          Configuration for rate limits which can be set to limit endpoint traffic.
        :param usage_tracking_config: :class:`AiGatewayUsageTrackingConfig` (optional)
          Configuration to enable usage tracking using system tables. These tables allow you to monitor
          operational usage on endpoints and their associated costs.
        
        :returns: :class:`PutAiGatewayResponse`
        """
        body = {}
        if guardrails is not None: body['guardrails'] = guardrails.as_dict()
        if inference_table_config is not None:
            body['inference_table_config'] = inference_table_config.as_dict()
        if rate_limits is not None: body['rate_limits'] = [v.as_dict() for v in rate_limits]
        if usage_tracking_config is not None: body['usage_tracking_config'] = usage_tracking_config.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT', f'/api/2.0/serving-endpoints/{name}/ai-gateway', body=body, headers=headers)
        return PutAiGatewayResponse.from_dict(res)

    def query(self,
              name: str,
              *,
              dataframe_records: Optional[List[Any]] = None,
              dataframe_split: Optional[DataframeSplitInput] = None,
              extra_params: Optional[Dict[str, str]] = None,
              input: Optional[Any] = None,
              inputs: Optional[Any] = None,
              instances: Optional[List[Any]] = None,
              max_tokens: Optional[int] = None,
              messages: Optional[List[ChatMessage]] = None,
              n: Optional[int] = None,
              prompt: Optional[Any] = None,
              stop: Optional[List[str]] = None,
              stream: Optional[bool] = None,
              temperature: Optional[float] = None) -> QueryEndpointResponse:
        """Query a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        :param dataframe_records: List[Any] (optional)
          Pandas Dataframe input in the records orientation.
        :param dataframe_split: :class:`DataframeSplitInput` (optional)
          Pandas Dataframe input in the split orientation.
        :param extra_params: Dict[str,str] (optional)
          The extra parameters field used ONLY for __completions, chat,__ and __embeddings external &
          foundation model__ serving endpoints. This is a map of strings and should only be used with other
          external/foundation model query fields.
        :param input: Any (optional)
          The input string (or array of strings) field used ONLY for __embeddings external & foundation
          model__ serving endpoints and is the only field (along with extra_params if needed) used by
          embeddings queries.
        :param inputs: Any (optional)
          Tensor-based input in columnar format.
        :param instances: List[Any] (optional)
          Tensor-based input in row format.
        :param max_tokens: int (optional)
          The max tokens field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is an integer and should only be used with other chat/completions query fields.
        :param messages: List[:class:`ChatMessage`] (optional)
          The messages field used ONLY for __chat external & foundation model__ serving endpoints. This is a
          map of strings and should only be used with other chat query fields.
        :param n: int (optional)
          The n (number of candidates) field used ONLY for __completions__ and __chat external & foundation
          model__ serving endpoints. This is an integer between 1 and 5 with a default of 1 and should only be
          used with other chat/completions query fields.
        :param prompt: Any (optional)
          The prompt string (or array of strings) field used ONLY for __completions external & foundation
          model__ serving endpoints and should only be used with other completions query fields.
        :param stop: List[str] (optional)
          The stop sequences field used ONLY for __completions__ and __chat external & foundation model__
          serving endpoints. This is a list of strings and should only be used with other chat/completions
          query fields.
        :param stream: bool (optional)
          The stream field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a boolean defaulting to false and should only be used with other chat/completions
          query fields.
        :param temperature: float (optional)
          The temperature field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a float between 0.0 and 2.0 with a default of 1.0 and should only be used with
          other chat/completions query fields.
        
        :returns: :class:`QueryEndpointResponse`
        """
        body = {}
        if dataframe_records is not None: body['dataframe_records'] = [v for v in dataframe_records]
        if dataframe_split is not None: body['dataframe_split'] = dataframe_split.as_dict()
        if extra_params is not None: body['extra_params'] = extra_params
        if input is not None: body['input'] = input
        if inputs is not None: body['inputs'] = inputs
        if instances is not None: body['instances'] = [v for v in instances]
        if max_tokens is not None: body['max_tokens'] = max_tokens
        if messages is not None: body['messages'] = [v.as_dict() for v in messages]
        if n is not None: body['n'] = n
        if prompt is not None: body['prompt'] = prompt
        if stop is not None: body['stop'] = [v for v in stop]
        if stream is not None: body['stream'] = stream
        if temperature is not None: body['temperature'] = temperature
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = ['served-model-name', ]
        res = self._api.do('POST',
                           f'/serving-endpoints/{name}/invocations',
                           body=body,
                           headers=headers,
                           response_headers=response_headers)
        return QueryEndpointResponse.from_dict(res)

    def set_permissions(
        self,
        serving_endpoint_id: str,
        *,
        access_control_list: Optional[List[ServingEndpointAccessControlRequest]] = None
    ) -> ServingEndpointPermissions:
        """Set serving endpoint permissions.
        
        Sets permissions on an object, replacing existing permissions if they exist. Deletes all direct
        permissions if none are specified. Objects can inherit permissions from their root object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PUT',
                           f'/api/2.0/permissions/serving-endpoints/{serving_endpoint_id}',
                           body=body,
                           headers=headers)
        return ServingEndpointPermissions.from_dict(res)

    def update_config(self,
                      name: str,
                      *,
                      auto_capture_config: Optional[AutoCaptureConfigInput] = None,
                      served_entities: Optional[List[ServedEntityInput]] = None,
                      served_models: Optional[List[ServedModelInput]] = None,
                      traffic_config: Optional[TrafficConfig] = None) -> Wait[ServingEndpointDetailed]:
        """Update config of a serving endpoint.
        
        Updates any combination of the serving endpoint's served entities, the compute configuration of those
        served entities, and the endpoint's traffic config. An endpoint that already has an update in progress
        can not be updated until the current update completes or fails.
        
        :param name: str
          The name of the serving endpoint to update. This field is required.
        :param auto_capture_config: :class:`AutoCaptureConfigInput` (optional)
          Configuration for Inference Tables which automatically logs requests and responses to Unity Catalog.
        :param served_entities: List[:class:`ServedEntityInput`] (optional)
          A list of served entities for the endpoint to serve. A serving endpoint can have up to 15 served
          entities.
        :param served_models: List[:class:`ServedModelInput`] (optional)
          (Deprecated, use served_entities instead) A list of served models for the endpoint to serve. A
          serving endpoint can have up to 15 served models.
        :param traffic_config: :class:`TrafficConfig` (optional)
          The traffic config defining how invocations to the serving endpoint should be routed.
        
        :returns:
          Long-running operation waiter for :class:`ServingEndpointDetailed`.
          See :method:wait_get_serving_endpoint_not_updating for more details.
        """
        body = {}
        if auto_capture_config is not None: body['auto_capture_config'] = auto_capture_config.as_dict()
        if served_entities is not None: body['served_entities'] = [v.as_dict() for v in served_entities]
        if served_models is not None: body['served_models'] = [v.as_dict() for v in served_models]
        if traffic_config is not None: body['traffic_config'] = traffic_config.as_dict()
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        op_response = self._api.do('PUT',
                                   f'/api/2.0/serving-endpoints/{name}/config',
                                   body=body,
                                   headers=headers)
        return Wait(self.wait_get_serving_endpoint_not_updating,
                    response=ServingEndpointDetailed.from_dict(op_response),
                    name=op_response['name'])

    def update_config_and_wait(
        self,
        name: str,
        *,
        auto_capture_config: Optional[AutoCaptureConfigInput] = None,
        served_entities: Optional[List[ServedEntityInput]] = None,
        served_models: Optional[List[ServedModelInput]] = None,
        traffic_config: Optional[TrafficConfig] = None,
        timeout=timedelta(minutes=20)) -> ServingEndpointDetailed:
        return self.update_config(auto_capture_config=auto_capture_config,
                                  name=name,
                                  served_entities=served_entities,
                                  served_models=served_models,
                                  traffic_config=traffic_config).result(timeout=timeout)

    def update_permissions(
        self,
        serving_endpoint_id: str,
        *,
        access_control_list: Optional[List[ServingEndpointAccessControlRequest]] = None
    ) -> ServingEndpointPermissions:
        """Update serving endpoint permissions.
        
        Updates the permissions on a serving endpoint. Serving endpoints can inherit permissions from their
        root object.
        
        :param serving_endpoint_id: str
          The serving endpoint for which to get or manage permissions.
        :param access_control_list: List[:class:`ServingEndpointAccessControlRequest`] (optional)
        
        :returns: :class:`ServingEndpointPermissions`
        """
        body = {}
        if access_control_list is not None:
            body['access_control_list'] = [v.as_dict() for v in access_control_list]
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }

        res = self._api.do('PATCH',
                           f'/api/2.0/permissions/serving-endpoints/{serving_endpoint_id}',
                           body=body,
                           headers=headers)
        return ServingEndpointPermissions.from_dict(res)


class ServingEndpointsDataPlaneAPI:
    """Serving endpoints DataPlane provides a set of operations to interact with data plane endpoints for Serving
    endpoints service."""

    def __init__(self, api_client, control_plane):
        self._api = api_client
        self._control_plane = control_plane
        self._data_plane_service = DataPlaneService()

    def query(self,
              name: str,
              *,
              dataframe_records: Optional[List[Any]] = None,
              dataframe_split: Optional[DataframeSplitInput] = None,
              extra_params: Optional[Dict[str, str]] = None,
              input: Optional[Any] = None,
              inputs: Optional[Any] = None,
              instances: Optional[List[Any]] = None,
              max_tokens: Optional[int] = None,
              messages: Optional[List[ChatMessage]] = None,
              n: Optional[int] = None,
              prompt: Optional[Any] = None,
              stop: Optional[List[str]] = None,
              stream: Optional[bool] = None,
              temperature: Optional[float] = None) -> QueryEndpointResponse:
        """Query a serving endpoint.
        
        :param name: str
          The name of the serving endpoint. This field is required.
        :param dataframe_records: List[Any] (optional)
          Pandas Dataframe input in the records orientation.
        :param dataframe_split: :class:`DataframeSplitInput` (optional)
          Pandas Dataframe input in the split orientation.
        :param extra_params: Dict[str,str] (optional)
          The extra parameters field used ONLY for __completions, chat,__ and __embeddings external &
          foundation model__ serving endpoints. This is a map of strings and should only be used with other
          external/foundation model query fields.
        :param input: Any (optional)
          The input string (or array of strings) field used ONLY for __embeddings external & foundation
          model__ serving endpoints and is the only field (along with extra_params if needed) used by
          embeddings queries.
        :param inputs: Any (optional)
          Tensor-based input in columnar format.
        :param instances: List[Any] (optional)
          Tensor-based input in row format.
        :param max_tokens: int (optional)
          The max tokens field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is an integer and should only be used with other chat/completions query fields.
        :param messages: List[:class:`ChatMessage`] (optional)
          The messages field used ONLY for __chat external & foundation model__ serving endpoints. This is a
          map of strings and should only be used with other chat query fields.
        :param n: int (optional)
          The n (number of candidates) field used ONLY for __completions__ and __chat external & foundation
          model__ serving endpoints. This is an integer between 1 and 5 with a default of 1 and should only be
          used with other chat/completions query fields.
        :param prompt: Any (optional)
          The prompt string (or array of strings) field used ONLY for __completions external & foundation
          model__ serving endpoints and should only be used with other completions query fields.
        :param stop: List[str] (optional)
          The stop sequences field used ONLY for __completions__ and __chat external & foundation model__
          serving endpoints. This is a list of strings and should only be used with other chat/completions
          query fields.
        :param stream: bool (optional)
          The stream field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a boolean defaulting to false and should only be used with other chat/completions
          query fields.
        :param temperature: float (optional)
          The temperature field used ONLY for __completions__ and __chat external & foundation model__ serving
          endpoints. This is a float between 0.0 and 2.0 with a default of 1.0 and should only be used with
          other chat/completions query fields.
        
        :returns: :class:`QueryEndpointResponse`
        """
        body = {}
        if dataframe_records is not None: body['dataframe_records'] = [v for v in dataframe_records]
        if dataframe_split is not None: body['dataframe_split'] = dataframe_split.as_dict()
        if extra_params is not None: body['extra_params'] = extra_params
        if input is not None: body['input'] = input
        if inputs is not None: body['inputs'] = inputs
        if instances is not None: body['instances'] = [v for v in instances]
        if max_tokens is not None: body['max_tokens'] = max_tokens
        if messages is not None: body['messages'] = [v.as_dict() for v in messages]
        if n is not None: body['n'] = n
        if prompt is not None: body['prompt'] = prompt
        if stop is not None: body['stop'] = [v for v in stop]
        if stream is not None: body['stream'] = stream
        if temperature is not None: body['temperature'] = temperature

        def info_getter():
            response = self._control_plane.get(name=name, )
            if response.data_plane_info is None:
                raise Exception("Resource does not support direct Data Plane access")
            return response.data_plane_info.query_info

        get_params = [name, ]
        data_plane_details = self._data_plane_service.get_data_plane_details('query', get_params, info_getter,
                                                                             self._api.get_oauth_token)
        token = data_plane_details.token

        def auth(r: requests.PreparedRequest) -> requests.PreparedRequest:
            authorization = f"{token.token_type} {token.access_token}"
            r.headers["Authorization"] = authorization
            return r

        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', }
        response_headers = ['served-model-name', ]
        res = self._api.do('POST',
                           url=data_plane_details.endpoint_url,
                           body=body,
                           headers=headers,
                           response_headers=response_headers,
                           auth=auth)
        return QueryEndpointResponse.from_dict(res)
