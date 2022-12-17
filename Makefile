dev-init:
	python3 -m venv .databricks
	.venv/bin/pip install .
	.venv/bin/pip install '.[dev]'

fmt:
	yapf -pri databricks
	autoflake -ri databricks

lint:
	pycodestyle databricks
	autoflake --check-diff --quiet --recursive databricks

