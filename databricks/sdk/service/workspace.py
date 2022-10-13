# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List

__all__ = [
    
    'Delete',
    'ExportResponse',
    'Import',
    'ImportFormat',
    'ImportLanguage',
    'ListResponse',
    'Mkdirs',
    'ObjectInfo',
    'ObjectInfoBlobLocation',
    'ObjectInfoLanguage',
    'ObjectInfoObjectType',
    'ExportRequest',
    'GetStatusRequest',
    'ListRequest',
    
    'Workspace',
]

# all definitions in this file are in alphabetical order

@dataclass
class Delete:
    
    # The absolute path of the notebook or directory.
    path: str
    # The flag that specifies whether to delete the object recursively. It is
    # ``false`` by default. Please note this deleting directory is not atomic.
    # If it fails in the middle, some of objects under this directory may be
    # deleted and cannot be undone.
    recursive: bool = None

    def as_request(self) -> (dict, dict):
        delete_query, delete_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.path:
            delete_body['path'] = self.path
        if self.recursive:
            delete_body['recursive'] = self.recursive
        
        return delete_query, delete_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Delete':
        return cls(
            path=d.get('path', None),
            recursive=d.get('recursive', None),
        )



@dataclass
class ExportResponse:
    
    # The base64-encoded content. If the limit (10MB) is exceeded, exception
    # with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** will be thrown.
    content: str = None

    def as_request(self) -> (dict, dict):
        exportResponse_query, exportResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.content:
            exportResponse_body['content'] = self.content
        
        return exportResponse_query, exportResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportResponse':
        return cls(
            content=d.get('content', None),
        )



@dataclass
class Import:
    
    # The absolute path of the notebook or directory. Importing directory is
    # only support for ``DBC`` format.
    path: str
    # The base64-encoded content. This has a limit of 10 MB. If the limit (10MB)
    # is exceeded, exception with error code **MAX_NOTEBOOK_SIZE_EXCEEDED** will
    # be thrown. This parameter might be absent, and instead a posted file will
    # be used. See :ref:`workspace-api-import-example` for more information
    # about how to use it.
    content: str = None
    # This specifies the format of the file to be imported. By default, this is
    # ``SOURCE``. However it may be one of: ``SOURCE``, ``HTML``, ``JUPYTER``,
    # ``DBC``. The value is case sensitive.
    format: 'ImportFormat' = None
    # The language. If format is set to ``SOURCE``, this field is required;
    # otherwise, it will be ignored.
    language: 'ImportLanguage' = None
    # The flag that specifies whether to overwrite existing object. It is
    # ``false`` by default. For ``DBC`` format, ``overwrite`` is not supported
    # since it may contain a directory.
    overwrite: bool = None

    def as_request(self) -> (dict, dict):
        import_query, import_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.content:
            import_body['content'] = self.content
        if self.format:
            import_body['format'] = self.format.value
        if self.language:
            import_body['language'] = self.language.value
        if self.overwrite:
            import_body['overwrite'] = self.overwrite
        if self.path:
            import_body['path'] = self.path
        
        return import_query, import_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Import':
        return cls(
            content=d.get('content', None),
            format=ImportFormat(d['format']) if 'format' in d else None,
            language=ImportLanguage(d['language']) if 'language' in d else None,
            overwrite=d.get('overwrite', None),
            path=d.get('path', None),
        )



class ImportFormat(Enum):
    """This specifies the format of the file to be imported. By default, this is
    ``SOURCE``. However it may be one of: ``SOURCE``, ``HTML``, ``JUPYTER``,
    ``DBC``. The value is case sensitive."""
    
    DBC = 'DBC'
    HTML = 'HTML'
    JUPYTER = 'JUPYTER'
    R_MARKDOWN = 'R_MARKDOWN'
    SOURCE = 'SOURCE'

class ImportLanguage(Enum):
    """The language. If format is set to ``SOURCE``, this field is required;
    otherwise, it will be ignored."""
    
    PYTHON = 'PYTHON'
    R = 'R'
    SCALA = 'SCALA'
    SQL = 'SQL'

@dataclass
class ListResponse:
    
    # List of objects.
    objects: 'List[ObjectInfo]' = None

    def as_request(self) -> (dict, dict):
        listResponse_query, listResponse_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.objects:
            listResponse_body['objects'] = [v.as_request()[1] for v in self.objects]
        
        return listResponse_query, listResponse_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListResponse':
        return cls(
            objects=[ObjectInfo.from_dict(v) for v in d['objects']] if 'objects' in d else None,
        )



@dataclass
class Mkdirs:
    
    # The absolute path of the directory. If the parent directories do not
    # exist, it will also create them. If the directory already exists, this
    # command will do nothing and succeed.
    path: str

    def as_request(self) -> (dict, dict):
        mkdirs_query, mkdirs_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.path:
            mkdirs_body['path'] = self.path
        
        return mkdirs_query, mkdirs_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Mkdirs':
        return cls(
            path=d.get('path', None),
        )



@dataclass
class ObjectInfo:
    
    # The location (bucket and prefix) enum value of the content blob. This
    # field is used in conjunction with the blob_path field to determine where
    # the blob is located.
    blob_location: 'ObjectInfoBlobLocation' = None
    # ========= File metadata. These values are set only if the object type is
    # ``FILE``. ===========//
    blob_path: str = None
    # <content needed>
    content_sha256_hex: str = None
    # <content needed>
    created_at: int = None
    # The language of the object. This value is set only if the object type is
    # ``NOTEBOOK``.
    language: 'ObjectInfoLanguage' = None
    # <content needed>
    metadata_version: int = None
    # <content needed>
    modified_at: int = None
    # <content needed>
    object_id: int = None
    # <content needed>
    object_type: 'ObjectInfoObjectType' = None
    # The absolute path of the object.
    path: str = None
    # <content needed>
    size: int = None

    def as_request(self) -> (dict, dict):
        objectInfo_query, objectInfo_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.blob_location:
            objectInfo_body['blob_location'] = self.blob_location.value
        if self.blob_path:
            objectInfo_body['blob_path'] = self.blob_path
        if self.content_sha256_hex:
            objectInfo_body['content_sha256_hex'] = self.content_sha256_hex
        if self.created_at:
            objectInfo_body['created_at'] = self.created_at
        if self.language:
            objectInfo_body['language'] = self.language.value
        if self.metadata_version:
            objectInfo_body['metadata_version'] = self.metadata_version
        if self.modified_at:
            objectInfo_body['modified_at'] = self.modified_at
        if self.object_id:
            objectInfo_body['object_id'] = self.object_id
        if self.object_type:
            objectInfo_body['object_type'] = self.object_type.value
        if self.path:
            objectInfo_body['path'] = self.path
        if self.size:
            objectInfo_body['size'] = self.size
        
        return objectInfo_query, objectInfo_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ObjectInfo':
        return cls(
            blob_location=ObjectInfoBlobLocation(d['blob_location']) if 'blob_location' in d else None,
            blob_path=d.get('blob_path', None),
            content_sha256_hex=d.get('content_sha256_hex', None),
            created_at=d.get('created_at', None),
            language=ObjectInfoLanguage(d['language']) if 'language' in d else None,
            metadata_version=d.get('metadata_version', None),
            modified_at=d.get('modified_at', None),
            object_id=d.get('object_id', None),
            object_type=ObjectInfoObjectType(d['object_type']) if 'object_type' in d else None,
            path=d.get('path', None),
            size=d.get('size', None),
        )



class ObjectInfoBlobLocation(Enum):
    """The location (bucket and prefix) enum value of the content blob. This field
    is used in conjunction with the blob_path field to determine where the blob
    is located."""
    
    DBFS_ROOT = 'DBFS_ROOT'
    INTERNAL_DBFS_JOBS = 'INTERNAL_DBFS_JOBS'

class ObjectInfoLanguage(Enum):
    """The language of the object. This value is set only if the object type is
    ``NOTEBOOK``."""
    
    PYTHON = 'PYTHON'
    R = 'R'
    SCALA = 'SCALA'
    SQL = 'SQL'

class ObjectInfoObjectType(Enum):
    """<content needed>"""
    
    DIRECTORY = 'DIRECTORY'
    FILE = 'FILE'
    LIBRARY = 'LIBRARY'
    MLFLOW_EXPERIMENT = 'MLFLOW_EXPERIMENT'
    NOTEBOOK = 'NOTEBOOK'
    PROJECT = 'PROJECT'
    REPO = 'REPO'

@dataclass
class ExportRequest:
    
    # The absolute path of the notebook or directory. Exporting directory is
    # only support for ``DBC`` format.
    path: str # query
    # Flag to enable direct download. If it is ``true``, the response will be
    # the exported file itself. Otherwise, the response contains content as
    # base64 encoded string. See :ref:`workspace-api-export-example` for more
    # information about how to use it.
    direct_download: bool = None # query
    # This specifies the format of the exported file. By default, this is
    # ``SOURCE``. However it may be one of: ``SOURCE``, ``HTML``, ``JUPYTER``,
    # ``DBC``. The value is case sensitive.
    format: str = None # query

    def as_request(self) -> (dict, dict):
        exportRequest_query, exportRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.direct_download:
            exportRequest_query['direct_download'] = self.direct_download
        if self.format:
            exportRequest_query['format'] = self.format
        if self.path:
            exportRequest_query['path'] = self.path
        
        return exportRequest_query, exportRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ExportRequest':
        return cls(
            direct_download=d.get('direct_download', None),
            format=d.get('format', None),
            path=d.get('path', None),
        )



@dataclass
class GetStatusRequest:
    
    # The absolute path of the notebook or directory.
    path: str # query

    def as_request(self) -> (dict, dict):
        getStatusRequest_query, getStatusRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.path:
            getStatusRequest_query['path'] = self.path
        
        return getStatusRequest_query, getStatusRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'GetStatusRequest':
        return cls(
            path=d.get('path', None),
        )



@dataclass
class ListRequest:
    
    # The absolute path of the notebook or directory.
    path: str # query
    # <content needed>
    notebooks_modified_after: int = None # query

    def as_request(self) -> (dict, dict):
        listRequest_query, listRequest_body = {}, {} # TODO: add .HasQuery() and .HasBody() to code generator
        if self.notebooks_modified_after:
            listRequest_query['notebooks_modified_after'] = self.notebooks_modified_after
        if self.path:
            listRequest_query['path'] = self.path
        
        return listRequest_query, listRequest_body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListRequest':
        return cls(
            notebooks_modified_after=d.get('notebooks_modified_after', None),
            path=d.get('path', None),
        )



class WorkspaceAPI:
    def __init__(self, api_client):
        self._api = api_client
    
    def delete(self, request: Delete):
        """Delete a workspace object
        
        Deletes an object or a directory (and optionally recursively deletes all
        objects in the directory). * If ``path`` does not exist, this call
        returns an error ``RESOURCE_DOES_NOT_EXIST``. * If ``path`` is a
        non-empty directory and ``recursive`` is set to ``false``, this call
        returns an error ``DIRECTORY_NOT_EMPTY``.
        
        Object deletion cannot be undone and deleting a directory recursively is
        not atomic.
        
        Example of request:
        
        ```json { "path": "/Users/user-name/project", "recursive": true } ```"""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/workspace/delete', query=query, body=body)
        
    
    def export(self, request: ExportRequest) -> ExportResponse:
        """Export a notebook
        
        Exports a notebook or the contents of an entire directory. If ``path``
        does not exist, this call returns an error ``RESOURCE_DOES_NOT_EXIST``.
        One can only export a directory in ``DBC`` format. If the exported data
        would exceed size limit, this call returns an error
        ``MAX_NOTEBOOK_SIZE_EXCEEDED``. Currently, this API does not support
        exporting a library. Example of request:
        
        .. code :: json
        
        { "path": "/Users/user@example.com/project/ScalaExampleNotebook",
        "format": "SOURCE" }
        
        Example of response, where ``content`` is base64-encoded:
        
        .. code :: json
        
        { "content": "Ly8gRGF0YWJyaWNrcyBub3RlYm9vayBzb3VyY2UKMSsx", }
        
        Alternaitvely, one can download the exported file by enabling
        ``direct_download``:
        
        .. code :: shell
        
        curl -n -o example.scala \
        'https://XX.cloud.databricks.com/api/2.0/workspace/export?path=/Users/user@example.com/ScalaExampleNotebook&direct_download=true'"""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/workspace/export', query=query, body=body)
        return ExportResponse.from_dict(json)
    
    def getStatus(self, request: GetStatusRequest) -> ObjectInfo:
        """Get status
        
        Gets the status of an object or a directory. If ``path`` does not exist,
        this call returns an error ``RESOURCE_DOES_NOT_EXIST``. Example of
        request:
        
        .. code :: json
        
        { "path": "/Users/user@example.com/project/ScaleExampleNotebook" }
        
        Example of response:
        
        .. code :: json
        
        { "path": "/Users/user@example.com/project/ScalaExampleNotebook",
        "language": "SCALA", "object_type": "NOTEBOOK", "object_id": 789 }"""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/workspace/get-status', query=query, body=body)
        return ObjectInfo.from_dict(json)
    
    def import(self, request: Import):
        """Import a notebook
        
        Imports a notebook or the contents of an entire directory. If ``path``
        already exists and ``overwrite`` is set to ``false``, this call returns
        an error ``RESOURCE_ALREADY_EXISTS``. One can only use ``DBC`` format to
        import a directory. Example of request, where ``content`` is the
        base64-encoded string of ``1+1``:
        
        .. code :: json
        
        { "content": "MSsx\n", "path":
        "/Users/user@example.com/project/ScalaExampleNotebook", "language":
        "SCALA", "overwrite": true, "format": "SOURCE" }
        
        Alternatively, one can import a local file directly:
        
        .. code :: shell
        
        curl -n -F path=/Users/user@example.com/project/ScalaExampleNotebook -F
        language=SCALA \ -F content=@example.scala \
        https://XX.cloud.databricks.com/api/2.0/workspace/import"""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/workspace/import', query=query, body=body)
        
    
    def list(self, request: ListRequest) -> ListResponse:
        """List contents
        
        Lists the contents of a directory, or the object if it is not a
        directory. If the input path does not exist, this call returns an error
        ``RESOURCE_DOES_NOT_EXIST``. Example of request:
        
        .. code :: json
        
        { "path": "/Users/user@example.com/" }
        
        Example of response:
        
        .. code :: json
        
        { "objects": [ { "path": "/Users/user@example.com/project",
        "object_type": "DIRECTORY", "object_id": 123 }, { "path":
        "/Users/user@example.com/PythonExampleNotebook", "language": "PYTHON",
        "object_type": "NOTEBOOK", "object_id": 456 } ] }"""
        query, body = request.as_request()
        json = self._api.do('GET', '/api/2.0/workspace/list', query=query, body=body)
        return ListResponse.from_dict(json)
    
    def mkdirs(self, request: Mkdirs):
        """Create a directory
        
        Creates the specified directory (and necessary parent directories if
        they do not exist) . If there is an object (not a directory) at any
        prefix of the input path, this call returns an error
        ``RESOURCE_ALREADY_EXISTS``. Note that if this operation fails it may
        have succeeded in creating some of the necessary parrent directories.
        Example of request:
        
        .. code:: json
        
        { "path": "/Users/user@example.com/project" }"""
        query, body = request.as_request()
        self._api.do('POST', '/api/2.0/workspace/mkdirs', query=query, body=body)
        
    