dev:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install '.[dev]'

install:
	pip install .

fmt:
	yapf -pri databricks tests
	autoflake -ri databricks tests
	isort databricks tests

fmte:
	yapf -pri examples
	autoflake -ri examples
	isort examples

lint:
	pycodestyle databricks
	autoflake --check-diff --quiet --recursive databricks

test:
	pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

integration:
	pytest -n auto -m 'integration and not benchmark' --reruns 2 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

dist:
	python3 setup.py bdist_wheel sdist

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
