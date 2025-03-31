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
	black databricks tests
	autoflake -ri databricks tests
	isort databricks tests

fmte:
	black examples
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

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
