ifeq ($(OS), Windows_NT)
	VENV_BIN = .venv/Scripts
else
	VENV_BIN = .venv/bin
endif

dev:
	python3 -m venv .venv
	$(VENV_BIN)/pip install '.[dev]'

install:
	$(VENV_BIN)/pip install .

fmt:
	$(VENV_BIN)/black databricks tests
	$(VENV_BIN)/autoflake -ri databricks tests
	$(VENV_BIN)/isort databricks tests

fmte:
	$(VENV_BIN)/black examples
	$(VENV_BIN)/autoflake -ri examples
	$(VENV_BIN)/isort examples

lint:
	$(VENV_BIN)/pycodestyle databricks
	$(VENV_BIN)/autoflake --check-diff --quiet --recursive databricks

test:
	$(VENV_BIN)/pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

integration:
	$(VENV_BIN)/pytest -n auto -m 'integration and not benchmark' --reruns 2 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	$(VENV_BIN)/pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov .venv
