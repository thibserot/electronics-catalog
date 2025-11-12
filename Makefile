# Makefile for electronics-catalog
# Key targets:
#   make registry_stickers  # generate registry YAML + registry page + stickers/QR
#   make serve              # build, then mkdocs serve
#   make publish            # build, then mkdocs gh-deploy --force
#   make precommit-install  # install a git pre-commit hook to run registry_stickers

PY ?= python
MKDOCS ?= mkdocs

.PHONY: all serve publish build registry stickers registry_stickers clean precommit-install

all: serve

# Back-compat alias
build: registry_stickers

# Explicit combined target requested for pre-commit
registry_stickers: registry stickers

registry:
	$(PY) scripts/generate_id_registry.py
	$(PY) scripts/build_registry_page.py

stickers:
	$(PY) scripts/build_labels.py

serve: registry_stickers
	$(MKDOCS) serve

publish: registry_stickers
	$(MKDOCS) gh-deploy --force

clean:
	rm -f docs/components/stickers/id_registry.yaml
	rm -f docs/components/stickers/id_registry_simple.yaml

# Install a lightweight git pre-commit hook that runs `make registry_stickers`
precommit-install:
	./scripts/install-git-hooks.sh
