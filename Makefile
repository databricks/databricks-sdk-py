dev:
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

test:
	pytest -m 'not integration' --cov=databricks --cov-report html tests

integration:
	pytest -n auto -m 'integration' --cov=databricks --cov-report html tests

coverage: test
	open htmlcov/index.html

dist:
	python3 setup.py bdist_wheel

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov