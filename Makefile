dev-init:
	python3 -m venv .databricks
	.venv/bin/pip install .
	.venv/bin/pip install '.[dev]'

fmt:
	yapf -pri databricks tests
	autoflake -ri databricks tests

lint:
	pycodestyle databricks
	autoflake --check-diff --quiet --recursive databricks

