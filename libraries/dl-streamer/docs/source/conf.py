# ==============================================================================
# Copyright (C) 2025 Intel Corporation
#
# SPDX-License-Identifier: MIT
# ==============================================================================

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

doxyrest_sphinx_dir = os.getenv("DOXYREST_SPHINX_DIR", "")
if doxyrest_sphinx_dir:
    sys.path.insert(0, os.path.abspath(doxyrest_sphinx_dir))


# -- Project information -----------------------------------------------------

project = 'Intel® Deep Learning Streamer (Intel® DL Streamer)'
copyright = '2025, Intel Corporation'
author = 'Intel Corporation'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['m2r2', 'sphinx.ext.graphviz', 'sphinxcontrib.mermaid', 'sphinxcontrib.spelling', 'sphinx_copybutton', 'sphinx_tabs.tabs']
if doxyrest_sphinx_dir:
    extensions.extend(['doxyrest', 'cpplexer'])

source_suffix = ['.rst', '.md']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for SPELLING check ---------------------------------------------------

# Dictionary selected
spelling_lang='en_US'

# Path of file containing a list of words known to be spelled correctly but that
# do not appear in the language dictionary selected
spelling_word_list_filename='spelling_wordlist.txt'

# Enable suggestions for misspelled words
spelling_show_suggestions=True

# -- Options for LINK check ---------------------------------------------------

# Enable anchors check
linkcheck_anchors=False
linkcheck_ignore = [
    r'https://www.intel.com/.*',
    r'https://*.intel.com/.*'
]
