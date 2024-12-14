.PHONY: clean clean-build clean-pyc clean-test install dependencies uninstall models model_local_install

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test:
	pytest

install-dev:
	pip install -e .[dev]

run-dev:
	rephrasinator

install: clean
	pip install .

uninstall: clean
	pip uninstall rephrasinator -y

run: install
	rephrasinator --help

demo: install
	rephrasinator text "Ollama can run with GPU acceleration inside Docker containers for Nvidia GPUs." --model "llama3.2:3b" --additional_request "Make the new sentences angry"

models: install
	rephrasinator list-models

model_local_install:
	ollama pull phi3:14b
	ollama pull llama3.3:70b
	ollama pull llama3.2:1b
	ollama pull llama3.2:3b
	ollama pull mistral:7b
	ollama pull gemma:7b
