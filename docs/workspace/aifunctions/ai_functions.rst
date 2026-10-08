``w.ai_functions``: AiFunctions.v1
==================================
.. currentmodule:: databricks.sdk.service.aifunctions

.. py:class:: AiFunctionsAPI

    Transform and enrich data with AI on Databricks.

    .. py:method:: ai_classify(content: any, labels: any [, options: Optional[AiClassifyOptions]]) -> AiClassifyResponse

        Classifies content according to a set of provided labels. For REST API requests, the default rate
        limit is 1,200 requests per minute per workspace. Contact your Databricks account team to request a
        higher limit.

        :param content: any
          The content to classify. It accepts a plain string or the response object of
          [ai_parse_document](:method:AiFunctions/AiParseDocument).
        :param labels: any
          The label set to classify as. Either a JSON array of label strings (e.g. ["spam", "not_spam"]), or a
          JSON object mapping each label to a description (e.g. {"spam": "unsolicited bulk message",
          "not_spam": "a legitimate message"}). Accepts 2 to 500 labels, each 1 to 100 characters.
        :param options: :class:`AiClassifyOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiClassifyResponse`
        

    .. py:method:: ai_decide(state: any, questions: any [, options: Optional[AiDecideOptions]]) -> AiDecideResponse

        Turn text and structured data into decisions your application can use. Define questions and criteria
        to choose an option, estimate a probability, or assign a score given a provided state.

        :param state: any
          A string, JSON object, or array containing the content, related context, and examples needed to
          answer the provided questions. For example, provide a support message, a conversation, or records
          describing the current state of an application. All questions receive this same state.
        :param questions: any
          A JSON object mapping question IDs to their definitions. Each ID must contain non-whitespace text;
          its answer is returned with the same ID in ``response.answers``.

          Each definition is an object with the required fields ``type`` and ``instructions``. The
          ``criteria`` field is optional for the type ``noul`` but is required for the types ``choice`` and
          ``score``.

          The ``instructions`` field describes the judgment to make and can be a string, object, or array. Use
          an object or array to include supporting context alongside the instructions.

          The ``type`` can be one of:

          - ``choice``: Selects one option from a defined set. Requires ``criteria`` to be an object mapping 1
            to 255 nonempty option names to descriptions. The criteria description can be a string, object,
            array, or null when the name needs no additional detail. For example:

          .. code-block:: json

             {
             "team": {
             "type": "choice",
             "instructions": "Which team should handle this ticket?",
             "criteria": {
             "billing": "Payments, charges, and refunds",
             "technical_support": null
             }
             }
             }

          - ``noul``: Estimates the probability that the answer to a true-or-false question is true.
            ``criteria`` can take the fields ``true`` or ``false``, or both, with descriptions that are
            strings, objects, or arrays. Omit ``criteria`` to use the question alone. The instructions or at
            least one criteria description must contain non-whitespace text, a nonempty object, or a nonempty
            array. For example, both of the following are valid:

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
            level descriptions, ordered from low to high. Descriptions must contain non-whitespace text, a
            nonempty object, or a nonempty array. Array positions define levels starting at 0. For example:

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

        Extracts structured data from text and documents according to a provided schema. For REST API
        requests, the default rate limit is 120 requests per minute per workspace. Contact your Databricks
        account team to request a higher limit.

        :param content: any
          The text to extract from. It accepts a plain string or the response object of
          [ai_parse_document](:method:AiFunctions/AiParseDocument).
        :param schema: any
          The extraction schema defining the fields to extract. Either a JSON array of field names, assumed to
          be strings (e.g. ["company", "valuation"]), or a JSON object mapping each field to its
          type/description/nullability (e.g. {"company": {"type": "string", "description": "the company
          name"}}). Accepts up to 256 fields, 12 levels of nesting, and 500 enum values. Supported field types
          are string, integer, number, boolean, and enum.
        :param options: :class:`AiExtractOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiExtractResponse`
        

    .. py:method:: ai_parse_document(content: str [, options: Optional[AiParseDocumentOptions]]) -> AiParseDocumentResponse

        Parse structured content from unstructured documents.

        :param content: str
          The document to parse, given as a Unity Catalog volume path to the source file (the REST API accepts
          only a UC volume path, not inline binary data). Supported formats: PDF, DOCX, DOC, PPTX, PPT, JPG,
          JPEG, PNG, TIFF. Accepts up to 100 pages and 100 MB per document.
        :param options: :class:`AiParseDocumentOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiParseDocumentResponse`
        