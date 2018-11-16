#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# BinderHub documentation build configuration file, created by
# sphinx-quickstart on Tue May 16 07:17:16 2017.
import os
from os.path import dirname
import sys

import alabaster_jupyterhub
import requests

# Set paths
sys.path.insert(0, os.path.abspath('.'))
docs = dirname(__file__)
print(docs)
root = dirname(docs)
print(root)
sys.path.insert(0, root)
sys.path.insert(0, os.path.join(docs, 'sphinxext'))
sys.path.insert(0, os.path.join(root, 'binderhub/'))
print(sys.path)
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.png"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'autodoc_traits',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# Support markdown via recommonmark:
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# Set the default role so we can use `foo` instead of ``foo``
default_role = 'literal'

# General information about the project.
project = 'BinderHub'
copyright = '2017, The Jupyter Team'
author = 'The Jupyter Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster_jupyterhub'
html_theme_path = [alabaster_jupyterhub.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'show_related': True,
    'description': "A project to build and serve Binders",
    'github_user': 'jupyterhub',
    'github_repo': 'binderhub',
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html'
    ]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BinderHubdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'BinderHub.tex', 'BinderHub Documentation',
     'Yuvi Panda', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'binderhub', 'BinderHub Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BinderHub', 'BinderHub Documentation',
     author, 'BinderHub', 'One line description of project.',
     'Miscellaneous'),
]

# -- Custom scripts -------------------------------------------

# Grab the latest version of the k8s and helm install instructions.
k8s_instructions = "https://raw.githubusercontent.com/jupyterhub/zero-to-jupyterhub-k8s/master/doc/source/create-k8s-cluster.rst"
helm_instructions = "https://raw.githubusercontent.com/jupyterhub/zero-to-jupyterhub-k8s/master/doc/source/setup-helm.rst"

resp = requests.get(k8s_instructions)
with open('./k8s.txt', 'w') as ff:
    ff.write(resp.text)

resp = requests.get(helm_instructions)
with open('./helm.txt', 'w') as ff:
    # Bump section headers
    lines = resp.text.split('\n')
    for ii, ln in enumerate(lines):
        if ln.startswith('---'):
            lines[ii] = ln.replace('-', '~')
    ff.write('\n'.join(lines))

# -- Add custom CSS ----------------------------------------------
def setup(app):
    app.add_stylesheet('https://gitcdn.link/repo/jupyterhub/binder/master/doc/_static/custom.css')

# -- ReadTheDocs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    html_theme = 'alabaster_jupyterhub'
    html_theme_path = [alabaster_jupyterhub.get_html_theme_path()]
