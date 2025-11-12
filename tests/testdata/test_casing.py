import pytest  # type: ignore[import-not-found]

from databricks.sdk.casing import Casing


@pytest.mark.parametrize(
    "name, expected",
    [
        ("", ""),
        ("a", "A"),
        ("abc", "Abc"),
        ("Abc", "Abc"),
        ("abc_def", "Abc-Def"),
        ("abc-def", "Abc-Def"),
        ("abcDef", "Abc-Def"),
        ("AbcDef", "Abc-Def"),
    ],
)
def test_to_header_case(name, expected):
    assert Casing.to_header_case(name) == expected
