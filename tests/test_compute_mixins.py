import pytest

from databricks.sdk.mixins.compute import SemVer


@pytest.mark.parametrize("given,expected",
                         [('v0.0.4', SemVer(0, 0, 4)), ('v1.2.3', SemVer(1, 2, 3)),
                          ('v12.1.x', SemVer(12, 1, 0)), ('v10.20.30', SemVer(10, 20, 30)),
                          ('v1.1.2+meta', SemVer(1, 1, 2, build='meta')),
                          ('v1.0.0-alpha', SemVer(1, 0, 0, pre_release='alpha')),
                          ('8.x-snapshot-scala2.12', SemVer(8, 0, 0, pre_release='snapshot-scala2.12')), ])
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
