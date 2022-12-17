dev-init:
	python3 -m venv .databricks
	.venv/bin/pip install .
	.venv/bin/pip install '.[dev]'

fmt:
	yapf -pri databricks

lint:
	pycodestyle databricks

