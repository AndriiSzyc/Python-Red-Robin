.PHONY: all \
		setup \
		lint \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv .venv

setup: ## project setup
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install jupyterlab
	. .venv/bin/activate; pip install wheel setuptools
