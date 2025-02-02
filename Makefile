build:
	uv run build

package-install:
	uv tool install dist/*.whl

install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff

test-coverage:
	uv run pytest --cov --cov-report xml:coverage.xml

.PHONY: install test lint selfcheck check build