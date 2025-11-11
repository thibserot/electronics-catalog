# Simple Makefile for electronics-catalog
# Usage:
#   make serve   # build registry + stickers, then mkdocs serve
#   make publish # build registry + stickers, then mkdocs gh-deploy --force

PY ?= python
MKDOCS ?= mkdocs

.PHONY: all serve publish build registry stickers clean

all: serve

build: registry stickers

registry:
	$(PY) scripts/generate_id_registry.py
	$(PY) scripts/build_registry_page.py

stickers:
	$(PY) scripts/build_labels.py

serve: build
	$(MKDOCS) serve

publish: build
	$(MKDOCS) gh-deploy --force

clean:
	rm -f docs/components/stickers/id_registry.yaml
	rm -f docs/components/stickers/id_registry_simple.yaml
