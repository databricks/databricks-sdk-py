dev:
	python3 -m venv .venv
ifeq ($(OS), Windows_NT)
	.venv\Scripts\activate
else
	. .venv/bin/activate
endif
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

PYTEST_CONCURRENCY ?= auto
integration:
	pytest -n $(PYTEST_CONCURRENCY) -m 'integration and not benchmark' --reruns 2 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
