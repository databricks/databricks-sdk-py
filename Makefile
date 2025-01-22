.PHONY: dev
dev: ## Create virtual environment and install development dependencies.
	@echo "Creating virtual environment..."
	@python3 -m venv .venv
	@echo "Activating virtual environment..."
ifeq ($(OS), Windows_NT)
	.venv\Scripts\activate
else
	. .venv/bin/activate
endif
	@echo "Installing development dependencies..."
	@pip install '.[dev]'

.PHONY: install
install: ## Install the package.
	@echo "Installing the package..."
	@pip install .

.PHONY: fmt
fmt: ## Format the code in 'databricks' and 'tests' directories.
	@echo "Formatting code..."
	@yapf -pri databricks tests
	@autoflake -ri databricks tests
	@isort databricks tests

.PHONY: fmte
fmte: ## Format the code in 'examples' directory.
	@echo "Formatting examples..."
	@yapf -pri examples
	@autoflake -ri examples
	@isort examples

.PHONY: lint
lint: ## Lint the code in 'databricks' directory.
	@echo "Linting code..."
	@pycodestyle databricks
	@autoflake --check-diff --quiet --recursive databricks

.PHONY: test
test: ## Run unit tests.
	@echo "Running unit tests..."
	@pytest -m 'not integration and not benchmark' --cov=databricks --cov-report html tests

.PHONY: integration
integration: ## Run integration tests.
	@echo "Running integration tests..."
	@pytest -n auto -m 'integration and not benchmark' --reruns 2 --dist loadgroup --cov=databricks --cov-report html tests

.PHONY: benchmark
benchmark: ## Run benchmark tests.
	@echo "Running benchmark tests..."
	@pytest -m 'benchmark' tests

.PHONY: coverage
coverage: test ## Generate and open the coverage report.
	@echo "Opening coverage report..."
	@open htmlcov/index.html

.PHONY: dist
dist: ## Build distribution packages.
	@echo "Building distribution packages..."
	@python3 setup.py bdist_wheel sdist

.PHONY: clean
clean: ## Clean up build artifacts.
	@echo "Cleaning up build artifacts..."
	@rm -fr dist *.egg-info .pytest_cache build htmlcov

.PHONY: help
help: ## Show help for the commands.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
