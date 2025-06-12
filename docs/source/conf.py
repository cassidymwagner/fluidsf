# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../../src"))

# import mock

# MOCK_MODULES = ['numpy', 'matplotlib', 'pandas']
# for mod_name in MOCK_MODULES:
#     sys.modules[mod_name] = mock.Mock()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "FluidSF"
copyright = "2024, Cassidy Wagner"  # noqa: A001
author = "Cassidy Wagner"
release = "0.2.0"
html_title = "FluidSF"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "nbsphinx",
]
templates_path = ["_templates"]
exclude_patterns = ["tests/test_*", "test_*"]

# autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
# html_static_path = ["./build/html/_static"]

# -- Intersphinx mapping --
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# -- Matplotlib configuration --
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'png'}",
    "--InlineBackend.rc={'figure.dpi': 200}",
]

