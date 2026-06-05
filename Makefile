SHELL = bash

format:
	uv run ruff format main.py

run:
	uv run python main.py

download-model:
	wget 'https://zenodo.org/record/3234051/files/embeddings-l-model.bin?download=1' -O resources/embeddings-l-model.bin
