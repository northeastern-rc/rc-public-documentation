# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
from datetime import date

# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "RC-HPC"
# logo = "_static/logo-square.png"
copyright = f"{date.today().year}, Andrey Petrov"
author = "Research Computing, NU"

# The full version, including alpha/beta/rc tags
release = "3.0.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "myst_nb",
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",  # https://pypi.org/project/sphinx_design/
    # "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    # https://sphinx-togglebutton.readthedocs.io/en/latest/use.html
    # "sphinxcontrib.bibtex",
    # "sphinxext.opengraph",
    # For the kitchen sink
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True

intersphinx_mapping = {"python": ("https://docs.python.org/3", None),
                       "sphinx": ("https://www.sphinx-doc.org/en/master", None)}

# -- Options for TODOs -------------------------------------------------------
#
todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]
myst_heading_anchors = 3
myst_deflist_enable = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["using-ood/cps_ood.md",
                    "_snippets/*"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# add logo to the upper left in the help system
html_logo = "_static/logo-square.png"
html_theme_options = {
    "show_toc_level": 2,
    "repository_url": "https://github.com/northeastern-rc/rc-public-documentation",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
}

# custom css file
html_css_files = ["../css/custom.css"]

# If true, “(C) Copyright …” is shown in the HTML footer. Default is True.
html_show_copyright = True
# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_static/video"]

master_doc = "index"
source_suffix = [".rst", ".md"]

# Warn about all references to unknown targets
nitpicky = True
