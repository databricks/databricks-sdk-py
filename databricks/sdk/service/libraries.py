# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from ._internal import _enum, _from_dict, _repeated

_LOG = logging.getLogger('databricks.sdk')

# all definitions in this file are in alphabetical order


@dataclass
class ClusterLibraryStatuses:
    cluster_id: str = None
    library_statuses: 'List[LibraryFullStatus]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.library_statuses: body['library_statuses'] = [v.as_dict() for v in self.library_statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ClusterLibraryStatuses':
        return cls(cluster_id=d.get('cluster_id', None),
                   library_statuses=_repeated(d, 'library_statuses', LibraryFullStatus))


@dataclass
class ClusterStatus:
    """Get status"""

    cluster_id: str


@dataclass
class InstallLibraries:
    cluster_id: str
    libraries: 'List[Library]'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'InstallLibraries':
        return cls(cluster_id=d.get('cluster_id', None), libraries=_repeated(d, 'libraries', Library))


@dataclass
class Library:
    cran: 'RCranLibrary' = None
    egg: str = None
    jar: str = None
    maven: 'MavenLibrary' = None
    pypi: 'PythonPyPiLibrary' = None
    whl: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.cran: body['cran'] = self.cran.as_dict()
        if self.egg: body['egg'] = self.egg
        if self.jar: body['jar'] = self.jar
        if self.maven: body['maven'] = self.maven.as_dict()
        if self.pypi: body['pypi'] = self.pypi.as_dict()
        if self.whl: body['whl'] = self.whl
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'Library':
        return cls(cran=_from_dict(d, 'cran', RCranLibrary),
                   egg=d.get('egg', None),
                   jar=d.get('jar', None),
                   maven=_from_dict(d, 'maven', MavenLibrary),
                   pypi=_from_dict(d, 'pypi', PythonPyPiLibrary),
                   whl=d.get('whl', None))


@dataclass
class LibraryFullStatus:
    is_library_for_all_clusters: bool = None
    library: 'Library' = None
    messages: 'List[str]' = None
    status: 'LibraryFullStatusStatus' = None

    def as_dict(self) -> dict:
        body = {}
        if self.is_library_for_all_clusters:
            body['is_library_for_all_clusters'] = self.is_library_for_all_clusters
        if self.library: body['library'] = self.library.as_dict()
        if self.messages: body['messages'] = [v for v in self.messages]
        if self.status: body['status'] = self.status.value
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'LibraryFullStatus':
        return cls(is_library_for_all_clusters=d.get('is_library_for_all_clusters', None),
                   library=_from_dict(d, 'library', Library),
                   messages=d.get('messages', None),
                   status=_enum(d, 'status', LibraryFullStatusStatus))


class LibraryFullStatusStatus(Enum):
    """Status of installing the library on the cluster."""

    FAILED = 'FAILED'
    INSTALLED = 'INSTALLED'
    INSTALLING = 'INSTALLING'
    PENDING = 'PENDING'
    RESOLVING = 'RESOLVING'
    SKIPPED = 'SKIPPED'
    UNINSTALL_ON_RESTART = 'UNINSTALL_ON_RESTART'


@dataclass
class ListAllClusterLibraryStatusesResponse:
    statuses: 'List[ClusterLibraryStatuses]' = None

    def as_dict(self) -> dict:
        body = {}
        if self.statuses: body['statuses'] = [v.as_dict() for v in self.statuses]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'ListAllClusterLibraryStatusesResponse':
        return cls(statuses=_repeated(d, 'statuses', ClusterLibraryStatuses))


@dataclass
class MavenLibrary:
    coordinates: str
    exclusions: 'List[str]' = None
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.coordinates: body['coordinates'] = self.coordinates
        if self.exclusions: body['exclusions'] = [v for v in self.exclusions]
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'MavenLibrary':
        return cls(coordinates=d.get('coordinates', None),
                   exclusions=d.get('exclusions', None),
                   repo=d.get('repo', None))


@dataclass
class PythonPyPiLibrary:
    package: str
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.package: body['package'] = self.package
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'PythonPyPiLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class RCranLibrary:
    package: str
    repo: str = None

    def as_dict(self) -> dict:
        body = {}
        if self.package: body['package'] = self.package
        if self.repo: body['repo'] = self.repo
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'RCranLibrary':
        return cls(package=d.get('package', None), repo=d.get('repo', None))


@dataclass
class UninstallLibraries:
    cluster_id: str
    libraries: 'List[Library]'

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id: body['cluster_id'] = self.cluster_id
        if self.libraries: body['libraries'] = [v.as_dict() for v in self.libraries]
        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> 'UninstallLibraries':
        return cls(cluster_id=d.get('cluster_id', None), libraries=_repeated(d, 'libraries', Library))


class LibrariesAPI:
    """The Libraries API allows you to install and uninstall libraries and get the status of libraries on a
    cluster.
    
    To make third-party or custom code available to notebooks and jobs running on your clusters, you can
    install a library. Libraries can be written in Python, Java, Scala, and R. You can upload Java, Scala, and
    Python libraries and point to external packages in PyPI, Maven, and CRAN repositories.
    
    Cluster libraries can be used by all notebooks running on a cluster. You can install a cluster library
    directly from a public repository such as PyPI or Maven, using a previously installed workspace library,
    or using an init script.
    
    When you install a library on a cluster, a notebook already attached to that cluster will not immediately
    see the new library. You must first detach and then reattach the notebook to the cluster.
    
    When you uninstall a library from a cluster, the library is removed only when you restart the cluster.
    Until you restart the cluster, the status of the uninstalled library appears as Uninstall pending restart."""

    def __init__(self, api_client):
        self._api = api_client

    def all_cluster_statuses(self) -> ListAllClusterLibraryStatusesResponse:
        """Get all statuses.
        
        Get the status of all libraries on all clusters. A status will be available for all libraries
        installed on this cluster via the API or the libraries UI as well as libraries set to be installed on
        all clusters via the libraries UI."""

        json = self._api.do('GET', '/api/2.0/libraries/all-cluster-statuses')
        return ListAllClusterLibraryStatusesResponse.from_dict(json)

    def cluster_status(self, cluster_id: str, **kwargs) -> ClusterLibraryStatuses:
        """Get status.
        
        Get the status of libraries on a cluster. A status will be available for all libraries installed on
        this cluster via the API or the libraries UI as well as libraries set to be installed on all clusters
        via the libraries UI. The order of returned libraries will be as follows.
        
        1. Libraries set to be installed on this cluster will be returned first. Within this group, the final
        order will be order in which the libraries were added to the cluster.
        
        2. Libraries set to be installed on all clusters are returned next. Within this group there is no
        order guarantee.
        
        3. Libraries that were previously requested on this cluster or on all clusters, but now marked for
        removal. Within this group there is no order guarantee."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = ClusterStatus(cluster_id=cluster_id)

        query = {}
        if cluster_id: query['cluster_id'] = request.cluster_id

        json = self._api.do('GET', '/api/2.0/libraries/cluster-status', query=query)
        return ClusterLibraryStatuses.from_dict(json)

    def install(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Add a library.
        
        Add libraries to be installed on a cluster. The installation is asynchronous; it happens in the
        background after the completion of this request.
        
        **Note**: The actual set of libraries to be installed on a cluster is the union of the libraries
        specified via this method and the libraries set to be installed on all clusters via the libraries UI."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = InstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/libraries/install', body=body)

    def uninstall(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Uninstall libraries.
        
        Set libraries to be uninstalled on a cluster. The libraries won't be uninstalled until the cluster is
        restarted. Uninstalling libraries that are not installed on the cluster will have no impact but is not
        an error."""
        request = kwargs.get('request', None)
        if not request: # request is not given through keyed args
            request = UninstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        self._api.do('POST', '/api/2.0/libraries/uninstall', body=body)
