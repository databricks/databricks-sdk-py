import pytest

from databricks.sdk import WorkspaceClient
from databricks.sdk.mixins.compute import SemVer
from databricks.sdk.service import compute


@pytest.mark.parametrize(
    "given,expected",
    [
        ("v0.0.4", SemVer(0, 0, 4)),
        ("v1.2.3", SemVer(1, 2, 3)),
        ("v12.1.x", SemVer(12, 1, 0)),
        ("v10.20.30", SemVer(10, 20, 30)),
        ("v1.1.2+meta", SemVer(1, 1, 2, build="meta")),
        ("v1.0.0-alpha", SemVer(1, 0, 0, pre_release="alpha")),
        (
            "8.x-snapshot-scala2.12",
            SemVer(8, 0, 0, pre_release="snapshot-scala2.12"),
        ),
    ],
)
def test_parse_semver(given, expected):
    assert SemVer.parse(given) == expected


def test_sorting_semver():
    unsorted = [
        SemVer(1, 0, 0),
        SemVer(0, 1, 0),
        SemVer(12, 0, 0),
        SemVer(0, 15, 0),
        SemVer(0, 0, 1),
        SemVer(0, 0, 22),
    ]

    assert sorted(unsorted) == [
        SemVer(0, 0, 1),
        SemVer(0, 0, 22),
        SemVer(0, 1, 0),
        SemVer(0, 15, 0),
        SemVer(1, 0, 0),
        SemVer(12, 0, 0),
    ]


def test_select_spark_version_filters_and_selects_latest_lts_from_http(config, requests_mock):
    requests_mock.get(
        "http://localhost/api/2.1/clusters/spark-versions",
        json={
            "versions": [
                {
                    "key": "14.3.x-scala2.12",
                    "name": "14.3 LTS (includes Apache Spark 3.5.0, Scala 2.12)",
                },
                {
                    "key": "15.4.x-scala2.12",
                    "name": "15.4 LTS (includes Apache Spark 3.5.0, Scala 2.12)",
                },
                {
                    "key": "16.0.x-scala2.12",
                    "name": "16.0 Beta (includes Apache Spark 4.0.0, Scala 2.12)",
                },
                {
                    "key": "15.4.x-photon-scala2.12",
                    "name": "15.4 LTS Photon (includes Apache Spark 3.5.0, Scala 2.12)",
                },
            ]
        },
    )
    workspace = WorkspaceClient(config=config)

    selected = workspace.clusters.select_spark_version(long_term_support=True)

    assert selected == "15.4.x-scala2.12"
    assert requests_mock.last_request.method == "GET"


def test_select_node_type_filters_diskless_and_unavailable_nodes_from_http(config, requests_mock):
    def node_type(
        node_type_id,
        *,
        memory_mb,
        num_cores,
        local_disks,
        local_disk_size_gb,
        node_info=None,
    ):
        node = {
            "category": "General Purpose",
            "description": node_type_id,
            "instance_type_id": node_type_id,
            "is_deprecated": False,
            "memory_mb": memory_mb,
            "node_instance_type": {
                "instance_type_id": node_type_id,
                "local_disk_size_gb": local_disk_size_gb,
                "local_disks": local_disks,
                "local_nvme_disk_size_gb": 0,
                "local_nvme_disks": 0,
            },
            "node_type_id": node_type_id,
            "num_cores": num_cores,
            "num_gpus": 0,
        }
        if node_info is not None:
            node["node_info"] = node_info
        return node

    requests_mock.get(
        "http://localhost/api/2.1/clusters/list-node-types",
        json={
            "node_types": [
                node_type(
                    "unavailable-local",
                    memory_mb=4096,
                    num_cores=2,
                    local_disks=1,
                    local_disk_size_gb=100,
                    node_info={"status": ["NotAvailableInRegion"]},
                ),
                node_type(
                    "diskless-small",
                    memory_mb=4096,
                    num_cores=2,
                    local_disks=0,
                    local_disk_size_gb=0,
                ),
                node_type(
                    "local-medium",
                    memory_mb=8192,
                    num_cores=4,
                    local_disks=1,
                    local_disk_size_gb=100,
                ),
                node_type(
                    "local-large",
                    memory_mb=16384,
                    num_cores=8,
                    local_disks=1,
                    local_disk_size_gb=200,
                ),
            ]
        },
    )
    workspace = WorkspaceClient(config=config)

    selected = workspace.clusters.select_node_type(local_disk=True)

    assert selected == "local-medium"
    assert requests_mock.last_request.method == "GET"


def test_ensure_cluster_is_running_waits_for_termination_then_starts(config, monkeypatch, requests_mock):
    cluster_url = "http://localhost/api/2.1/clusters/get?cluster_id=cluster-1"
    requests_mock.register_uri(
        "GET",
        cluster_url,
        [
            {"json": {"cluster_id": "cluster-1", "cluster_name": "fixture", "state": "TERMINATING"}},
            {"json": {"cluster_id": "cluster-1", "cluster_name": "fixture", "state": "TERMINATED"}},
            {"json": {"cluster_id": "cluster-1", "cluster_name": "fixture", "state": "PENDING"}},
            {"json": {"cluster_id": "cluster-1", "cluster_name": "fixture", "state": "RUNNING"}},
        ],
    )
    requests_mock.post("http://localhost/api/2.1/clusters/start", json={})
    monkeypatch.setattr(compute.time, "sleep", lambda _: None)
    workspace = WorkspaceClient(config=config)

    workspace.clusters.ensure_cluster_is_running("cluster-1")

    assert [request.method for request in requests_mock.request_history] == ["GET", "GET", "POST", "GET", "GET"]
    assert requests_mock.request_history[2].json() == {"cluster_id": "cluster-1"}


def test_cluster_events_reposts_next_page_request_at_http_boundary(config, requests_mock):
    next_page = {
        "cluster_id": "cluster-1",
        "event_types": ["STARTING", "TERMINATING"],
        "limit": 1,
        "offset": 1,
    }
    requests_mock.register_uri(
        "POST",
        "http://localhost/api/2.1/clusters/events",
        [
            {
                "json": {
                    "events": [{"cluster_id": "cluster-1", "timestamp": 1000, "type": "STARTING"}],
                    "next_page": next_page,
                }
            },
            {"json": {"events": [{"cluster_id": "cluster-1", "timestamp": 2000, "type": "TERMINATING"}]}},
        ],
    )
    workspace = WorkspaceClient(config=config)

    events = list(
        workspace.clusters.events(
            "cluster-1",
            event_types=[compute.EventType.STARTING, compute.EventType.TERMINATING],
            limit=1,
        )
    )

    assert [event.type for event in events] == [compute.EventType.STARTING, compute.EventType.TERMINATING]
    assert requests_mock.request_history[0].json() == {
        "cluster_id": "cluster-1",
        "event_types": ["STARTING", "TERMINATING"],
        "limit": 1,
    }
    assert requests_mock.request_history[1].json() == next_page
