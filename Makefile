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

define pip-lock
	pip-compile --generate-hashes --allow-unsafe --extra dev --output-file $(1)/requirements-dev-lock.txt pyproject.toml
	pip-compile --generate-hashes --allow-unsafe --output-file $(1)/requirements-lock.txt pyproject.toml
endef

lock:
	$(call pip-lock,.)

check-lock:
	$(call pip-lock,/tmp)
	diff -q requirements-dev-lock.txt /tmp/requirements-dev-lock.txt || (echo "requirements-dev-lock.txt is out of date - run 'make lock'" && exit 1)
	diff -q requirements-lock.txt /tmp/requirements-lock.txt || (echo "requirements-lock.txt is out of date - run 'make lock'" && exit 1)

clean:
	rm -fr dist *.egg-info .pytest_cache build htmlcov
