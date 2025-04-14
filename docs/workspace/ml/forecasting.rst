``w.forecasting``: Forecasting
==============================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: ForecastingAPI

    The Forecasting API allows you to create and get serverless forecasting experiments

    .. py:method:: create_experiment(train_data_path: str, target_column: str, time_column: str, forecast_granularity: str, forecast_horizon: int [, custom_weights_column: Optional[str], experiment_path: Optional[str], holiday_regions: Optional[List[str]], include_features: Optional[List[str]], max_runtime: Optional[int], prediction_data_path: Optional[str], primary_metric: Optional[str], register_to: Optional[str], split_column: Optional[str], timeseries_identifier_columns: Optional[List[str]], training_frameworks: Optional[List[str]]]) -> Wait[ForecastingExperiment]

        Create a forecasting experiment.

        Creates a serverless forecasting experiment. Returns the experiment ID.

        :param train_data_path: str
          The fully qualified name of a Unity Catalog table, formatted as catalog_name.schema_name.table_name,
          used as training data for the forecasting model.
        :param target_column: str
          The column in the input training table used as the prediction target for model training. The values
          in this column are used as the ground truth for model training.
        :param time_column: str
          The column in the input training table that represents each row's timestamp.
        :param forecast_granularity: str
          The time interval between consecutive rows in the time series data. Possible values include: '1
          second', '1 minute', '5 minutes', '10 minutes', '15 minutes', '30 minutes', 'Hourly', 'Daily',
          'Weekly', 'Monthly', 'Quarterly', 'Yearly'.
        :param forecast_horizon: int
          The number of time steps into the future to make predictions, calculated as a multiple of
          forecast_granularity. This value represents how far ahead the model should forecast.
        :param custom_weights_column: str (optional)
          The column in the training table used to customize weights for each time series.
        :param experiment_path: str (optional)
          The path in the workspace to store the created experiment.
        :param holiday_regions: List[str] (optional)
          The region code(s) to automatically add holiday features. Currently supports only one region.
        :param include_features: List[str] (optional)
          Specifies the list of feature columns to include in model training. These columns must exist in the
          training data and be of type string, numerical, or boolean. If not specified, no additional features
          will be included. Note: Certain columns are automatically handled: - Automatically excluded:
          split_column, target_column, custom_weights_column. - Automatically included: time_column.
        :param max_runtime: int (optional)
          The maximum duration for the experiment in minutes. The experiment stops automatically if it exceeds
          this limit.
        :param prediction_data_path: str (optional)
          The fully qualified path of a Unity Catalog table, formatted as catalog_name.schema_name.table_name,
          used to store predictions.
        :param primary_metric: str (optional)
          The evaluation metric used to optimize the forecasting model.
        :param register_to: str (optional)
          The fully qualified path of a Unity Catalog model, formatted as catalog_name.schema_name.model_name,
          used to store the best model.
        :param split_column: str (optional)
          // The column in the training table used for custom data splits. Values must be 'train', 'validate',
          or 'test'.
        :param timeseries_identifier_columns: List[str] (optional)
          The column in the training table used to group the dataset for predicting individual time series.
        :param training_frameworks: List[str] (optional)
          List of frameworks to include for model tuning. Possible values are 'Prophet', 'ARIMA', 'DeepAR'. An
          empty list includes all supported frameworks.

        :returns:
          Long-running operation waiter for :class:`ForecastingExperiment`.
          See :method:wait_get_experiment_forecasting_succeeded for more details.
        

    .. py:method:: create_experiment_and_wait(train_data_path: str, target_column: str, time_column: str, forecast_granularity: str, forecast_horizon: int [, custom_weights_column: Optional[str], experiment_path: Optional[str], holiday_regions: Optional[List[str]], include_features: Optional[List[str]], max_runtime: Optional[int], prediction_data_path: Optional[str], primary_metric: Optional[str], register_to: Optional[str], split_column: Optional[str], timeseries_identifier_columns: Optional[List[str]], training_frameworks: Optional[List[str]], timeout: datetime.timedelta = 2:00:00]) -> ForecastingExperiment


    .. py:method:: get_experiment(experiment_id: str) -> ForecastingExperiment

        Get a forecasting experiment.

        Public RPC to get forecasting experiment

        :param experiment_id: str
          The unique ID of a forecasting experiment

        :returns: :class:`ForecastingExperiment`
        

    .. py:method:: wait_get_experiment_forecasting_succeeded(experiment_id: str, timeout: datetime.timedelta = 2:00:00, callback: Optional[Callable[[ForecastingExperiment], None]]) -> ForecastingExperiment
