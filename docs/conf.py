# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

about = {}
with open("../sec_edgar_downloader/_version.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

# -- Project information -----------------------------------------------------

project = "sec-edgar-downloader"
copyright = "2019, Jad Chaar"
author = "Jad Chaar"

release = about["__version__"]

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc"]

autodoc_member_order = "bysource"

master_doc = "index"
source_suffix = {".rst": "restructuredtext"}

html_sidebars = {
    "**": ["about.html", "localtoc.html", "relations.html", "searchbox.html"]
}

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_theme_options = {
    "description": "Download SEC filings with ease.",
    "github_user": "jadchaar",
    "github_repo": "sec-edgar-downloader",
    "github_banner": True,
    "show_related": False,
    "show_powered_by": False,
}

html_static_path = []

html_show_sourcelink = False
html_show_copyright = True
html_show_sphinx = False
