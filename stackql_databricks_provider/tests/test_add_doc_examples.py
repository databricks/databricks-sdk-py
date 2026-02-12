"""Tests for stackql_databricks_provider.add_doc_examples module."""

import json
import os
import tempfile

import pytest

from stackql_databricks_provider.add_doc_examples import (
    _inject_select_tabs,
    _resolve_doc_path,
    apply_doc_examples,
    load_examples,
)

# Minimal doc content matching the generated structure
SAMPLE_DOC = '''## `SELECT` examples
<Tabs
    defaultValue="billable_usage_download"
    values={[
        { label: 'billable_usage_download', value: 'billable_usage_download' }
    ]}
>
<TabItem value="billable_usage_download">

Returns billable usage logs in CSV format.

```sql
SELECT
contents
FROM databricks_account.billing.billable_usage
WHERE account_id = '{{ account_id }}'
AND start_month = '{{ start_month }}'
AND end_month = '{{ end_month }}'
;
```

</TabItem>
</Tabs>'''


class TestLoadExamples:
    def test_loads_from_default_path(self):
        examples = load_examples()
        assert isinstance(examples, list)
        assert len(examples) > 0

    def test_returns_empty_for_missing_file(self):
        examples = load_examples("/nonexistent/path.json")
        assert examples == []

    def test_has_billable_usage_entry(self):
        examples = load_examples()
        providers = [e["provider"] for e in examples]
        assert "databricks_account" in providers

    def test_entry_has_required_fields(self):
        examples = load_examples()
        for entry in examples:
            assert "provider" in entry
            assert "service" in entry
            assert "resource" in entry
            assert "tabs" in entry
            for tab in entry["tabs"]:
                assert "label" in tab
                assert "value" in tab
                assert "content" in tab


class TestResolveDocPath:
    def test_builds_correct_path(self):
        path = _resolve_doc_path(
            "/website", "databricks_account", "billing", "billable_usage"
        )
        assert path == (
            "/website/databricks_account/docs/services/"
            "billing/billable_usage/index.md"
        )


class TestInjectSelectTabs:
    def test_adds_tab_to_values_array(self):
        tabs = [{"label": "Export to CSV", "value": "export_csv", "content": "Example content"}]
        result = _inject_select_tabs(SAMPLE_DOC, tabs)
        assert "export_csv" in result
        assert "Export to CSV" in result

    def test_adds_tab_item_block(self):
        tabs = [{"label": "Export to CSV", "value": "export_csv", "content": "My example here"}]
        result = _inject_select_tabs(SAMPLE_DOC, tabs)
        assert '<TabItem value="export_csv">' in result
        assert "My example here" in result

    def test_preserves_existing_tab(self):
        tabs = [{"label": "Export to CSV", "value": "export_csv", "content": "New content"}]
        result = _inject_select_tabs(SAMPLE_DOC, tabs)
        assert "billable_usage_download" in result
        assert '<TabItem value="billable_usage_download">' in result
        assert "Returns billable usage logs in CSV format." in result

    def test_adds_multiple_tabs(self):
        tabs = [
            {"label": "Tab A", "value": "tab_a", "content": "Content A"},
            {"label": "Tab B", "value": "tab_b", "content": "Content B"},
        ]
        result = _inject_select_tabs(SAMPLE_DOC, tabs)
        assert "tab_a" in result
        assert "tab_b" in result
        assert "Content A" in result
        assert "Content B" in result

    def test_returns_unchanged_if_no_select_section(self):
        content = "## Some other section\nNo select examples here."
        tabs = [{"label": "Test", "value": "test", "content": "x"}]
        result = _inject_select_tabs(content, tabs)
        assert result == content

    def test_closing_tabs_preserved(self):
        tabs = [{"label": "New", "value": "new", "content": "stuff"}]
        result = _inject_select_tabs(SAMPLE_DOC, tabs)
        assert result.count("</Tabs>") == 1


class TestApplyDocExamples:
    def _setup_doc_tree(self, tmpdir, content=SAMPLE_DOC):
        """Create a minimal doc tree and return the doc dir."""
        doc_path = os.path.join(
            tmpdir, "databricks_account", "docs", "services",
            "billing", "billable_usage",
        )
        os.makedirs(doc_path)
        index_path = os.path.join(doc_path, "index.md")
        with open(index_path, "w") as f:
            f.write(content)
        return tmpdir, index_path

    def test_injects_example_into_doc(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            doc_dir, index_path = self._setup_doc_tree(tmpdir)

            config = {
                "examples": [{
                    "provider": "databricks_account",
                    "service": "billing",
                    "resource": "billable_usage",
                    "section": "select",
                    "tabs": [{
                        "label": "Export to CSV",
                        "value": "export_to_csv",
                        "content": "```bash\n./stackql exec ...\n```",
                    }],
                }]
            }
            config_path = os.path.join(tmpdir, "examples.json")
            with open(config_path, "w") as f:
                json.dump(config, f)

            summary = apply_doc_examples(doc_dir, config_path)
            assert summary["applied"] == 1

            with open(index_path) as f:
                result = f.read()
            assert "export_to_csv" in result
            assert "Export to CSV" in result
            assert "./stackql exec" in result

    def test_idempotent_on_second_run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            doc_dir, index_path = self._setup_doc_tree(tmpdir)

            config = {
                "examples": [{
                    "provider": "databricks_account",
                    "service": "billing",
                    "resource": "billable_usage",
                    "section": "select",
                    "tabs": [{
                        "label": "Export to CSV",
                        "value": "export_to_csv",
                        "content": "Example",
                    }],
                }]
            }
            config_path = os.path.join(tmpdir, "examples.json")
            with open(config_path, "w") as f:
                json.dump(config, f)

            # First run
            summary1 = apply_doc_examples(doc_dir, config_path)
            assert summary1["applied"] == 1

            # Second run should skip (already present)
            summary2 = apply_doc_examples(doc_dir, config_path)
            assert summary2["skipped"] == 1
            assert summary2["applied"] == 0

    def test_skips_missing_doc_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config = {
                "examples": [{
                    "provider": "databricks_account",
                    "service": "billing",
                    "resource": "nonexistent_resource",
                    "section": "select",
                    "tabs": [{"label": "X", "value": "x", "content": "y"}],
                }]
            }
            config_path = os.path.join(tmpdir, "examples.json")
            with open(config_path, "w") as f:
                json.dump(config, f)

            summary = apply_doc_examples(tmpdir, config_path)
            assert summary["skipped"] == 1

    def test_returns_zero_for_empty_config(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            summary = apply_doc_examples(tmpdir, "/nonexistent/config.json")
            assert summary == {"applied": 0, "skipped": 0}
