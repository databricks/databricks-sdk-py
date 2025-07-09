# Detect Python version from the system
PYTHON_VERSION := $(shell python3 -c 'import sys; print(f"{sys.version_info.major}{sys.version_info.minor}")')

# Generate requirements filename based on Python version
REQUIREMENTS_FILE = requirements-dev-py$(PYTHON_VERSION).txt

# Testing workflow:
# 1. GitHub Actions runs tests for each Python version (3.8-3.12) on multiple OSes
# 2. For each Python version, tests run in two modes:
#    - 'latest': Uses dependencies directly from pyproject.toml
#    - 'frozen': Uses version-specific requirements-dev-pyXY.txt
# 3. Each Python version gets its own virtual environment (.venvXY)
# 4. Tests are only blocking in `frozen` mode. Tests run in `latest` mode are
#    allowed to fail and serve as a warning that there may have been a breaking
#    change in a dependency.
# 5. To run tests locally:
#    - make dev test    # uses frozen dependencies
#    - make dev-latest test  # uses latest dependencies
#
# To update dependencies for all Python versions using pyenv:
# rm -rf .venv* requirements-dev-py*.txt
# for v in 3.8 3.9 3.10 3.11 3.12 3.13; do
#  pyenv local $v
#  make dev-env update-dev-dep-lockfile
# done

dev-env:
	python -m venv .venv$(PYTHON_VERSION)
ifeq ($(OS), Windows_NT)
	.venv$(PYTHON_VERSION)\Scripts\activate
else
	. .venv$(PYTHON_VERSION)/bin/activate
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
