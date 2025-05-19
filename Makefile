# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
# SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# %: Makefile
# 	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


.PHONY: build-playground
build-playground: check-jq
	@echo "Building playground..."
	rm -rf public/lite && \
	jupyter lite build && \
    WHL_FILE=$$(ls pypi | grep .whl) ;\
	python tools/patch_jlite_json.py \
	  public/lite/jupyter-lite.json \
	  --whl-url "pypi/$$WHL_FILE" && \
	cp -frpv pyodide public/lite/ && \
	cp -frpv pypi public/lite/extensions/@jupyterlite/pyodide-kernel-extension/static/



.PHONY: wheel
wheel: clean-wheel
	$(VENV_PATH)/bin/python -m build


.PHONY: clean-wheel
clean-wheel:
	rm -rf public/lite

.PHONY: clean-playground
clean-playground:
	rm -rf public/lite

.PHONY: check-jq
check-jq:
	which jq || (echo "jq is not installed. Please install jq to continue." && exit 1)
