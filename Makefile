dev-init:
	python3 -m venv .venv
	.venv/bin/pip install .
	.venv/bin/pip install '.[dev]'