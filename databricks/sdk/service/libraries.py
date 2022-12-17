# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class ClusterLibraryStatuses:

    # Unique identifier for the cluster.
    cluster_id: str
    # Status of all libraries on the cluster.
    library_statuses: "List[LibraryFullStatus]"

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id:
            body["cluster_id"] = self.cluster_id
        if self.library_statuses:
            body["library_statuses"] = [v.as_dict() for v in self.library_statuses]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ClusterLibraryStatuses":
        return cls(
            cluster_id=d.get("cluster_id", None),
            library_statuses=[
                LibraryFullStatus.from_dict(v) for v in d["library_statuses"]
            ]
            if "library_statuses" in d
            else None,
        )


@dataclass
class ClusterStatus:
    """Get status"""

    # Unique identifier of the cluster whose status should be retrieved.
    cluster_id: str  # query

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id:
            body["cluster_id"] = self.cluster_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ClusterStatus":
        return cls(
            cluster_id=d.get("cluster_id", None),
        )


@dataclass
class InstallLibraries:

    # Unique identifier for the cluster on which to install these libraries.
    cluster_id: str
    # The libraries to install.
    libraries: "List[Library]"

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id:
            body["cluster_id"] = self.cluster_id
        if self.libraries:
            body["libraries"] = [v.as_dict() for v in self.libraries]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "InstallLibraries":
        return cls(
            cluster_id=d.get("cluster_id", None),
            libraries=[Library.from_dict(v) for v in d["libraries"]]
            if "libraries" in d
            else None,
        )


@dataclass
class Library:

    # Specification of a CRAN library to be installed as part of the library
    cran: "RCranLibrary"
    # URI of the egg to be installed. Currently only DBFS and S3 URIs are
    # supported. For example: `{ "egg": "dbfs:/my/egg" }` or `{ "egg":
    # "s3://my-bucket/egg" }`. If S3 is used, please make sure the cluster has
    # read access on the library. You may need to launch the cluster with an IAM
    # role to access the S3 URI.
    egg: str
    # URI of the jar to be installed. Currently only DBFS and S3 URIs are
    # supported. For example: `{ "jar": "dbfs:/mnt/databricks/library.jar" }` or
    # `{ "jar": "s3://my-bucket/library.jar" }`. If S3 is used, please make sure
    # the cluster has read access on the library. You may need to launch the
    # cluster with an IAM role to access the S3 URI.
    jar: str
    # Specification of a maven library to be installed. For example: `{
    # "coordinates": "org.jsoup:jsoup:1.7.2" }`
    maven: "MavenLibrary"
    # Specification of a PyPi library to be installed. For example: `{
    # "package": "simplejson" }`
    pypi: "PythonPyPiLibrary"
    # URI of the wheel to be installed. For example: `{ "whl": "dbfs:/my/whl" }`
    # or `{ "whl": "s3://my-bucket/whl" }`. If S3 is used, please make sure the
    # cluster has read access on the library. You may need to launch the cluster
    # with an IAM role to access the S3 URI.
    whl: str

    def as_dict(self) -> dict:
        body = {}
        if self.cran:
            body["cran"] = self.cran.as_dict()
        if self.egg:
            body["egg"] = self.egg
        if self.jar:
            body["jar"] = self.jar
        if self.maven:
            body["maven"] = self.maven.as_dict()
        if self.pypi:
            body["pypi"] = self.pypi.as_dict()
        if self.whl:
            body["whl"] = self.whl

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Library":
        return cls(
            cran=RCranLibrary.from_dict(d["cran"]) if "cran" in d else None,
            egg=d.get("egg", None),
            jar=d.get("jar", None),
            maven=MavenLibrary.from_dict(d["maven"]) if "maven" in d else None,
            pypi=PythonPyPiLibrary.from_dict(d["pypi"]) if "pypi" in d else None,
            whl=d.get("whl", None),
        )


@dataclass
class LibraryFullStatus:

    # Whether the library was set to be installed on all clusters via the
    # libraries UI.
    is_library_for_all_clusters: bool
    # Unique identifier for the library.
    library: "Library"
    # All the info and warning messages that have occurred so far for this
    # library.
    messages: "List[str]"
    # Status of installing the library on the cluster.
    status: "LibraryFullStatusStatus"

    def as_dict(self) -> dict:
        body = {}
        if self.is_library_for_all_clusters:
            body["is_library_for_all_clusters"] = self.is_library_for_all_clusters
        if self.library:
            body["library"] = self.library.as_dict()
        if self.messages:
            body["messages"] = [v for v in self.messages]
        if self.status:
            body["status"] = self.status.value

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "LibraryFullStatus":
        return cls(
            is_library_for_all_clusters=d.get("is_library_for_all_clusters", None),
            library=Library.from_dict(d["library"]) if "library" in d else None,
            messages=d.get("messages", None),
            status=LibraryFullStatusStatus(d["status"]) if "status" in d else None,
        )


class LibraryFullStatusStatus(Enum):
    """Status of installing the library on the cluster."""

    FAILED = "FAILED"
    INSTALLED = "INSTALLED"
    INSTALLING = "INSTALLING"
    PENDING = "PENDING"
    RESOLVING = "RESOLVING"
    SKIPPED = "SKIPPED"
    UNINSTALL_ON_RESTART = "UNINSTALL_ON_RESTART"


@dataclass
class ListAllClusterLibraryStatusesResponse:

    # A list of cluster statuses.
    statuses: "List[ClusterLibraryStatuses]"

    def as_dict(self) -> dict:
        body = {}
        if self.statuses:
            body["statuses"] = [v.as_dict() for v in self.statuses]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListAllClusterLibraryStatusesResponse":
        return cls(
            statuses=[ClusterLibraryStatuses.from_dict(v) for v in d["statuses"]]
            if "statuses" in d
            else None,
        )


@dataclass
class MavenLibrary:

    # Gradle-style maven coordinates. For example: "org.jsoup:jsoup:1.7.2".
    coordinates: str
    # List of dependences to exclude. For example: `["slf4j:slf4j",
    # "*:hadoop-client"]`.
    #
    # Maven dependency exclusions:
    # https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html.
    exclusions: "List[str]"
    # Maven repo to install the Maven package from. If omitted, both Maven
    # Central Repository and Spark Packages are searched.
    repo: str

    def as_dict(self) -> dict:
        body = {}
        if self.coordinates:
            body["coordinates"] = self.coordinates
        if self.exclusions:
            body["exclusions"] = [v for v in self.exclusions]
        if self.repo:
            body["repo"] = self.repo

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "MavenLibrary":
        return cls(
            coordinates=d.get("coordinates", None),
            exclusions=d.get("exclusions", None),
            repo=d.get("repo", None),
        )


@dataclass
class PythonPyPiLibrary:

    # The name of the pypi package to install. An optional exact version
    # specification is also supported. Examples: "simplejson" and
    # "simplejson==3.8.0".
    package: str
    # The repository where the package can be found. If not specified, the
    # default pip index is used.
    repo: str

    def as_dict(self) -> dict:
        body = {}
        if self.package:
            body["package"] = self.package
        if self.repo:
            body["repo"] = self.repo

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "PythonPyPiLibrary":
        return cls(
            package=d.get("package", None),
            repo=d.get("repo", None),
        )


@dataclass
class RCranLibrary:

    # The name of the CRAN package to install.
    package: str
    # The repository where the package can be found. If not specified, the
    # default CRAN repo is used.
    repo: str

    def as_dict(self) -> dict:
        body = {}
        if self.package:
            body["package"] = self.package
        if self.repo:
            body["repo"] = self.repo

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "RCranLibrary":
        return cls(
            package=d.get("package", None),
            repo=d.get("repo", None),
        )


@dataclass
class UninstallLibraries:

    # Unique identifier for the cluster on which to uninstall these libraries.
    cluster_id: str
    # The libraries to uninstall.
    libraries: "List[Library]"

    def as_dict(self) -> dict:
        body = {}
        if self.cluster_id:
            body["cluster_id"] = self.cluster_id
        if self.libraries:
            body["libraries"] = [v.as_dict() for v in self.libraries]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UninstallLibraries":
        return cls(
            cluster_id=d.get("cluster_id", None),
            libraries=[Library.from_dict(v) for v in d["libraries"]]
            if "libraries" in d
            else None,
        )


class LibrariesAPI:
    def __init__(self, api_client):
        self._api = api_client

    def all_cluster_statuses(self) -> ListAllClusterLibraryStatusesResponse:
        """Get all statuses.

        Get the status of all libraries on all clusters. A status will be
        available for all libraries installed on this cluster via the API or the
        libraries UI as well as libraries set to be installed on all clusters
        via the libraries UI."""

        json = self._api.do("GET", "/api/2.0/libraries/all-cluster-statuses")
        return ListAllClusterLibraryStatusesResponse.from_dict(json)

    def cluster_status(self, cluster_id: str, **kwargs) -> ClusterLibraryStatuses:
        """Get status.

        Get the status of libraries on a cluster. A status will be available for
        all libraries installed on this cluster via the API or the libraries UI
        as well as libraries set to be installed on all clusters via the
        libraries UI. The order of returned libraries will be as follows.

        1. Libraries set to be installed on this cluster will be returned first.
        Within this group, the final order will be order in which the libraries
        were added to the cluster.

        2. Libraries set to be installed on all clusters are returned next.
        Within this group there is no order guarantee.

        3. Libraries that were previously requested on this cluster or on all
        clusters, but now marked for removal. Within this group there is no
        order guarantee."""

        request = kwargs.get("request", None)
        if not request:
            request = ClusterStatus(cluster_id=cluster_id)
        body = request.as_dict()
        query = {}
        if cluster_id:
            query["cluster_id"] = cluster_id

        json = self._api.do(
            "GET", "/api/2.0/libraries/cluster-status", query=query, body=body
        )
        return ClusterLibraryStatuses.from_dict(json)

    def install(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Add a library.

        Add libraries to be installed on a cluster. The installation is
        asynchronous; it happens in the background after the completion of this
        request.

        **Note**: The actual set of libraries to be installed on a cluster is
        the union of the libraries specified via this method and the libraries
        set to be installed on all clusters via the libraries UI."""

        request = kwargs.get("request", None)
        if not request:
            request = InstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/libraries/install", query=query, body=body)

    def uninstall(self, cluster_id: str, libraries: List[Library], **kwargs):
        """Uninstall libraries.

        Set libraries to be uninstalled on a cluster. The libraries won't be
        uninstalled until the cluster is restarted. Uninstalling libraries that
        are not installed on the cluster will have no impact but is not an
        error."""

        request = kwargs.get("request", None)
        if not request:
            request = UninstallLibraries(cluster_id=cluster_id, libraries=libraries)
        body = request.as_dict()
        query = {}

        self._api.do("POST", "/api/2.0/libraries/uninstall", query=query, body=body)
