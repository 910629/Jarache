import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))  # Add project root to path
os.environ['DJANGO_SETTINGS_MODULE'] = 'Jarache.settings'  # Set Django settings
django.setup()

# Sphinx configuration options
project = 'Jarache'
copyright = '2024, Your Name'
author = 'Jarache Khunyeli'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

