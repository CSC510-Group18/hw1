# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))  # Set root of our project

project = "hw01"
copyright = "2025, Jeff Powell, Zeiad Yakout, Jakub Jon"
author = "Jeff Powell, Zeiad Yakout, Jakub Jon"
release = "2025"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Enable autodoc
    "sphinx.ext.viewcode",  # Optional: Add links to source code
    "sphinx.ext.napoleon",  # Optional: Support for Google-style or NumPy-style docstrings
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_static_path = ["_static"]
