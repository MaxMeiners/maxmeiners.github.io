import sphinx_rtd_theme
import os
import sys

# Add the path to the folder containing your Python source code files
sys.path.insert(0, os.path.abspath('../deliverables/'))
sys.path.insert(1, os.path.abspath('../deliverables/pages/'))
sys.path.insert(2, os.path.abspath('../deliverables/machine_learning/'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'group10'
copyright = '2023, Max Meiners, Michal Dziechciarz, Isa van der Mierde, Marwa Rouah'
author = 'Max Meiners, Michal Dziechciarz, Isa van der Mierde, Marwa Rouah'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   'sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
