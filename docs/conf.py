# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime as dt

project = 'grid4earth tools inventory'
author = 'grid4earth project'
year = dt.datetime.today().year
copyright = f'{year}, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "myst_nb",
    "sphinx_codeautolink",
    "sphinx_copybutton",
    "sphinx_remove_toctrees",
    "sphinxext.opengraph",
    "sphinx_design",
]

autodoc_typehints = "none"
codeautolink_concat_default = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {".rst": "restructuredtext",
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}
root_doc = "index"
language = "en"

remove_from_toctrees = ["generated/*"]

# Myst_nb options
nb_execution_raise_on_error = True
nb_execution_mode = "cache"
nb_execution_show_tb = True
nb_remove_cell_tags = ["remove-cell"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "igor"

ogp_site_url = "https://xarray-indexes.readthedocs.io/"

# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_book_theme"
# html_logo = "Xarray.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
css_vars = {
    "admonition-font-size": "0.9rem",
    "font-size--small": "92%",
    "font-size--small--2": "87.5%",
}

html_context = {
    "github_user": "EOPF-DGGS",
    "github_repo": "tools-inventory",
    "github_version": "main",
    "doc_path": "docs",
}
html_theme_options = {
    "use_edit_page_button": True,
}
html_static_path = ["_static"]
html_css_files = ["style.css"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "xarray": ("https://docs.xarray.dev/en/latest/", None),
    "rasterix": ("https://rasterix.readthedocs.io/en/latest/", None),
    "shapely": ("https://shapely.readthedocs.io/en/latest/", None),
    "xvec": ("https://xvec.readthedocs.io/en/stable/", None),
    "xdggs": ("https://xdggs.readthedocs.io/en/latest/", None),
    "geopandas": ("https://geopandas.org/en/stable/", None),
    "pint-xarray": ("https://pint-xarray.readthedocs.io/en/latest/", None),
    "pint": ("https://pint.readthedocs.io/en/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "astropy": ("https://docs.astropy.org/en/latest/", None),
}
