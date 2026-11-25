``w.ai_functions``: AiFunctions.v1
==================================
.. currentmodule:: databricks.sdk.service.aifunctions

.. py:class:: AiFunctionsAPI

    Transform and enrich data with AI.

    .. py:method:: ai_classify(content: any, labels: any [, options: Optional[AiClassifyOptions]]) -> AiClassifyResponse

        Classifies content according to a set of provided labels. The AI Classify REST API has a default rate
        limit of 1,200 requests per minute per workspace. Contact your account team to request a higher limit.

        :param content: any
          The content to classify. It accepts a plain string or the response object of
          [ai_parse_document](:method:AiFunctions/AiParseDocument).
        :param labels: any
          The label set to classify as. Either a JSON array of label strings (e.g. ["spam", "not_spam"]), or a
          JSON object mapping each label to a description (e.g. {"spam": "unsolicited bulk message",
          "not_spam": "a legitimate message"}). Accepts 2 to 5000 labels, each 1 to 100 characters. When
          multilabel is true, a single label is also accepted.
        :param options: :class:`AiClassifyOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiClassifyResponse`
        

    .. py:method:: ai_decide(state: any, questions: any [, options: Optional[AiDecideOptions]]) -> AiDecideResponse

        Turn text and structured data into decisions your application can use. Define questions and criteria
        to choose an option, estimate a probability, or assign a score given a provided state. The AI Decide
        REST API has a default rate limit of 1,200 requests per minute per workspace. Contact your account
        team to request a higher limit.

        .. note::

           **Note:** The v1 AI Decide syntax supporting strings and objects in ``state`` and objects and
           arrays in ``instructions`` will no longer be supported starting February 1, 2027. To use AI Decide,
           you must set ``options.version`` to ``"2.0"``, pass an array of typed content objects to ``state``,
           and a nonblank string to ``instructions``.

        :param state: any
          A nonempty array of typed content objects shared by all questions. Set ``options.version`` to
          ``"2.0"`` to use this format. Text and JSON content plus questions must fit within 32 KiB as compact
          UTF-8 JSON, excluding image parts.

          | type | Content field | Value | | --- | --- | --- | | ``text`` | ``text`` | A nonblank string. | |
          ``json`` | ``data`` | A JSON object or array. | | ``image`` | ``image_url`` | An inline base64 PNG
          or JPEG data URL: ``data:image/png;base64,<base64-encoded image bytes>`` or
          ``data:image/jpeg;base64,<base64-encoded image bytes>``. HTTP URLs and file paths are not supported.
          Each image must be at most 4 MiB after base64 decoding, with a resolution up to 1,568 × 1,568
          pixels (or an equivalent pixel count). A request supports up to five images. Images are only
          supported in `select regions
          <https://docs.databricks.com/aws/en/resources/feature-region-support#ai-function-availability>`__. |
        :param questions: any
          A JSON object mapping up to 256 question IDs to their definitions. Each ID must be nonblank; its
          answer is returned with the same ID in ``response.answers``.

          Each definition is an object with the required fields ``type`` and ``instructions``. The
          ``criteria`` field is optional for the type ``noul`` but is required for the types ``choice`` and
          ``score``.

          In AI Decide v2, ``instructions`` and each criteria description must be nonblank strings. Each
          question may contain at most 20,000 characters across its ID, instructions, and criteria.

          The ``type`` can be one of:

          - ``choice``: Selects one option from a defined set. Requires ``criteria`` to be an object mapping 1
            to 255 nonblank option names to nonblank string descriptions. For example:

          .. code-block:: json

             {
             "team": {
             "type": "choice",
             "instructions": "Which team should handle this ticket?",
             "criteria": {
             "billing": "Payments, charges, and refunds",
             "technical_support": "Product errors and troubleshooting"
             }
             }
             }

          - ``noul``: Estimates the probability that the answer to a true-or-false question is true.
            ``criteria`` can take the fields ``true`` or ``false``, or both, with nonblank string
            descriptions. Omit ``criteria`` to use the question alone. For example, both of the following are
            valid:

          .. code-block:: json

             {
             "escalate": {
             "type": "noul",
             "instructions": "Does this ticket need escalation?",
             "criteria": {
             "true": "Suspected fraud or an exception to standard policy",
             "false": "A routine issue frontline support can resolve"
             }
             }
             }

          or

          .. code-block:: json

             {
             "escalate": {
             "type": "noul",
             "instructions": "Does this ticket need escalation?"
             }
             }

          - ``score``: Rates the state on an ordered scale. Requires ``criteria`` to be an array of 2 to 10
            unique, nonblank string descriptions, ordered from low to high. Array positions define levels
            starting at 0. For example:

          .. code-block:: json

             {
             "urgency": {
             "type": "score",
             "instructions": "How urgent is this ticket?",
             "criteria": [
             "Routine: can wait a few days",
             "Time-sensitive: needs attention today",
             "Critical: needs immediate action"
             ]
             }
             }
        :param options: :class:`AiDecideOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiDecideResponse`
        

    .. py:method:: ai_extract(content: any, schema: any [, options: Optional[AiExtractOptions]]) -> AiExtractResponse

        Extracts structured data from text and documents according to a provided schema. The AI Extract REST
        API has a default rate limit of 120 requests per minute per workspace. Contact your account team to
        request a higher limit.

        :param content: any
          The text to extract from. It accepts a plain string or the response object of
          [ai_parse_document](:method:AiFunctions/AiParseDocument).
        :param schema: any
          The extraction schema defining the fields to extract. Either a JSON array of field names, assumed to
          be strings (e.g. ["company", "valuation"]), or a JSON object mapping each field to its
          type/description (e.g. {"company": {"type": "string", "description": "the company name"}}). Enum
          fields list their values in "labels" (e.g. {"currency": {"type": "enum", "labels": ["USD",
          "EUR"]}}). Primitive and enum fields are nullable by default. Accepts up to 256 fields, 12 levels of
          nesting, and 500 enum values. Supported field types are string, integer, number, boolean, and enum.
        :param options: :class:`AiExtractOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiExtractResponse`
        

    .. py:method:: ai_parse_document(content: str [, options: Optional[AiParseDocumentOptions]]) -> AiParseDocumentResponse

        Parse structured content from unstructured documents.

        :param content: str
          The document to parse. The REST API accepts a Unity Catalog volume path to the source file or a
          base64 data URL containing the file bytes (for example,
          data:application/pdf;base64,<encoded-file-bytes> or data:image/jpeg;base64,<encoded-file-bytes>).
          Supported formats: PDF, DOCX, DOC, PPTX, PPT, JPG, JPEG, PNG, TIFF. Accepts up to 100 pages and 100
          MB per document.
        :param options: :class:`AiParseDocumentOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiParseDocumentResponse`
        

    .. py:method:: cancel_batch(name: str) -> CancelBatchResponse

        Starts the asynchronous cancellation of a batch. Requests in progress are stopped, and the results of
        the requests that finished are kept. Cancellation is best effort, so the batch can still complete.

        :param name: str
          Unique identifier of the batch. Format: ``batch_<id>``.

        :returns: :class:`CancelBatchResponse`
        

    .. py:method:: create_batch(batch: Batch) -> Batch

        Creates a batch that runs an AI function on every request in a JSONL file on a Unity Catalog volume.
        The batch runs asynchronously. To follow its progress, get the batch.

        :param batch: :class:`Batch`
          The batch to create.

        :returns: :class:`Batch`
        

    .. py:method:: get_batch(name: str) -> Batch

        Gets the latest status and progress of a batch.

        :param name: str
          Unique identifier of the batch. Format: ``batch_<id>``.

        :returns: :class:`Batch`
        

    .. py:method:: list_batches( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[Batch]

        Lists the batches that the caller created in this workspace.

        :param page_size: int (optional)
          Maximum number of batches to return in one page.
        :param page_token: str (optional)
          A page token from a previous call to list batches. Omit it to get the first page.

        :returns: Iterator over :class:`Batch`
        