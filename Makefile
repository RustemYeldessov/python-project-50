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
.PHONY: install test lint selfcheck check build