``w.custom_llms``: Custom LLMs Service
======================================
.. currentmodule:: databricks.sdk.service.aibuilder

.. py:class:: CustomLlmsAPI

    The Custom LLMs service manages state and powers the UI for the Custom LLM product.

    .. py:method:: cancel(id: str)

        Cancel a Custom LLM Optimization Run.

        :param id: str


        

    .. py:method:: create(id: str) -> CustomLlm

        Start a Custom LLM Optimization Run.

        :param id: str
          The Id of the tile.

        :returns: :class:`CustomLlm`
        

    .. py:method:: get(id: str) -> CustomLlm

        Get a Custom LLM.

        :param id: str
          The id of the custom llm

        :returns: :class:`CustomLlm`
        

    .. py:method:: update(id: str, custom_llm: CustomLlm, update_mask: str) -> CustomLlm

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
        