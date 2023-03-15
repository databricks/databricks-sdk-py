dev-init:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install .
	pip install '.[dev]'

fmt:
	yapf -pri databricks tests
	autoflake -ri databricks tests
	isort databricks tests

lint:
	pycodestyle databricks
	autoflake --check-diff --quiet --recursive databricks

