# -*- coding: utf-8 -*-
#
# Bio-Formats documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 29 15:42:49 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import re
import subprocess
from datetime import datetime

def popen(args, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
        copy = os.environ.copy()
        shell = (sys.platform == "win32")
        return subprocess.Popen(args,
                env=copy,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr,
                shell=shell)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.)
extensions = ['sphinx.ext.extlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bio-Formats'
title = u'%s Documentation' % project
author = u'The Open Microscopy Environment'
now = datetime.now()
copyright = u'2000-%d, %s ' % (now.year, author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
try:
    if "BF_RELEASE" in os.environ:
        release = os.environ.get('BF_RELEASE')
    else:
        p = popen(['git','describe'])
        tag = p.communicate()
        split_tag = re.split("^(v)?(.*?)(-[0-9]+)?((-)g(.*?))?$",tag[0])
        # The full version, including alpha/beta/rc tags.
        release = split_tag[2]
    split_release =  re.split("^([0-9]\.[0-9])(\.[0-9]+)(.*?)$",release)
    # The short X.Y version.
    version = split_release[1]
except:
    version = 'UNKNOWN'
    release = 'UNKNOWN'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# Variables used to define Jenkins extlinks
if "JENKINS_JOB" in os.environ:
    jenkins_job = os.environ.get('JENKINS_JOB')
else:
    jenkins_job = 'BIOFORMATS-trunk'

jenkins_root = 'http://hudson.openmicroscopy.org.uk'
jenkins_job_root = jenkins_root + '/job'
bf_job_root = jenkins_job_root + '/' + jenkins_job
daily_job_root = jenkins_job_root + '/BIOFORMATS-daily'
trunk_artifact_root = bf_job_root + '/lastSuccessfulBuild/artifact/artifacts'
daily_artifact_root = daily_job_root + '/lastSuccessfulBuild/artifact/artifacts'

# Variables used to define other extlinks
cvs_root = 'http://cvs.openmicroscopy.org.uk'
oo_root = 'http://www.openmicroscopy.org'
oo_site_root = oo_root + '/site'
doc_root = oo_site_root + '/support/bio-formats4'
downloads_root = 'http://downloads.openmicroscopy.org'
bf_downloads_root = downloads_root + '/bio-formats'
bf_artifacts_root = bf_downloads_root + '/' + release

extlinks = {
    'downloads': (bf_downloads_root + '/%s', ''),
    'artifact': (bf_artifacts_root + '/%s', ''),
    'trunk_artifact': (trunk_artifact_root + '/%s', ''),
    'daily_artifact': (daily_artifact_root + '/%s', ''),
    'html_doc': (doc_root + '/%s', ''),
    'pdf_artifact': (bf_artifacts_root + '/Bio-Formats-' + release +'.pdf%s', ''),
    }

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = { '**' : [] }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bio-Formatsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'classoptions': ',oneside',
    'pointsize': '10pt',
    'inputenc': '%% Unused',
    'utf8extra': '%% Unused',
    'fontenc' : '%% Unused',
    'fontpkg': '%% Unused',
    'babel': '%% Unused',
    'printindex': '''\\phantomsection
\\addcontentsline{toc}{part}{\indexname}
\\printindex''',
    'preamble': '''
\input{../../preamble.tex}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
target = project + '-' + release + '.tex'
latex_documents = [
  (master_doc, target, title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "images/bio-formats-logo.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'OMERO', title, author, 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, project, title, author, 'omedocs', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore = ['http://www.openmicroscopy.org/site/support/faq',]

import urllib
brokenfiles_url = 'https://raw.github.com/openmicroscopy/sphinx-ignore-links/master/broken_links.txt'
linkcheck_ignore.extend(urllib.urlopen(brokenfiles_url).read().splitlines())
