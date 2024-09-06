SHELL = bash

format:
	ruff format main.py

run:
	poetry run python main.py
