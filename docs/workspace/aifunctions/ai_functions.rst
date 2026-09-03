``w.ai_functions``: AiFunctions.v1
==================================
.. currentmodule:: databricks.sdk.service.aifunctions

.. py:class:: AiFunctionsAPI

    Transform and enrich data with AI on Databricks.

    .. py:method:: ai_classify(content: any, labels: any [, options: Optional[AiClassifyOptions]]) -> AiClassifyResponse

        Classifies content according to a set of provided labels.

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
        

    .. py:method:: ai_extract(content: any, schema: any [, options: Optional[AiExtractOptions]]) -> AiExtractResponse

        Extracts structured data from text and documents according to a provided schema.

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
        