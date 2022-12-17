# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class Delete:

    # The absolute path of the notebook or directory.
    path: str
    # The flag that specifies whether to delete the object recursively. It is
    # `false` by default. Please note this deleting directory is not atomic. If
    # it fails in the middle, some of objects under this directory may be
    # deleted and cannot be undone.
    recursive: bool

    def as_dict(self) -> dict:
        body = {}
        if self.path:
            body["path"] = self.path
        if self.recursive:
            body["recursive"] = self.recursive

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            path=d.get("path", None),
            recursive=d.get("recursive", None),
        )


@dataclass
class Export:
    """Export a notebook"""

    # Flag to enable direct download. If it is `true`, the response will be the
    # exported file itself. Otherwise, the response contains content as base64
    # encoded string.
    direct_download: bool  # query
    # This specifies the format of the exported file. By default, this is
    # `SOURCE`. However it may be one of: `SOURCE`, `HTML`, `JUPYTER`, `DBC`.
    #
    # The value is case sensitive.
    format: "ExportFormat"  # query
    # The absolute path of the notebook or directory. Exporting directory is
    # only support for `DBC` format.
    path: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.direct_download:
            body["direct_download"] = self.direct_download
        if self.format:
            body["format"] = self.format.value
        if self.path:
            body["path"] = self.path

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Export":
        return cls(
            direct_download=d.get("direct_download", None),
            format=ExportFormat(d["format"]) if "format" in d else None,
            path=d.get("path", None),
        )


class ExportFormat(Enum):
    """This specifies the format of the file to be imported. By default, this is
    `SOURCE`. However it may be one of: `SOURCE`, `HTML`, `JUPYTER`, `DBC`. The
    value is case sensitive."""

    DBC = "DBC"
    HTML = "HTML"
    JUPYTER = "JUPYTER"
    R_MARKDOWN = "R_MARKDOWN"
    SOURCE = "SOURCE"


@dataclass
class ExportResponse:

    # The base64-encoded content. If the limit (10MB) is exceeded, exception
    # with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** will be thrown.
    content: str

    def as_dict(self) -> dict:
        body = {}
        if self.content:
            body["content"] = self.content

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ExportResponse":
        return cls(
            content=d.get("content", None),
        )


@dataclass
class GetStatus:
    """Get status"""

    # The absolute path of the notebook or directory.
    path: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.path:
            body["path"] = self.path

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetStatus":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class Import:

    # The base64-encoded content. This has a limit of 10 MB.
    #
    # If the limit (10MB) is exceeded, exception with error code
    # **MAX_NOTEBOOK_SIZE_EXCEEDED** will be thrown. This parameter might be
    # absent, and instead a posted file will be used.
    content: str
    # This specifies the format of the file to be imported. By default, this is
    # `SOURCE`. However it may be one of: `SOURCE`, `HTML`, `JUPYTER`, `DBC`.
    # The value is case sensitive.
    format: "ExportFormat"
    # The language of the object. This value is set only if the object type is
    # `NOTEBOOK`.
    language: "Language"
    # The flag that specifies whether to overwrite existing object. It is
    # `false` by default. For `DBC` format, `overwrite` is not supported since
    # it may contain a directory.
    overwrite: bool
    # The absolute path of the notebook or directory. Importing directory is
    # only support for `DBC` format.
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.content:
            body["content"] = self.content
        if self.format:
            body["format"] = self.format.value
        if self.language:
            body["language"] = self.language.value
        if self.overwrite:
            body["overwrite"] = self.overwrite
        if self.path:
            body["path"] = self.path

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Import":
        return cls(
            content=d.get("content", None),
            format=ExportFormat(d["format"]) if "format" in d else None,
            language=Language(d["language"]) if "language" in d else None,
            overwrite=d.get("overwrite", None),
            path=d.get("path", None),
        )


class Language(Enum):
    """The language of the object. This value is set only if the object type is
    `NOTEBOOK`."""

    PYTHON = "PYTHON"
    R = "R"
    SCALA = "SCALA"
    SQL = "SQL"


@dataclass
class List:
    """List contents"""

    # <content needed>
    notebooks_modified_after: int  # query
    # The absolute path of the notebook or directory.
    path: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.notebooks_modified_after:
            body["notebooks_modified_after"] = self.notebooks_modified_after
        if self.path:
            body["path"] = self.path

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "List":
        return cls(
            notebooks_modified_after=d.get("notebooks_modified_after", None),
            path=d.get("path", None),
        )


@dataclass
class ListResponse:

    # List of objects.
    objects: "List[ObjectInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.objects:
            body["objects"] = [v.as_dict() for v in self.objects]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListResponse":
        return cls(
            objects=[ObjectInfo.from_dict(v) for v in d["objects"]]
            if "objects" in d
            else None,
        )


@dataclass
class Mkdirs:

    # The absolute path of the directory. If the parent directories do not
    # exist, it will also create them. If the directory already exists, this
    # command will do nothing and succeed.
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path:
            body["path"] = self.path

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Mkdirs":
        return cls(
            path=d.get("path", None),
        )


@dataclass
class ObjectInfo:

    # <content needed>
    created_at: int
    # The language of the object. This value is set only if the object type is
    # `NOTEBOOK`.
    language: "Language"
    # <content needed>
    modified_at: int
    # <content needed>
    object_id: int
    # The type of the object in workspace.
    object_type: "ObjectType"
    # The absolute path of the object.
    path: str
    # <content needed>
    size: int

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.language:
            body["language"] = self.language.value
        if self.modified_at:
            body["modified_at"] = self.modified_at
        if self.object_id:
            body["object_id"] = self.object_id
        if self.object_type:
            body["object_type"] = self.object_type.value
        if self.path:
            body["path"] = self.path
        if self.size:
            body["size"] = self.size

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ObjectInfo":
        return cls(
            created_at=d.get("created_at", None),
            language=Language(d["language"]) if "language" in d else None,
            modified_at=d.get("modified_at", None),
            object_id=d.get("object_id", None),
            object_type=ObjectType(d["object_type"]) if "object_type" in d else None,
            path=d.get("path", None),
            size=d.get("size", None),
        )


class ObjectType(Enum):
    """The type of the object in workspace."""

    DIRECTORY = "DIRECTORY"
    FILE = "FILE"
    LIBRARY = "LIBRARY"
    NOTEBOOK = "NOTEBOOK"
    REPO = "REPO"


class WorkspaceAPI:
    def __init__(self, api_client):
        self._api = api_client

    def delete(self, path: str, *, recursive: bool = None, **kwargs):
        """Delete a workspace object.

        Deletes an object or a directory (and optionally recursively deletes all
        objects in the directory). * If `path` does not exist, this call returns
        an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a non-empty directory
        and `recursive` is set to `false`, this call returns an error
        `DIRECTORY_NOT_EMPTY`.

        Object deletion cannot be undone and deleting a directory recursively is
        not atomic."""

        request = kwargs.get("request", None)
        if not request:
            request = Delete(path=path, recursive=recursive)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/workspace/delete", query=query, body=body)

    def export(
        self,
        path: str,
        *,
        direct_download: bool = None,
        format: ExportFormat = None,
        **kwargs
    ) -> ExportResponse:
        """Export a notebook.

        Exports a notebook or the contents of an entire directory.

        If `path` does not exist, this call returns an error
        `RESOURCE_DOES_NOT_EXIST`.

        One can only export a directory in `DBC` format. If the exported data
        would exceed size limit, this call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`.
        Currently, this API does not support exporting a library."""

        request = kwargs.get("request", None)
        if not request:
            request = Export(direct_download=direct_download, format=format, path=path)
        body = request.as_dict()
        query = {}
        if direct_download:
            query["direct_download"] = direct_download
        if format:
            query["format"] = format.value
        if path:
            query["path"] = path

        json = self._api.do("GET", "/api/2.0/workspace/export", query=query, body=body)
        return ExportResponse.from_dict(json)

    def get_status(self, path: str, **kwargs) -> ObjectInfo:
        """Get status.

        Gets the status of an object or a directory. If `path` does not exist,
        this call returns an error `RESOURCE_DOES_NOT_EXIST`."""

        request = kwargs.get("request", None)
        if not request:
            request = GetStatus(path=path)
        body = request.as_dict()
        query = {}
        if path:
            query["path"] = path

        json = self._api.do(
            "GET", "/api/2.0/workspace/get-status", query=query, body=body
        )
        return ObjectInfo.from_dict(json)

    def import_(
        self,
        path: str,
        *,
        content: str = None,
        format: ExportFormat = None,
        language: Language = None,
        overwrite: bool = None,
        **kwargs
    ):
        """Import a notebook.

        Imports a notebook or the contents of an entire directory. If `path`
        already exists and `overwrite` is set to `false`, this call returns an
        error `RESOURCE_ALREADY_EXISTS`. One can only use `DBC` format to import
        a directory."""

        request = kwargs.get("request", None)
        if not request:
            request = Import(
                content=content,
                format=format,
                language=language,
                overwrite=overwrite,
                path=path,
            )
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/workspace/import", query=query, body=body)

    def list(
        self, path: str, *, notebooks_modified_after: int = None, **kwargs
    ) -> ListResponse:
        """List contents.

        Lists the contents of a directory, or the object if it is not a
        directory.If the input path does not exist, this call returns an error
        `RESOURCE_DOES_NOT_EXIST`."""

        request = kwargs.get("request", None)
        if not request:
            request = List(notebooks_modified_after=notebooks_modified_after, path=path)
        body = request.as_dict()
        query = {}
        if notebooks_modified_after:
            query["notebooks_modified_after"] = notebooks_modified_after
        if path:
            query["path"] = path

        json = self._api.do("GET", "/api/2.0/workspace/list", query=query, body=body)
        return ListResponse.from_dict(json)

    def mkdirs(self, path: str, **kwargs):
        """Create a directory.

        Creates the specified directory (and necessary parent directories if
        they do not exist). If there is an object (not a directory) at any
        prefix of the input path, this call returns an error
        `RESOURCE_ALREADY_EXISTS`.

        Note that if this operation fails it may have succeeded in creating some
        of the necessary\nparrent directories."""

        request = kwargs.get("request", None)
        if not request:
            request = Mkdirs(path=path)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/workspace/mkdirs", query=query, body=body)
