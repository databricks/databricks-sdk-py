``w.serving_endpoints_data_plane``: Serving endpoints DataPlane
===============================================================
.. currentmodule:: databricks.sdk.service.serving

.. py:class:: ServingEndpointsDataPlaneAPI

    Serving endpoints DataPlane provides a set of operations to interact with data plane endpoints for Serving
    endpoints service.

    .. py:method:: query(name: str [, dataframe_records: Optional[List[Any]], dataframe_split: Optional[DataframeSplitInput], extra_params: Optional[Dict[str, str]], input: Optional[Any], inputs: Optional[Any], instances: Optional[List[Any]], max_tokens: Optional[int], messages: Optional[List[ChatMessage]], n: Optional[int], prompt: Optional[Any], stop: Optional[List[str]], stream: Optional[bool], temperature: Optional[float]]) -> QueryEndpointResponse

        Query a serving endpoint.
        
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
        