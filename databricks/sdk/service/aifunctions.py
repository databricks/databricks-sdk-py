# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.
# ruff: noqa: F811, F841
# F401 is intentionally NOT covered: `make fmt` uses `ruff check --fix-only`
# to strip the fat-import header below; ignoring F401 would defeat that.

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any, Optional


import logging

from databricks.sdk.service._internal import (
    _from_dict,
    _int64,
    _repeated_dict,
    _repeated_int64,
)


_LOG = logging.getLogger("databricks.sdk")


# all definitions in this file are in alphabetical order


@dataclass
class AiClassifyOptions:
    """ai_classify"""

    enable_confidence_scores: Optional[bool] = None
    """When true, includes a per-label confidence score in the response."""

    enable_rationales: Optional[bool] = None
    """When true, includes a rationale explaining each classification in the response."""

    instructions: Optional[str] = None
    """Natural-language guidance that steers how the text is classified (up to 20,000 characters)."""

    multilabel: Optional[bool] = None
    """When true, allows more than one label to be returned per input."""

    version: Optional[str] = None
    """The function version to invoke. Defaults to the latest version. Supported versions: ["2.1"]."""

    def as_dict(self) -> dict:
        """Serializes the AiClassifyOptions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_confidence_scores is not None:
            body["enable_confidence_scores"] = self.enable_confidence_scores
        if self.enable_rationales is not None:
            body["enable_rationales"] = self.enable_rationales
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.multilabel is not None:
            body["multilabel"] = self.multilabel
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiClassifyOptions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_confidence_scores is not None:
            body["enable_confidence_scores"] = self.enable_confidence_scores
        if self.enable_rationales is not None:
            body["enable_rationales"] = self.enable_rationales
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.multilabel is not None:
            body["multilabel"] = self.multilabel
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiClassifyOptions:
        """Deserializes the AiClassifyOptions from a dictionary."""
        return cls(
            enable_confidence_scores=d.get("enable_confidence_scores", None),
            enable_rationales=d.get("enable_rationales", None),
            instructions=d.get("instructions", None),
            multilabel=d.get("multilabel", None),
            version=d.get("version", None),
        )


@dataclass
class AiClassifyResponse:
    metadata: Optional[AiClassifyResponseMetadata] = None
    """Additional metadata returned by AI Classify."""

    response: Optional[any] = None
    """The function result as a JSON value. An array of per-label objects: one element in single-label
    mode (the default), or multiple elements when ``multilabel`` is true. When
    ``enable_confidence_scores`` and ``enable_rationales`` are true, ``confidence_score`` and
    ``rationale`` are included in each response value, respectively."""

    def as_dict(self) -> dict:
        """Serializes the AiClassifyResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metadata:
            body["metadata"] = self.metadata.as_dict()
        if self.response:
            body["response"] = self.response
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiClassifyResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.metadata:
            body["metadata"] = self.metadata
        if self.response:
            body["response"] = self.response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiClassifyResponse:
        """Deserializes the AiClassifyResponse from a dictionary."""
        return cls(metadata=_from_dict(d, "metadata", AiClassifyResponseMetadata), response=d.get("response", None))


@dataclass
class AiClassifyResponseMetadata:
    version: Optional[str] = None
    """The resolved function version."""

    def as_dict(self) -> dict:
        """Serializes the AiClassifyResponseMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiClassifyResponseMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiClassifyResponseMetadata:
        """Deserializes the AiClassifyResponseMetadata from a dictionary."""
        return cls(version=d.get("version", None))


@dataclass
class AiExtractBbox:
    """A bounding box on a source page; used by bbox-input citations."""

    coord: Optional[List[int]] = None
    """Pixel coordinates on the page image as [x0, y0, x1, y1]."""

    page_id: Optional[int] = None
    """0-based page index the box is on."""

    def as_dict(self) -> dict:
        """Serializes the AiExtractBbox into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.coord:
            body["coord"] = [v for v in self.coord]
        if self.page_id is not None:
            body["page_id"] = self.page_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiExtractBbox into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.coord:
            body["coord"] = self.coord
        if self.page_id is not None:
            body["page_id"] = self.page_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiExtractBbox:
        """Deserializes the AiExtractBbox from a dictionary."""
        return cls(coord=_repeated_int64(d, "coord"), page_id=_int64(d, "page_id"))


@dataclass
class AiExtractCitation:
    """A citation locating an extracted value in the source. start/stop are set for span (STRING input)
    citations, bbox for bbox (parsed-document input) citations."""

    bbox: Optional[List[AiExtractBbox]] = None
    """Bounding boxes locating the citation on the source pages; set for bbox citations."""

    id: Optional[int] = None
    """Integer matching a citation_ids entry on an extracted field."""

    start: Optional[int] = None
    """Inclusive 0-based character offset into the input string; set for span citations."""

    stop: Optional[int] = None
    """Exclusive 0-based character offset into the input string; set for span citations."""

    def as_dict(self) -> dict:
        """Serializes the AiExtractCitation into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.bbox:
            body["bbox"] = [v.as_dict() for v in self.bbox]
        if self.id is not None:
            body["id"] = self.id
        if self.start is not None:
            body["start"] = self.start
        if self.stop is not None:
            body["stop"] = self.stop
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiExtractCitation into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.bbox:
            body["bbox"] = self.bbox
        if self.id is not None:
            body["id"] = self.id
        if self.start is not None:
            body["start"] = self.start
        if self.stop is not None:
            body["stop"] = self.stop
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiExtractCitation:
        """Deserializes the AiExtractCitation from a dictionary."""
        return cls(
            bbox=_repeated_dict(d, "bbox", AiExtractBbox),
            id=_int64(d, "id"),
            start=_int64(d, "start"),
            stop=_int64(d, "stop"),
        )


@dataclass
class AiExtractOptions:
    """ai_extract"""

    enable_citations: Optional[bool] = None
    """When true, includes citation metadata locating each extracted value in the source. Depending on
    the type of input, citations can be one of two types:
    
    For raw text (STRING) inputs, a citation is a span of text in the original input. Each object in
    ``metadata.citations`` has an ``id`` (integer matching a ``citation_ids`` entry on a field), a
    ``start`` (inclusive 0-based character offset into the input string), and a ``stop`` (exclusive
    0-based character offset into the input string).
    
    For PDF documents and images (when using ai_extract downstream of ai_parse_document), a citation
    is a bounding box in the original input. Each object in ``metadata.citations`` has an ``id``
    (integer matching a ``citation_ids`` entry on a field) and a ``bbox`` (array of {coord, page_id}
    objects, identical in shape to element.bbox in ai_parse_document output; coord is pixel
    coordinates on the page image as [x0, y0, x1, y1], and page_id is a 0-based page index)."""

    enable_confidence_scores: Optional[bool] = None
    """When true, includes a per-field confidence score in the response."""

    instructions: Optional[str] = None
    """Natural-language guidance that steers how data is extracted (up to 20,000 characters)."""

    mode: Optional[str] = None
    """Extraction mode. Supported modes: "precision" — more powerful extraction for complex schemas,
    long documents, and reasoning-heavy extractions. Defaults to none (standard extraction)."""

    version: Optional[str] = None
    """The function version to invoke. Defaults to the latest version. Supported versions: ["2.1"]."""

    def as_dict(self) -> dict:
        """Serializes the AiExtractOptions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.enable_citations is not None:
            body["enable_citations"] = self.enable_citations
        if self.enable_confidence_scores is not None:
            body["enable_confidence_scores"] = self.enable_confidence_scores
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.mode is not None:
            body["mode"] = self.mode
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiExtractOptions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.enable_citations is not None:
            body["enable_citations"] = self.enable_citations
        if self.enable_confidence_scores is not None:
            body["enable_confidence_scores"] = self.enable_confidence_scores
        if self.instructions is not None:
            body["instructions"] = self.instructions
        if self.mode is not None:
            body["mode"] = self.mode
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiExtractOptions:
        """Deserializes the AiExtractOptions from a dictionary."""
        return cls(
            enable_citations=d.get("enable_citations", None),
            enable_confidence_scores=d.get("enable_confidence_scores", None),
            instructions=d.get("instructions", None),
            mode=d.get("mode", None),
            version=d.get("version", None),
        )


@dataclass
class AiExtractResponse:
    metadata: Optional[AiExtractResponseMetadata] = None
    """Additional metadata returned by AI Extract."""

    response: Optional[any] = None
    """The function result as a JSON value. When ``enable_confidence_scores`` and ``enable_citations``
    are true, ``confidence`` and ``citation_ids`` are included in each response field, respectively."""

    def as_dict(self) -> dict:
        """Serializes the AiExtractResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.metadata:
            body["metadata"] = self.metadata.as_dict()
        if self.response:
            body["response"] = self.response
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiExtractResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.metadata:
            body["metadata"] = self.metadata
        if self.response:
            body["response"] = self.response
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiExtractResponse:
        """Deserializes the AiExtractResponse from a dictionary."""
        return cls(metadata=_from_dict(d, "metadata", AiExtractResponseMetadata), response=d.get("response", None))


@dataclass
class AiExtractResponseMetadata:
    chunk_type: Optional[str] = None
    """How the source was chunked for citation offsets (span for text input, bbox for parsed-document
    input); present when citations are enabled."""

    citations: Optional[List[AiExtractCitation]] = None
    """Citation objects locating each result in the source; present when citations are enabled."""

    mode: Optional[str] = None
    """The resolved extraction mode; present when a non-default mode was used."""

    version: Optional[str] = None
    """The resolved function version."""

    def as_dict(self) -> dict:
        """Serializes the AiExtractResponseMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.chunk_type is not None:
            body["chunk_type"] = self.chunk_type
        if self.citations:
            body["citations"] = [v.as_dict() for v in self.citations]
        if self.mode is not None:
            body["mode"] = self.mode
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiExtractResponseMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.chunk_type is not None:
            body["chunk_type"] = self.chunk_type
        if self.citations:
            body["citations"] = self.citations
        if self.mode is not None:
            body["mode"] = self.mode
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiExtractResponseMetadata:
        """Deserializes the AiExtractResponseMetadata from a dictionary."""
        return cls(
            chunk_type=d.get("chunk_type", None),
            citations=_repeated_dict(d, "citations", AiExtractCitation),
            mode=d.get("mode", None),
            version=d.get("version", None),
        )


@dataclass
class AiParseDocumentFileMetadata:
    """Metadata about the source file; present only for file-path input."""

    file_modification_time: Optional[str] = None
    """Last-modified timestamp of the source file, as an HTTP date string."""

    file_name: Optional[str] = None
    """Base name of the source file."""

    file_path: Optional[str] = None
    """Unity Catalog volume path of the source file."""

    file_size: Optional[int] = None
    """Size of the source file in bytes."""

    def as_dict(self) -> dict:
        """Serializes the AiParseDocumentFileMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.file_modification_time is not None:
            body["file_modification_time"] = self.file_modification_time
        if self.file_name is not None:
            body["file_name"] = self.file_name
        if self.file_path is not None:
            body["file_path"] = self.file_path
        if self.file_size is not None:
            body["file_size"] = self.file_size
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiParseDocumentFileMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.file_modification_time is not None:
            body["file_modification_time"] = self.file_modification_time
        if self.file_name is not None:
            body["file_name"] = self.file_name
        if self.file_path is not None:
            body["file_path"] = self.file_path
        if self.file_size is not None:
            body["file_size"] = self.file_size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiParseDocumentFileMetadata:
        """Deserializes the AiParseDocumentFileMetadata from a dictionary."""
        return cls(
            file_modification_time=d.get("file_modification_time", None),
            file_name=d.get("file_name", None),
            file_path=d.get("file_path", None),
            file_size=_int64(d, "file_size"),
        )


@dataclass
class AiParseDocumentOptions:
    """ai_parse_document"""

    description_element_types: Optional[str] = None
    """Element types for which an AI-generated description is produced. Use "*" (default) to generate
    descriptions for all supported element types, "figure" to generate them for figures only, or ""
    (empty string) to generate none. Only figure descriptions are supported for version "2.0", so
    "*" and "figure" produce the same behavior."""

    image_output_path: Optional[str] = None
    """Unity Catalog volume path where rendered page and element images are written."""

    page_range: Optional[str] = None
    """Pages to parse (1-indexed), as a comma-separated list of page numbers or ranges (e.g.
    "1,3,5-10")."""

    version: Optional[str] = None
    """The ai_parse_document output schema version. Supported value: "2.0"."""

    def as_dict(self) -> dict:
        """Serializes the AiParseDocumentOptions into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.description_element_types is not None:
            body["description_element_types"] = self.description_element_types
        if self.image_output_path is not None:
            body["image_output_path"] = self.image_output_path
        if self.page_range is not None:
            body["page_range"] = self.page_range
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiParseDocumentOptions into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.description_element_types is not None:
            body["description_element_types"] = self.description_element_types
        if self.image_output_path is not None:
            body["image_output_path"] = self.image_output_path
        if self.page_range is not None:
            body["page_range"] = self.page_range
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiParseDocumentOptions:
        """Deserializes the AiParseDocumentOptions from a dictionary."""
        return cls(
            description_element_types=d.get("description_element_types", None),
            image_output_path=d.get("image_output_path", None),
            page_range=d.get("page_range", None),
            version=d.get("version", None),
        )


@dataclass
class AiParseDocumentPageError:
    """A single page that failed to parse while the overall request succeeded."""

    error_message: Optional[str] = None
    """Message describing why the page failed."""

    page_id: Optional[int] = None
    """0-based index of the page that failed."""

    def as_dict(self) -> dict:
        """Serializes the AiParseDocumentPageError into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.page_id is not None:
            body["page_id"] = self.page_id
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiParseDocumentPageError into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.error_message is not None:
            body["error_message"] = self.error_message
        if self.page_id is not None:
            body["page_id"] = self.page_id
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiParseDocumentPageError:
        """Deserializes the AiParseDocumentPageError from a dictionary."""
        return cls(error_message=d.get("error_message", None), page_id=_int64(d, "page_id"))


@dataclass
class AiParseDocumentResponse:
    document: Optional[any] = None
    """The parsed document as a JSON value, containing the extracted pages and elements."""

    error_status: Optional[List[AiParseDocumentPageError]] = None
    """Per-page partial-failure details; present when the request succeeds (2xx) but individual pages
    fail."""

    metadata: Optional[AiParseDocumentResponseMetadata] = None
    """Additional metadata returned by AI Parse Document."""

    def as_dict(self) -> dict:
        """Serializes the AiParseDocumentResponse into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.document:
            body["document"] = self.document
        if self.error_status:
            body["error_status"] = [v.as_dict() for v in self.error_status]
        if self.metadata:
            body["metadata"] = self.metadata.as_dict()
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiParseDocumentResponse into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.document:
            body["document"] = self.document
        if self.error_status:
            body["error_status"] = self.error_status
        if self.metadata:
            body["metadata"] = self.metadata
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiParseDocumentResponse:
        """Deserializes the AiParseDocumentResponse from a dictionary."""
        return cls(
            document=d.get("document", None),
            error_status=_repeated_dict(d, "error_status", AiParseDocumentPageError),
            metadata=_from_dict(d, "metadata", AiParseDocumentResponseMetadata),
        )


@dataclass
class AiParseDocumentResponseMetadata:
    file_metadata: Optional[AiParseDocumentFileMetadata] = None
    """Describes the source file; present only for file-path input."""

    id: Optional[str] = None
    """Unique identifier for the parse request."""

    version: Optional[str] = None
    """The resolved function version."""

    def as_dict(self) -> dict:
        """Serializes the AiParseDocumentResponseMetadata into a dictionary suitable for use as a JSON request body."""
        body = {}
        if self.file_metadata:
            body["file_metadata"] = self.file_metadata.as_dict()
        if self.id is not None:
            body["id"] = self.id
        if self.version is not None:
            body["version"] = self.version
        return body

    def as_shallow_dict(self) -> dict:
        """Serializes the AiParseDocumentResponseMetadata into a shallow dictionary of its immediate attributes."""
        body = {}
        if self.file_metadata:
            body["file_metadata"] = self.file_metadata
        if self.id is not None:
            body["id"] = self.id
        if self.version is not None:
            body["version"] = self.version
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> AiParseDocumentResponseMetadata:
        """Deserializes the AiParseDocumentResponseMetadata from a dictionary."""
        return cls(
            file_metadata=_from_dict(d, "file_metadata", AiParseDocumentFileMetadata),
            id=d.get("id", None),
            version=d.get("version", None),
        )


class AiFunctionsAPI:
    """Transform and enrich data with AI on Databricks."""

    def __init__(self, api_client):
        self._api = api_client

    def ai_classify(
        self, content: any, labels: any, *, options: Optional[AiClassifyOptions] = None
    ) -> AiClassifyResponse:
        """Classifies content according to a set of provided labels.

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
        """

        body = {}
        if content is not None:
            body["content"] = content
        if labels is not None:
            body["labels"] = labels
        if options is not None:
            body["options"] = options.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/ai-functions/ai-classify", body=body, headers=headers)
        return AiClassifyResponse.from_dict(res)

    def ai_extract(self, content: any, schema: any, *, options: Optional[AiExtractOptions] = None) -> AiExtractResponse:
        """Extracts structured data from text and documents according to a provided schema.

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
        """

        body = {}
        if content is not None:
            body["content"] = content
        if options is not None:
            body["options"] = options.as_dict()
        if schema is not None:
            body["schema"] = schema
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/ai-functions/ai-extract", body=body, headers=headers)
        return AiExtractResponse.from_dict(res)

    def ai_parse_document(
        self, content: str, *, options: Optional[AiParseDocumentOptions] = None
    ) -> AiParseDocumentResponse:
        """Parse structured content from unstructured documents.

        :param content: str
          The document to parse, given as a Unity Catalog volume path to the source file (the REST API accepts
          only a UC volume path, not inline binary data). Supported formats: PDF, DOCX, DOC, PPTX, PPT, JPG,
          JPEG, PNG, TIFF. Accepts up to 100 pages and 100 MB per document.
        :param options: :class:`AiParseDocumentOptions` (optional)
          Function options. Omitted fields fall back to their documented defaults.

        :returns: :class:`AiParseDocumentResponse`
        """

        body = {}
        if content is not None:
            body["content"] = content
        if options is not None:
            body["options"] = options.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        cfg = self._api._cfg
        if cfg.workspace_id:
            headers["X-Databricks-Workspace-Id"] = cfg.workspace_id

        res = self._api.do("POST", "/api/2.0/ai-functions/ai-parse-document", body=body, headers=headers)
        return AiParseDocumentResponse.from_dict(res)
