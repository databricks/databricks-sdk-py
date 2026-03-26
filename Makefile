dev:
	python3 -m venv .venv
ifeq ($(OS), Windows_NT)
	.venv\Scripts\activate
else
	. .venv/bin/activate
endif
ifeq ($(CI),true)
	pip install --require-hashes -r requirements-dev-lock.txt
	pip install --no-deps .
else
	pip install '.[dev]'
endif

install:
ifeq ($(CI),true)
	pip install --require-hashes -r requirements-lock.txt
	pip install --no-deps .
else
	pip install .
endif

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
	pytest -n auto -m 'integration and not benchmark' --reruns 4 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
