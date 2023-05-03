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

lint:
	pycodestyle databricks
	autoflake --check-diff --quiet --recursive databricks

# need to do mypy --install-types
mypy:
	@mypy --namespace-packages \
		--config-file mypy.ini \
		--cache-dir /tmp/.mypy_cache \
		databricks

test:
	pytest -m 'not integration' --cov=databricks --cov-report html tests

integration:
	pytest -n auto -m 'integration' --cov=databricks --cov-report html tests

coverage: test
	open htmlcov/index.html

dist:
	python3 setup.py bdist_wheel sdist

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
