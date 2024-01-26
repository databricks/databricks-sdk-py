``w.model_registry``: Model Registry
====================================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: ModelRegistryAPI

    Note: This API reference documents APIs for the Workspace Model Registry. Databricks recommends using
    [Models in Unity Catalog](/api/workspace/registeredmodels) instead. Models in Unity Catalog provides
    centralized model governance, cross-workspace access, lineage, and deployment. Workspace Model Registry
    will be deprecated in the future.
    
    The Workspace Model Registry is a centralized model repository and a UI and set of APIs that enable you to
    manage the full lifecycle of MLflow Models.

    .. py:method:: approve_transition_request(name: str, version: str, stage: Stage, archive_existing_versions: bool [, comment: Optional[str]]) -> ApproveTransitionRequestResponse

        Approve transition request.
        
        Approves a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param archive_existing_versions: bool
          Specifies whether to archive all current model versions in the target stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`ApproveTransitionRequestResponse`
        

    .. py:method:: create_comment(name: str, version: str, comment: str) -> CreateCommentResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            mv = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")
            
            created = w.model_registry.create_comment(comment=f'sdk-{time.time_ns()}',
                                                      name=mv.model_version.name,
                                                      version=mv.model_version.version)
            
            # cleanup
            w.model_registry.delete_comment(id=created.comment.id)

        Post a comment.
        
        Posts a comment on a model version. A comment can be submitted either by a user or programmatically to
        display relevant information about the model. For example, test results or deployment errors.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param comment: str
          User-provided comment on the action.
        
        :returns: :class:`CreateCommentResponse`
        

    .. py:method:: create_model(name: str [, description: Optional[str], tags: Optional[List[ModelTag]]]) -> CreateModelResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')

        Create a model.
        
        Creates a new registered model with the name specified in the request body.
        
        Throws `RESOURCE_ALREADY_EXISTS` if a registered model with the given name exists.
        
        :param name: str
          Register models under this name
        :param description: str (optional)
          Optional description for registered model.
        :param tags: List[:class:`ModelTag`] (optional)
          Additional metadata for registered model.
        
        :returns: :class:`CreateModelResponse`
        

    .. py:method:: create_model_version(name: str, source: str [, description: Optional[str], run_id: Optional[str], run_link: Optional[str], tags: Optional[List[ModelVersionTag]]]) -> CreateModelVersionResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            mv = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")

        Create a model version.
        
        Creates a model version.
        
        :param name: str
          Register model under this name
        :param source: str
          URI indicating the location of the model artifacts.
        :param description: str (optional)
          Optional description for model version.
        :param run_id: str (optional)
          MLflow run ID for correlation, if `source` was generated by an experiment run in MLflow tracking
          server
        :param run_link: str (optional)
          MLflow run link - this is the exact link of the run that generated this model version, potentially
          hosted at another instance of MLflow.
        :param tags: List[:class:`ModelVersionTag`] (optional)
          Additional metadata for model version.
        
        :returns: :class:`CreateModelVersionResponse`
        

    .. py:method:: create_transition_request(name: str, version: str, stage: Stage [, comment: Optional[str]]) -> CreateTransitionRequestResponse

        Make a transition request.
        
        Creates a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`CreateTransitionRequestResponse`
        

    .. py:method:: create_webhook(events: List[RegistryWebhookEvent] [, description: Optional[str], http_url_spec: Optional[HttpUrlSpec], job_spec: Optional[JobSpec], model_name: Optional[str], status: Optional[RegistryWebhookStatus]]) -> CreateWebhookResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            created = w.model_registry.create_webhook(description=f'sdk-{time.time_ns()}',
                                                      events=[ml.RegistryWebhookEvent.MODEL_VERSION_CREATED],
                                                      http_url_spec=ml.HttpUrlSpec(url=w.config.host))
            
            # cleanup
            w.model_registry.delete_webhook(id=created.webhook.id)

        Create a webhook.
        
        **NOTE**: This endpoint is in Public Preview.
        
        Creates a registry webhook.
        
        :param events: List[:class:`RegistryWebhookEvent`]
          Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A new model version was
          created for the associated model.
          
          * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed.
          
          * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned.
          
          * `COMMENT_CREATED`: A user wrote a comment on a registered model.
          
          * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be
          specified for a registry-wide webhook, which can be created by not specifying a model name in the
          create request.
          
          * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
          
          * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging.
          
          * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production.
          
          * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
          
          * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to
          staging.
          
          * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to
          production.
          
          * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived.
        :param description: str (optional)
          User-specified description for the webhook.
        :param http_url_spec: :class:`HttpUrlSpec` (optional)
        :param job_spec: :class:`JobSpec` (optional)
        :param model_name: str (optional)
          Name of the model whose events would trigger this webhook.
        :param status: :class:`RegistryWebhookStatus` (optional)
          Enable or disable triggering the webhook, or put the webhook into test mode. The default is
          `ACTIVE`: * `ACTIVE`: Webhook is triggered when an associated event happens.
          
          * `DISABLED`: Webhook is not triggered.
          
          * `TEST_MODE`: Webhook can be triggered through the test endpoint, but is not triggered on a real
          event.
        
        :returns: :class:`CreateWebhookResponse`
        

    .. py:method:: delete_comment(id: str)

        Delete a comment.
        
        Deletes a comment on a model version.
        
        :param id: str
        
        
        

    .. py:method:: delete_model(name: str)

        Delete a model.
        
        Deletes a registered model.
        
        :param name: str
          Registered model unique name identifier.
        
        
        

    .. py:method:: delete_model_tag(name: str, key: str)

        Delete a model tag.
        
        Deletes the tag for a registered model.
        
        :param name: str
          Name of the registered model that the tag was logged under.
        :param key: str
          Name of the tag. The name must be an exact match; wild-card deletion is not supported. Maximum size
          is 250 bytes.
        
        
        

    .. py:method:: delete_model_version(name: str, version: str)

        Delete a model version.
        
        Deletes a model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        
        

    .. py:method:: delete_model_version_tag(name: str, version: str, key: str)

        Delete a model version tag.
        
        Deletes a model version tag.
        
        :param name: str
          Name of the registered model that the tag was logged under.
        :param version: str
          Model version number that the tag was logged under.
        :param key: str
          Name of the tag. The name must be an exact match; wild-card deletion is not supported. Maximum size
          is 250 bytes.
        
        
        

    .. py:method:: delete_transition_request(name: str, version: str, stage: DeleteTransitionRequestStage, creator: str [, comment: Optional[str]])

        Delete a transition request.
        
        Cancels a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`DeleteTransitionRequestStage`
          Target stage of the transition request. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param creator: str
          Username of the user who created this request. Of the transition requests matching the specified
          details, only the one transition created by this user will be deleted.
        :param comment: str (optional)
          User-provided comment on the action.
        
        
        

    .. py:method:: delete_webhook( [, id: Optional[str]])

        Delete a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Deletes a registry webhook.
        
        :param id: str (optional)
          Webhook ID required to delete a registry webhook.
        
        
        

    .. py:method:: get_latest_versions(name: str [, stages: Optional[List[str]]]) -> Iterator[ModelVersion]

        Get the latest version.
        
        Gets the latest version of a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param stages: List[str] (optional)
          List of stages.
        
        :returns: Iterator over :class:`ModelVersion`
        

    .. py:method:: get_model(name: str) -> GetModelResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            created = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            model = w.model_registry.get_model(name=created.registered_model.name)

        Get model.
        
        Get the details of a model. This is a Databricks workspace version of the [MLflow endpoint] that also
        returns the model's Databricks workspace ID and the permission level of the requesting user on the
        model.
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#get-registeredmodel
        
        :param name: str
          Registered model unique name identifier.
        
        :returns: :class:`GetModelResponse`
        

    .. py:method:: get_model_version(name: str, version: str) -> GetModelVersionResponse

        Get a model version.
        
        Get a model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        :returns: :class:`GetModelVersionResponse`
        

    .. py:method:: get_model_version_download_uri(name: str, version: str) -> GetModelVersionDownloadUriResponse

        Get a model version URI.
        
        Gets a URI to download the model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        
        :returns: :class:`GetModelVersionDownloadUriResponse`
        

    .. py:method:: get_permission_levels(registered_model_id: str) -> GetRegisteredModelPermissionLevelsResponse

        Get registered model permission levels.
        
        Gets the permission levels that a user can have on an object.
        
        :param registered_model_id: str
          The registered model for which to get or manage permissions.
        
        :returns: :class:`GetRegisteredModelPermissionLevelsResponse`
        

    .. py:method:: get_permissions(registered_model_id: str) -> RegisteredModelPermissions

        Get registered model permissions.
        
        Gets the permissions of a registered model. Registered models can inherit permissions from their root
        object.
        
        :param registered_model_id: str
          The registered model for which to get or manage permissions.
        
        :returns: :class:`RegisteredModelPermissions`
        

    .. py:method:: list_models( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[Model]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            all = w.model_registry.list_models(ml.ListModelsRequest())

        List models.
        
        Lists all available registered models, up to the limit specified in __max_results__.
        
        :param max_results: int (optional)
          Maximum number of registered models desired. Max threshold is 1000.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous query.
        
        :returns: Iterator over :class:`Model`
        

    .. py:method:: list_transition_requests(name: str, version: str) -> Iterator[Activity]

        List transition requests.
        
        Gets a list of all open stage transition requests for the model version.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        
        :returns: Iterator over :class:`Activity`
        

    .. py:method:: list_webhooks( [, events: Optional[List[RegistryWebhookEvent]], model_name: Optional[str], page_token: Optional[str]]) -> Iterator[RegistryWebhook]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            all = w.model_registry.list_webhooks(ml.ListWebhooksRequest())

        List registry webhooks.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Lists all registry webhooks.
        
        :param events: List[:class:`RegistryWebhookEvent`] (optional)
          If `events` is specified, any webhook with one or more of the specified trigger events is included
          in the output. If `events` is not specified, webhooks of all event types are included in the output.
        :param model_name: str (optional)
          If not specified, all webhooks associated with the specified events are listed, regardless of their
          associated model.
        :param page_token: str (optional)
          Token indicating the page of artifact results to fetch
        
        :returns: Iterator over :class:`RegistryWebhook`
        

    .. py:method:: reject_transition_request(name: str, version: str, stage: Stage [, comment: Optional[str]]) -> RejectTransitionRequestResponse

        Reject a transition request.
        
        Rejects a model version stage transition request.
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`RejectTransitionRequestResponse`
        

    .. py:method:: rename_model(name: str [, new_name: Optional[str]]) -> RenameModelResponse

        Rename a model.
        
        Renames a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param new_name: str (optional)
          If provided, updates the name for this `registered_model`.
        
        :returns: :class:`RenameModelResponse`
        

    .. py:method:: search_model_versions( [, filter: Optional[str], max_results: Optional[int], order_by: Optional[List[str]], page_token: Optional[str]]) -> Iterator[ModelVersion]

        Searches model versions.
        
        Searches for specific model versions based on the supplied __filter__.
        
        :param filter: str (optional)
          String filter condition, like "name='my-model-name'". Must be a single boolean condition, with
          string values wrapped in single quotes.
        :param max_results: int (optional)
          Maximum number of models desired. Max threshold is 10K.
        :param order_by: List[str] (optional)
          List of columns to be ordered by including model name, version, stage with an optional "DESC" or
          "ASC" annotation, where "ASC" is the default. Tiebreaks are done by latest stage transition
          timestamp, followed by name ASC, followed by version DESC.
        :param page_token: str (optional)
          Pagination token to go to next page based on previous search query.
        
        :returns: Iterator over :class:`ModelVersion`
        

    .. py:method:: search_models( [, filter: Optional[str], max_results: Optional[int], order_by: Optional[List[str]], page_token: Optional[str]]) -> Iterator[Model]

        Search models.
        
        Search for registered models based on the specified __filter__.
        
        :param filter: str (optional)
          String filter condition, like "name LIKE 'my-model-name'". Interpreted in the backend automatically
          as "name LIKE '%my-model-name%'". Single boolean condition, with string values wrapped in single
          quotes.
        :param max_results: int (optional)
          Maximum number of models desired. Default is 100. Max threshold is 1000.
        :param order_by: List[str] (optional)
          List of columns for ordering search results, which can include model name and last updated timestamp
          with an optional "DESC" or "ASC" annotation, where "ASC" is the default. Tiebreaks are done by model
          name ASC.
        :param page_token: str (optional)
          Pagination token to go to the next page based on a previous search query.
        
        :returns: Iterator over :class:`Model`
        

    .. py:method:: set_model_tag(name: str, key: str, value: str)

        Set a tag.
        
        Sets a tag on a registered model.
        
        :param name: str
          Unique name of the model.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. If a tag with this name already exists,
          its preexisting value will be replaced by the specified `value`. All storage backends are guaranteed
          to support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        

    .. py:method:: set_model_version_tag(name: str, version: str, key: str, value: str)

        Set a version tag.
        
        Sets a model version tag.
        
        :param name: str
          Unique name of the model.
        :param version: str
          Model version number.
        :param key: str
          Name of the tag. Maximum size depends on storage backend. If a tag with this name already exists,
          its preexisting value will be replaced by the specified `value`. All storage backends are guaranteed
          to support key values up to 250 bytes in size.
        :param value: str
          String value of the tag being logged. Maximum size depends on storage backend. All storage backends
          are guaranteed to support key values up to 5000 bytes in size.
        
        
        

    .. py:method:: set_permissions(registered_model_id: str [, access_control_list: Optional[List[RegisteredModelAccessControlRequest]]]) -> RegisteredModelPermissions

        Set registered model permissions.
        
        Sets permissions on a registered model. Registered models can inherit permissions from their root
        object.
        
        :param registered_model_id: str
          The registered model for which to get or manage permissions.
        :param access_control_list: List[:class:`RegisteredModelAccessControlRequest`] (optional)
        
        :returns: :class:`RegisteredModelPermissions`
        

    .. py:method:: test_registry_webhook(id: str [, event: Optional[RegistryWebhookEvent]]) -> TestRegistryWebhookResponse

        Test a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Tests a registry webhook.
        
        :param id: str
          Webhook ID
        :param event: :class:`RegistryWebhookEvent` (optional)
          If `event` is specified, the test trigger uses the specified event. If `event` is not specified, the
          test trigger uses a randomly chosen event associated with the webhook.
        
        :returns: :class:`TestRegistryWebhookResponse`
        

    .. py:method:: transition_stage(name: str, version: str, stage: Stage, archive_existing_versions: bool [, comment: Optional[str]]) -> TransitionStageResponse

        Transition a stage.
        
        Transition a model version's stage. This is a Databricks workspace version of the [MLflow endpoint]
        that also accepts a comment associated with the transition to be recorded.",
        
        [MLflow endpoint]: https://www.mlflow.org/docs/latest/rest-api.html#transition-modelversion-stage
        
        :param name: str
          Name of the model.
        :param version: str
          Version of the model.
        :param stage: :class:`Stage`
          Target stage of the transition. Valid values are:
          
          * `None`: The initial stage of a model version.
          
          * `Staging`: Staging or pre-production stage.
          
          * `Production`: Production stage.
          
          * `Archived`: Archived stage.
        :param archive_existing_versions: bool
          Specifies whether to archive all current model versions in the target stage.
        :param comment: str (optional)
          User-provided comment on the action.
        
        :returns: :class:`TransitionStageResponse`
        

    .. py:method:: update_comment(id: str, comment: str) -> UpdateCommentResponse


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            mv = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")
            
            created = w.model_registry.create_comment(comment=f'sdk-{time.time_ns()}',
                                                      name=mv.model_version.name,
                                                      version=mv.model_version.version)
            
            _ = w.model_registry.update_comment(comment=f'sdk-{time.time_ns()}', id=created.comment.id)
            
            # cleanup
            w.model_registry.delete_comment(id=created.comment.id)

        Update a comment.
        
        Post an edit to a comment on a model version.
        
        :param id: str
          Unique identifier of an activity
        :param comment: str
          User-provided comment on the action.
        
        :returns: :class:`UpdateCommentResponse`
        

    .. py:method:: update_model(name: str [, description: Optional[str]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            created = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")
            
            w.model_registry.update_model_version(description=f'sdk-{time.time_ns()}',
                                                  name=created.model_version.name,
                                                  version=created.model_version.version)

        Update model.
        
        Updates a registered model.
        
        :param name: str
          Registered model unique name identifier.
        :param description: str (optional)
          If provided, updates the description for this `registered_model`.
        
        
        

    .. py:method:: update_model_version(name: str, version: str [, description: Optional[str]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            model = w.model_registry.create_model(name=f'sdk-{time.time_ns()}')
            
            created = w.model_registry.create_model_version(name=model.registered_model.name, source="dbfs:/tmp")
            
            w.model_registry.update_model_version(description=f'sdk-{time.time_ns()}',
                                                  name=created.model_version.name,
                                                  version=created.model_version.version)

        Update model version.
        
        Updates the model version.
        
        :param name: str
          Name of the registered model
        :param version: str
          Model version number
        :param description: str (optional)
          If provided, updates the description for this `registered_model`.
        
        
        

    .. py:method:: update_permissions(registered_model_id: str [, access_control_list: Optional[List[RegisteredModelAccessControlRequest]]]) -> RegisteredModelPermissions

        Update registered model permissions.
        
        Updates the permissions on a registered model. Registered models can inherit permissions from their
        root object.
        
        :param registered_model_id: str
          The registered model for which to get or manage permissions.
        :param access_control_list: List[:class:`RegisteredModelAccessControlRequest`] (optional)
        
        :returns: :class:`RegisteredModelPermissions`
        

    .. py:method:: update_webhook(id: str [, description: Optional[str], events: Optional[List[RegistryWebhookEvent]], http_url_spec: Optional[HttpUrlSpec], job_spec: Optional[JobSpec], status: Optional[RegistryWebhookStatus]])


        Usage:

        .. code-block::

            import time
            
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service import ml
            
            w = WorkspaceClient()
            
            created = w.model_registry.create_webhook(description=f'sdk-{time.time_ns()}',
                                                      events=[ml.RegistryWebhookEvent.MODEL_VERSION_CREATED],
                                                      http_url_spec=ml.HttpUrlSpec(url=w.config.host))
            
            w.model_registry.update_webhook(id=created.webhook.id, description=f'sdk-{time.time_ns()}')
            
            # cleanup
            w.model_registry.delete_webhook(id=created.webhook.id)

        Update a webhook.
        
        **NOTE:** This endpoint is in Public Preview.
        
        Updates a registry webhook.
        
        :param id: str
          Webhook ID
        :param description: str (optional)
          User-specified description for the webhook.
        :param events: List[:class:`RegistryWebhookEvent`] (optional)
          Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A new model version was
          created for the associated model.
          
          * `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage was changed.
          
          * `TRANSITION_REQUEST_CREATED`: A user requested a model version’s stage be transitioned.
          
          * `COMMENT_CREATED`: A user wrote a comment on a registered model.
          
          * `REGISTERED_MODEL_CREATED`: A new registered model was created. This event type can only be
          specified for a registry-wide webhook, which can be created by not specifying a model name in the
          create request.
          
          * `MODEL_VERSION_TAG_SET`: A user set a tag on the model version.
          
          * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model version was transitioned to staging.
          
          * `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version was transitioned to production.
          
          * `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version was archived.
          
          * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A user requested a model version be transitioned to
          staging.
          
          * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user requested a model version be transitioned to
          production.
          
          * `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a model version be archived.
        :param http_url_spec: :class:`HttpUrlSpec` (optional)
        :param job_spec: :class:`JobSpec` (optional)
        :param status: :class:`RegistryWebhookStatus` (optional)
          Enable or disable triggering the webhook, or put the webhook into test mode. The default is
          `ACTIVE`: * `ACTIVE`: Webhook is triggered when an associated event happens.
          
          * `DISABLED`: Webhook is not triggered.
          
          * `TEST_MODE`: Webhook can be triggered through the test endpoint, but is not triggered on a real
          event.
        
        
        