from types import SimpleNamespace
from unittest.mock import MagicMock

from databricks.sdk.service.catalog import EntityTagAssignmentsAPI


def _client_with_mock_api():
    api = MagicMock()
    api._cfg = SimpleNamespace(workspace_id=None)
    api.do.return_value = {"tag_assignments": []}
    return EntityTagAssignmentsAPI(api), api


def test_list_encodes_slash_in_entity_name():
    client, api = _client_with_mock_api()
    entity_name = "main.my_schema.my_table.Inferences/Second"
    list(client.list(entity_type="columns", entity_name=entity_name))
    method, path = api.do.call_args.args[:2]
    assert method == "GET"
    assert path == (
        "/api/2.1/unity-catalog/entity-tag-assignments/columns/"
        "main.my_schema.my_table.Inferences%2FSecond/tags"
    )


def test_get_encodes_slash_in_entity_name_and_tag_key():
    client, api = _client_with_mock_api()
    api.do.return_value = {
        "entity_type": "columns",
        "entity_name": "main.s.t.Inferences/Second",
        "tag_key": "a/b",
    }
    client.get(
        entity_type="columns",
        entity_name="main.s.t.Inferences/Second",
        tag_key="a/b",
    )
    method, path = api.do.call_args.args[:2]
    assert method == "GET"
    assert path == (
        "/api/2.1/unity-catalog/entity-tag-assignments/columns/"
        "main.s.t.Inferences%2FSecond/tags/a%2Fb"
    )


def test_delete_encodes_slash_in_entity_name():
    client, api = _client_with_mock_api()
    client.delete(
        entity_type="columns",
        entity_name="cat.sch.tbl.Inferences/Second",
        tag_key="env",
    )
    method, path = api.do.call_args.args[:2]
    assert method == "DELETE"
    assert path == (
        "/api/2.1/unity-catalog/entity-tag-assignments/columns/"
        "cat.sch.tbl.Inferences%2FSecond/tags/env"
    )
