UV_SYNC_FLAGS ?= --locked
UV_RUN_FLAGS ?=

dev:
	uv sync $(UV_SYNC_FLAGS) --extra dev

install:
	uv sync $(UV_SYNC_FLAGS)

fmt:
	uv run $(UV_RUN_FLAGS) black databricks tests
	uv run $(UV_RUN_FLAGS) autoflake -ri databricks tests
	uv run $(UV_RUN_FLAGS) isort databricks tests

fmte:
	uv run $(UV_RUN_FLAGS) black examples
	uv run $(UV_RUN_FLAGS) autoflake -ri examples
	uv run $(UV_RUN_FLAGS) isort examples

lint:
	uv run $(UV_RUN_FLAGS) pycodestyle databricks
	uv run $(UV_RUN_FLAGS) autoflake --check-diff --quiet --recursive databricks

test:
	uv run $(UV_RUN_FLAGS) pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

integration:
	uv run $(UV_RUN_FLAGS) pytest -n auto -m 'integration and not benchmark' --reruns 4 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	uv run $(UV_RUN_FLAGS) pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

fix-lockfile:
	@# Replace JFrog proxy URLs with public equivalents in lockfiles.
	@# Prevents proxy URLs from being accidentally committed.
	find . -type f -name '*.lock' -not -path './.github/*' \
	  -exec sed -i 's|databricks\.jfrog\.io/artifactory/api/pypi/db-pypi/simple|pypi.org/simple|g' {} +
	find . -type f -name '*.lock' -not -path './.github/*' \
	  -exec sed -i 's|databricks\.jfrog\.io/artifactory/api/pypi/db-pypi/packages|files.pythonhosted.org|g' {} +

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov .venv
