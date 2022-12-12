import typing

from .client import *
from .service import clusters, tokens

def test_profile_auth():
    from databricks.sdk import WorkspaceClient
    w = WorkspaceClient()
    w.clusters.list()


def test_marshall_to_dict():
    c = ApiClient()
    res = c.marshall(
        tokens.CreateTokenResponse(
            token_info=tokens.PublicTokenInfo(comment="test"),
            token_value="going to be redacted",
        ),
        redact_sensitive=True,
    )

    assert res == {"token_info": {"comment": "test"}, "token_value": "*REDACTED*"}


def test_conversions():
    info = clusters.ClusterInfo(
        state=clusters.ClusterInfoState.RUNNING,
        autotermination_minutes=10,
        custom_tags={"foo": "bar"},
        ssh_public_keys=["abc", "bcd"],
        autoscale=clusters.AutoScale(min_workers=10, max_workers=20),
    )

    assert info == clusters.ClusterInfo.from_dict(info.as_dict())


def test_unmarshall_to_dataclass():
    c = ApiClient()
    res = c.unmarshall(
        {
            "autotermination_minutes": 10,
            "state": "RUNNING",
            "custom_tags": {
                "foo": "bar",
            },
            "ssh_public_keys": ["abc", "bcd"],
            "autoscale": {"min_workers": 10, "max_workers": 20},
        },
        clusters.ClusterInfo,
    )

    assert res == clusters.ClusterInfo(
        state=clusters.ClusterInfoState.RUNNING,
        autotermination_minutes=10,
        custom_tags={"foo": "bar"},
        ssh_public_keys=["abc", "bcd"],
        autoscale=clusters.AutoScale(10, 20),
    )
