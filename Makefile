dev:
	uv sync --locked --extra dev

install:
	uv sync --locked

fmt:
	uv run black databricks tests
	uv run autoflake -ri databricks tests
	uv run isort databricks tests

fmte:
	uv run black examples
	uv run autoflake -ri examples
	uv run isort examples

lint:
	uv run pycodestyle databricks
	uv run autoflake --check-diff --quiet --recursive databricks

test:
	uv run pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

integration:
	uv run pytest -n auto -m 'integration and not benchmark' --reruns 4 --dist loadgroup --cov=databricks --cov-report html tests

benchmark:
	uv run pytest -m 'benchmark' tests

coverage: test
	open htmlcov/index.html

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov .venv
