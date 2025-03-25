``w.forecasting``: Forecasting
==============================
.. currentmodule:: databricks.sdk.service.ml

.. py:class:: ForecastingAPI

    The Forecasting API allows you to create and get serverless forecasting experiments

    .. py:method:: create_experiment(train_data_path: str, target_column: str, time_column: str, forecast_granularity: str, forecast_horizon: int [, custom_weights_column: Optional[str], experiment_path: Optional[str], holiday_regions: Optional[List[str]], max_runtime: Optional[int], prediction_data_path: Optional[str], primary_metric: Optional[str], register_to: Optional[str], split_column: Optional[str], timeseries_identifier_columns: Optional[List[str]], training_frameworks: Optional[List[str]]]) -> Wait[ForecastingExperiment]

        Create a forecasting experiment.

        Creates a serverless forecasting experiment. Returns the experiment ID.

        :param train_data_path: str
          The three-level (fully qualified) name of a unity catalog table. This table serves as the training
          data for the forecasting model.
        :param target_column: str
          Name of the column in the input training table that serves as the prediction target. The values in
          this column will be used as the ground truth for model training.
        :param time_column: str
          Name of the column in the input training table that represents the timestamp of each row.
        :param forecast_granularity: str
          The granularity of the forecast. This defines the time interval between consecutive rows in the time
          series data. Possible values: '1 second', '1 minute', '5 minutes', '10 minutes', '15 minutes', '30
          minutes', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly'.
        :param forecast_horizon: int
          The number of time steps into the future for which predictions should be made. This value represents
          a multiple of forecast_granularity determining how far ahead the model will forecast.
        :param custom_weights_column: str (optional)
          Name of the column in the input training table used to customize the weight for each time series to
          calculate weighted metrics.
        :param experiment_path: str (optional)
          The path to the created experiment. This is the path where the experiment will be stored in the
          workspace.
        :param holiday_regions: List[str] (optional)
          Region code(s) to consider when automatically adding holiday features. When empty, no holiday
          features are added. Only supports 1 holiday region for now.
        :param max_runtime: int (optional)
          The maximum duration in minutes for which the experiment is allowed to run. If the experiment
          exceeds this time limit it will be stopped automatically.
        :param prediction_data_path: str (optional)
          The three-level (fully qualified) path to a unity catalog table. This table path serves to store the
          predictions.
        :param primary_metric: str (optional)
          The evaluation metric used to optimize the forecasting model.
        :param register_to: str (optional)
          The three-level (fully qualified) path to a unity catalog model. This model path serves to store the
          best model.
        :param split_column: str (optional)
          Name of the column in the input training table used for custom data splits. The values in this
          column must be "train", "validate", or "test" to indicate which split each row belongs to.
        :param timeseries_identifier_columns: List[str] (optional)
          Name of the column in the input training table used to group the dataset to predict individual time
          series
        :param training_frameworks: List[str] (optional)
          The list of frameworks to include for model tuning. Possible values: 'Prophet', 'ARIMA', 'DeepAR'.
          An empty list will include all supported frameworks.

        :returns:
          Long-running operation waiter for :class:`ForecastingExperiment`.
          See :method:wait_get_experiment_forecasting_succeeded for more details.
        

    .. py:method:: create_experiment_and_wait(train_data_path: str, target_column: str, time_column: str, forecast_granularity: str, forecast_horizon: int [, custom_weights_column: Optional[str], experiment_path: Optional[str], holiday_regions: Optional[List[str]], max_runtime: Optional[int], prediction_data_path: Optional[str], primary_metric: Optional[str], register_to: Optional[str], split_column: Optional[str], timeseries_identifier_columns: Optional[List[str]], training_frameworks: Optional[List[str]], timeout: datetime.timedelta = 2:00:00]) -> ForecastingExperiment


    .. py:method:: get_experiment(experiment_id: str) -> ForecastingExperiment

        Get a forecasting experiment.

        Public RPC to get forecasting experiment

        :param experiment_id: str
          The unique ID of a forecasting experiment

        :returns: :class:`ForecastingExperiment`
        

    .. py:method:: wait_get_experiment_forecasting_succeeded(experiment_id: str, timeout: datetime.timedelta = 2:00:00, callback: Optional[Callable[[ForecastingExperiment], None]]) -> ForecastingExperiment
