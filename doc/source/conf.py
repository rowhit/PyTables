# -*- coding: utf-8 -*-
#
# PyTables documentation build configuration file, created by
# sphinx-quickstart on Sun Feb  7 22:29:49 2010.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown
# here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'IPython.sphinxext.ipython_console_highlighting',
    'numpydoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyTables'
copyright = '2011-2016, PyTables maintainers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
VERSION = open('../../VERSION').read().strip()
version = VERSION

# The full version, including alpha/beta/rc tags.
release = VERSION

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
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
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


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
}

# Add any paths that contain custom themes here, relative to this directory.
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo-pytables-small.png'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '\usepackage{bookmark,hyperref}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('usersguide/usersguide', 'usersguide-%s.tex' % version,
   u'PyTables User Guide', u'PyTables maintainers', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'usersguide/images/pytables-front-logo.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = [
#    'usersguide/datatypes',
#    'usersguide/condition_syntax',
#    'usersguide/parameter_files',
#    'usersguide/nested_rec_arrays',
#    'usersguide/utilities',
#    'usersguide/file_format',
#    'usersguide/bibliography',
#]

# If false, no module index is generated.
latex_domain_indices = False

# -- Options for autodocumentation ---------------------------------------------
autodoc_member_order = "groupwise"
autoclass_content = "class"
autosummary_generate = []



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'PyTables'
epub_author = 'PyTables maintainers'
epub_publisher = 'PyTables maintainers'
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'PyTables'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# -- Intersphinx options ----------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}

# -- External link options ----------------------------------------------------
extlinks = {
    'issue': ('https://github.com/PyTables/PyTables/issues/%s', 'gh-'),
    'irc': ('http://pytables.github.io/irc/%s.html', ''),
}
