# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "pyproject-hooks"
copyright = "2021, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    # External stuff
    "myst_parser",
]

#
# -- Options for intersphinx -------------------------------------------------
#
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pypug": ("https://packaging.python.org/", None),
}

#
# -- Options for Markdown files ----------------------------------------------
#
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
language = "en"
