dev:
	uv sync --locked --extra dev

install:
	uv sync --locked

fmt:
	uv run ruff format databricks tests

fmte:
	uv run ruff format examples

lint:
	uv run ruff check databricks
	uv run ruff format --check databricks

test:
	uv run pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

integration:
	uv run pytest -n auto -m 'integration and not benchmark' --reruns 4 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	uv run pytest -m 'benchmark' tests

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
