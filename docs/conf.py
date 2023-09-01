# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Databricks SDK for Python'
copyright = '2023, Databricks'
author = 'Serge Smertin'
release = 'alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'myst_parser', # pip install myst-parser
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['images']
html_theme_options = {
    'logo': 'databricks-logo.svg',
    'github_user': 'databricks',
    'github_repo': 'databricks-sdk-py',
    'description': 'Databricks SDK for Python',
    'fixed_sidebar': 'true',
    'logo_text_align': 'center',
    'github_button': 'true',
    'show_related': 'true',
    'sidebar_collapse': 'true',
}
