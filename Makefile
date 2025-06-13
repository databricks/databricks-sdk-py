# Default Python version if not specified
# This is expected to have the form X.Y.
# The corresponding requirements file is requirements-dev-pyXY.txt.
PYTHON_VERSION ?= 3.13
PYTHON_VERSION_NO_DOTS = $(subst .,,$(PYTHON_VERSION))

# Generate requirements filename based on Python version
REQUIREMENTS_FILE = requirements-dev-py$(PYTHON_VERSION_NO_DOTS).txt

dev-env:
	python -m venv .venv$(PYTHON_VERSION_NO_DOTS)
ifeq ($(OS), Windows_NT)
	.venv$(PYTHON_VERSION_NO_DOTS)\Scripts\activate
else
	. .venv$(PYTHON_VERSION_NO_DOTS)/bin/activate
endif

dev: dev-env
	# Install all dependencies from the version-specific requirements file
	# Regenerate this file with `make update-dev-dep-lockfile PYTHON_VERSION=X.Y`
	pip install -r $(REQUIREMENTS_FILE)

dev-latest: dev-env
	# Install all dependencies from the pyproject.toml file
	pip install '.[dev]'

install-pip-tools:
	pip install pip-tools

update-dev-dep-lockfile: install-pip-tools
	pip-compile pyproject.toml --extra dev --output-file $(REQUIREMENTS_FILE)

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
