.PHONY: help setup test run clean lint autofix

# Display available commands
help:
	@echo "Available commands:"
	@echo "  setup    - set up the project environment"
	@echo "  test     - run unit tests"
	@echo "  run      - run application, train models, predict on test data"
	@echo "  clean    - clean up build artifacts"
	@echo "  lint     - run linters on code"
	@echo "  autofix  - automatically fix some linting issues using autopep8"

# Set up the project environment using Pipenv
setup:
	pipenv install --dev

# Run unit tests
test:
	pipenv run pytest

# Train models
run:
	pipenv run python3 main.py 

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf workspace.egg-info/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Run linters on code
lint:
	pipenv run flake8 src/

# Automatically fix some linting issues using autopep8
autofix:
	pipenv run autopep8 --in-place --recursive --max-line-length 79 src/
