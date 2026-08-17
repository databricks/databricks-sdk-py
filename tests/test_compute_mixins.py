import json

import pytest

from databricks.sdk.mixins.compute import SemVer

SPARK_VERSIONS_RESPONSE = {
    "versions": [
        {"key": "16.4.x-scala2.12", "name": "16.4"},
        {"key": "18.2.x-scala2.13", "name": "18.2"},
    ]
}


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


def test_select_spark_version_latest_ignores_scala_by_default(w, requests_mock):
    # Regression test for https://github.com/databricks/databricks-sdk-py/issues/1487:
    # select_spark_version(latest=True) implicitly filtered to the "2.12" default
    # scala version before picking the latest, instead of considering every scala
    # version like the Go SDK it's ported from does.
    requests_mock.get(
        "http://localhost/api/2.1/clusters/spark-versions",
        text=json.dumps(SPARK_VERSIONS_RESPONSE),
    )

    assert w.clusters.select_spark_version(latest=True) == "18.2.x-scala2.13"


def test_select_spark_version_latest_still_honors_an_explicit_scala(w, requests_mock):
    requests_mock.get(
        "http://localhost/api/2.1/clusters/spark-versions",
        text=json.dumps(SPARK_VERSIONS_RESPONSE),
    )

    assert w.clusters.select_spark_version(latest=True, scala="2.12") == "16.4.x-scala2.12"
