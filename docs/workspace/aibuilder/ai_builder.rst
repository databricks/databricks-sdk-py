``w.ai_builder``: AI Builder Service
====================================
.. currentmodule:: databricks.sdk.service.aibuilder

.. py:class:: AiBuilderAPI

    The Custom LLMs service manages state and powers the UI for the Custom LLM product.

    .. py:method:: cancel_optimize(id: str)

        Cancel a Custom LLM Optimization Run.

        :param id: str


        

    .. py:method:: create_custom_llm(name: str, instructions: str [, agent_artifact_path: Optional[str], datasets: Optional[List[Dataset]], guidelines: Optional[List[str]]]) -> CustomLlm

        Create a Custom LLM.

        :param name: str
          Name of the custom LLM. Only alphanumeric characters and dashes allowed.
        :param instructions: str
          Instructions for the custom LLM to follow
        :param agent_artifact_path: str (optional)
          Optional: UC path for agent artifacts. If you are using a dataset that you only have read
          permissions, please provide a destination path where you have write permissions. Please provide this
          in catalog.schema format.
        :param datasets: List[:class:`Dataset`] (optional)
          Datasets used for training and evaluating the model, not for inference. Currently, only 1 dataset is
          accepted.
        :param guidelines: List[str] (optional)
          Guidelines for the custom LLM to adhere to

        :returns: :class:`CustomLlm`
        

    .. py:method:: delete_custom_llm(id: str)

        Delete a Custom LLM.

        :param id: str
          The id of the custom llm


        

    .. py:method:: get_custom_llm(id: str) -> CustomLlm

        Get a Custom LLM.

        :param id: str
          The id of the custom llm

        :returns: :class:`CustomLlm`
        

    .. py:method:: start_optimize(id: str) -> CustomLlm

        Start a Custom LLM Optimization Run.

        :param id: str
          The Id of the tile.

        :returns: :class:`CustomLlm`
        

    .. py:method:: update_custom_llm(id: str, custom_llm: CustomLlm, update_mask: str) -> CustomLlm

        Update a Custom LLM.

        :param id: str
          The id of the custom llm
        :param custom_llm: :class:`CustomLlm`
          The CustomLlm containing the fields which should be updated.
        :param update_mask: str
          The list of the CustomLlm fields to update. These should correspond to the values (or lack thereof)
          present in `custom_llm`.

          The field mask must be a single string, with multiple fields separated by commas (no spaces). The
          field path is relative to the resource object, using a dot (`.`) to navigate sub-fields (e.g.,
          `author.given_name`). Specification of elements in sequence or map fields is not allowed, as only
          the entire collection field can be specified. Field names must exactly match the resource field
          names.

          A field mask of `*` indicates full replacement. It’s recommended to always explicitly list the
          fields being updated and avoid using `*` wildcards, as it can lead to unintended results if the API
          changes in the future.

        :returns: :class:`CustomLlm`
        