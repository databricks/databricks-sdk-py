# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List

from ._internal import _enum, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class Delete:
    path: str
    recursive: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        if self.recursive: body['recursive'] = self.recursive
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Delete':
        return cls(path=d.get('path', None), recursive=d.get('recursive', None))


@dataclass
class Export:
    """Export a notebook"""

    path: str
    direct_download: bool = None
    format: 'ExportFormat' = None


class ExportFormat(Enum):
    """This specifies the format of the file to be imported. By default, this is `SOURCE`. However it
    may be one of: `SOURCE`, `HTML`, `JUPYTER`, `DBC`. The value is case sensitive."""

    DBC = 'DBC'
    HTML = 'HTML'
    JUPYTER = 'JUPYTER'
    R_MARKDOWN = 'R_MARKDOWN'
    SOURCE = 'SOURCE'


@dataclass
class ExportResponse:
    content: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.content: body['content'] = self.content
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportResponse':
        return cls(content=d.get('content', None))


@dataclass
class GetStatus:
    """Get status"""

    path: str


@dataclass
class Import:
    path: str
    content: str = None
    format: 'ExportFormat' = None
    language: 'Language' = None
    overwrite: bool = None

    def as_dict(self) -> dict:
        body = {}
        if self.content: body['content'] = self.content
        if self.format: body['format'] = self.format.value
        if self.language: body['language'] = self.language.value
        if self.overwrite: body['overwrite'] = self.overwrite
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Import':
        return cls(content=d.get('content', None),
                   format=_enum(d, 'format', ExportFormat),
                   language=_enum(d, 'language', Language),
                   overwrite=d.get('overwrite', None),
                   path=d.get('path', None))


class Language(Enum):
    """The language of the object. This value is set only if the object type is `NOTEBOOK`."""

    PYTHON = 'PYTHON'
    R = 'R'
    SCALA = 'SCALA'
    SQL = 'SQL'


@dataclass
class ListRequest:
    """List contents"""

    path: str
    notebooks_modified_after: int = None


@dataclass
class ListResponse:
    objects: 'List[ObjectInfo]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.objects: body['objects'] = [v.as_dict() for v in self.objects]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(objects=_repeated(d, 'objects', ObjectInfo))


@dataclass
class Mkdirs:
    path: str

    def as_dict(self) -> dict:
        body = {}
        if self.path: body['path'] = self.path
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Mkdirs':
        return cls(path=d.get('path', None))


@dataclass
class ObjectInfo:
    created_at: int = None
    language: 'Language' = None
    modified_at: int = None
    object_id: int = None
    object_type: 'ObjectType' = None
    path: str = None
    size: int = None

    def as_dict(self) -> dict:
        body = {}
        if self.created_at: body['created_at'] = self.created_at
        if self.language: body['language'] = self.language.value
        if self.modified_at: body['modified_at'] = self.modified_at
        if self.object_id: body['object_id'] = self.object_id
        if self.object_type: body['object_type'] = self.object_type.value
        if self.path: body['path'] = self.path
        if self.size: body['size'] = self.size
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectInfo':
        return cls(created_at=d.get('created_at', None),
                   language=_enum(d, 'language', Language),
                   modified_at=d.get('modified_at', None),
                   object_id=d.get('object_id', None),
                   object_type=_enum(d, 'object_type', ObjectType),
                   path=d.get('path', None),
                   size=d.get('size', None))


class ObjectType(Enum):
    """The type of the object in workspace."""

    DIRECTORY = 'DIRECTORY'
    FILE = 'FILE'
    LIBRARY = 'LIBRARY'
    NOTEBOOK = 'NOTEBOOK'
    REPO = 'REPO'


class WorkspaceAPI:
    """The Workspace API allows you to list, import, export, and delete notebooks and folders.
    
    A notebook is a web-based interface to a document that contains runnable code, visualizations, and
    explanatory text."""

    def __init__(self, api_client):
        self._api = api_client

    def delete(self, path: str, *, recursive: bool = None, **kwargs):
        """Delete a workspace object.
        
        Deletes an object or a directory (and optionally recursively deletes all objects in the directory). *
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`. * If `path` is a
        non-empty directory and `recursive` is set to `false`, this call returns an error
        `DIRECTORY_NOT_EMPTY`.
        
        Object deletion cannot be undone and deleting a directory recursively is not atomic."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Delete(path=path, recursive=recursive)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/delete', body=body)

    def export(self,
               path: str,
               *,
               direct_download: bool = None,
               format: ExportFormat = None,
               **kwargs) -> ExportResponse:
        """Export a notebook.
        
        Exports a notebook or the contents of an entire directory.
        
        If `path` does not exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`.
        
        One can only export a directory in `DBC` format. If the exported data would exceed size limit, this
        call returns `MAX_NOTEBOOK_SIZE_EXCEEDED`. Currently, this API does not support exporting a library."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Export(direct_download=direct_download, format=format, path=path)

        query = {}
        if direct_download: query['direct_download'] = request.direct_download
        if format: query['format'] = request.format.value
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/export', query=query)
        return ExportResponse.from_dict(json)

    def get_status(self, path: str, **kwargs) -> ObjectInfo:
        """Get status.
        
        Gets the status of an object or a directory. If `path` does not exist, this call returns an error
        `RESOURCE_DOES_NOT_EXIST`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = GetStatus(path=path)

        query = {}
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/get-status', query=query)
        return ObjectInfo.from_dict(json)

    def import_(self,
                path: str,
                *,
                content: str = None,
                format: ExportFormat = None,
                language: Language = None,
                overwrite: bool = None,
                **kwargs):
        """Import a notebook.
        
        Imports a notebook or the contents of an entire directory. If `path` already exists and `overwrite` is
        set to `false`, this call returns an error `RESOURCE_ALREADY_EXISTS`. One can only use `DBC` format to
        import a directory."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Import(content=content,
                             format=format,
                             language=language,
                             overwrite=overwrite,
                             path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/import', body=body)

    def list(self, path: str, *, notebooks_modified_after: int = None, **kwargs) -> Iterator[ObjectInfo]:
        """List contents.
        
        Lists the contents of a directory, or the object if it is not a directory.If the input path does not
        exist, this call returns an error `RESOURCE_DOES_NOT_EXIST`."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ListRequest(notebooks_modified_after=notebooks_modified_after, path=path)

        query = {}
        if notebooks_modified_after: query['notebooks_modified_after'] = request.notebooks_modified_after
        if path: query['path'] = request.path

        json = self._api.do('GET', '/api/2.0/workspace/list', query=query)
        return [ObjectInfo.from_dict(v) for v in json.get('objects', [])]

    def mkdirs(self, path: str, **kwargs):
        """Create a directory.
        
        Creates the specified directory (and necessary parent directories if they do not exist). If there is
        an object (not a directory) at any prefix of the input path, this call returns an error
        `RESOURCE_ALREADY_EXISTS`.
        
        Note that if this operation fails it may have succeeded in creating some of the necessary parrent
        directories."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = Mkdirs(path=path)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/workspace/mkdirs', body=body)
