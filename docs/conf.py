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
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "HPC Documentation"
logo = "_static/logo-square.png"
copyright = "2023"
author = "Research Computing, Northeastern University"

# The full version, including alpha/beta/rc tags
release = "2.0.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",  # https://pypi.org/project/sphinx_design/
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",  # https://sphinx-togglebutton.readthedocs.io/en/latest/use.html
    # "sphinxcontrib.bibtex",
    # "sphinxext.opengraph",
    # For the kitchen sink
    "sphinx.ext.todo",
    'sphinx.ext.autosectionlabel',
]

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["first_steps/cps_ood.md",
                    "using-discovery/bash.md",
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
html_static_path = ["_static",
                    "_static/video"]

master_doc = "index.md"
source_suffix = [".rst", ".md"]
