.PHONY: all \
		setup \
		lint \
		unittest \
		pytest \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv .venv

setup: ## project setup
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install wheel setuptools
	. .venv/bin/activate; pip install -r requirements.txt

lint: ## Check code quality
	. .venv/bin/activate; black ./
	. .venv/bin/activate; flake8

unittest: ## Start testing with unittest
	. .venv/bin/activate; python -m unittest

pytest: ## Start testing with pytest
	. .venv/bin/activate; pytest ./

run: ## Run
	. .venv/bin/activate; python main.py