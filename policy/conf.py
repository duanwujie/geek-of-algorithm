#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Debian Policy Manual documentation build configuration file, created by
# sphinx-quickstart on Tue Aug  8 07:14:47 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os
import sphinx

# Get Sphinx version
major, minor, patch = sphinx.version_info[:3]

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u''
copyright = 'dhacklove@163.com'
author = 'duanwujie'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2.0.0'
# The full version, including alpha/beta/rc tags.
release = '0.2.0.0'

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
#
#html_theme = 'nature'
html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Override the title to remove the unnecessary "documentation" suffix.
html_title = u""

# Suppress the copyright notice.
html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
# html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'policy'

#'classoptions': ',english,openany,oneside,toc=flat',
# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        'papersize': 'a4paper',
        # The font size ('10pt', '11pt' or '12pt').
        'pointsize': '8pt',
        
        'classoptions': ',english,openany,oneside,listof=flat,toc=flat',
        'babel': '\usepackage[english]{babel}',
        'inputenc': '',
        'utf8extra': '',
        
# Additional stuff for the LaTeX preamble.
        'preamble': '''
        % Use some font with UTF-8 support with XeLaTeX
            \\usepackage{fontspec}
            \\usepackage{xeCJK}
            \\usepackage{pdfpages} 
	    \\usepackage{indentfirst}
            \\setlength{\parindent}{2em}
            \\usepackage{fancyhdr}
            \\setsansfont{Source Code Pro}
            \\setromanfont{Source Code Pro}
            \\setmonofont{Source Code Pro}            
            \\setCJKmainfont{SimSun}
            \\setCJKsansfont{SimSun}    
            \\usepackage[titles]{tocloft}
            \\renewcommand{\\cftdot}{$\\cdot$}
            \\renewcommand{\\cftdotsep}{1.5}
            \\setlength{\\cftbeforechapskip}{10pt}
            
            \\renewcommand{\\cftchapleader}{\\cftdotfill{\\cftchapdotsep}}
            \\renewcommand{\\cftchapdotsep}{\\cftdotsep}
            \\makeatletter
            \\renewcommand{\\numberline}[1]{%
            \\settowidth\\@tempdimb{#1\\hspace{0.5em}}%
            \\ifdim\\@tempdima<\\@tempdimb%
              \\@tempdima=\\@tempdimb%
            \\fi%
            \\hb@xt@\@tempdima{\\@cftbsnum #1\\@cftasnum\\hfil}\\@cftasnumb}
            \\makeatother


            
         '''
}

#          \\usepackage{fancyhdr}
#          \\pagestyle{fancyplain}
#          \\fancyhead[LE]{\\fancyplain{}{\\bfseries\\thepage}}
#          \\fancyhead[CE]{\\fancyplain{}{}}
#          \\fancyhead[RE]{\\fancyplain{}{\\bfseries\\leftmark}}
#          \\fancyhead[LO]{\\fancyplain{}{\\bfseries\\rightmark}}
#          \\fancyhead[CO]{\\fancyplain{}{}}
#          \\fancyhead[RO]{\\fancyplain{}{\\bfseries\\thepage}}
#          \\fancyfoot[LE]{\\fancyplain{}{}}
#          \\fancyfoot[CE]{\\fancyplain{}{}}
#          \\fancyfoot[RE]{\\fancyplain{}{\\includegraphics[scale=0.2]{logo.png}}}
#          \\fancyfoot[LO]{\\fancyplain{}{\\includegraphics[scale=0.2]{logo.png}}}
#          \\fancyfoot[CO]{\\fancyplain{}{}}
#          \\fancyfoot[RO]{\\fancyplain{}{}}

# Fix reference escape troubles with Sphinx 1.4.x
if major == 1 and minor > 3:
    latex_elements['preamble']  += '\\renewcommand*{\\DUrole}[2]{ #2 }\n'

if major == 1 and minor <= 4:
    latex_elements['preamble']  += '\\usepackage[margin=0.5in, top=1in, bottom=1in]{geometry}'
elif major == 1 and (minor > 5 or (minor == 5 and patch >= 3)):
    latex_elements['sphinxsetup'] = 'hmargin=0.5in, vmargin=1in'
    latex_elements['preamble']  += '\\fvset{fontsize=auto}\n'

# Customize notice background colors on Sphinx < 1.6:
if major == 1 and minor < 6:
   latex_elements['preamble']  += '''
        \\usepackage{ifthen}

        % Put notes in color and let them be inside a table
    \\definecolor{NoteColor}{RGB}{204,255,255}
    \\definecolor{WarningColor}{RGB}{255,204,204}
    \\definecolor{AttentionColor}{RGB}{255,255,204}
    \\definecolor{ImportantColor}{RGB}{192,255,204}
    \\definecolor{OtherColor}{RGB}{204,204,204}
        \\newlength{\\mynoticelength}
        \\makeatletter\\newenvironment{coloredbox}[1]{%
       \\setlength{\\fboxrule}{1pt}
       \\setlength{\\fboxsep}{7pt}
       \\setlength{\\mynoticelength}{\\linewidth}
       \\addtolength{\\mynoticelength}{-2\\fboxsep}
       \\addtolength{\\mynoticelength}{-2\\fboxrule}
           \\begin{lrbox}{\\@tempboxa}\\begin{minipage}{\\mynoticelength}}{\\end{minipage}\\end{lrbox}%
       \\ifthenelse%
          {\\equal{\\py@noticetype}{note}}%
          {\\colorbox{NoteColor}{\\usebox{\\@tempboxa}}}%
          {%
             \\ifthenelse%
             {\\equal{\\py@noticetype}{warning}}%
             {\\colorbox{WarningColor}{\\usebox{\\@tempboxa}}}%
         {%
                \\ifthenelse%
                {\\equal{\\py@noticetype}{attention}}%
                {\\colorbox{AttentionColor}{\\usebox{\\@tempboxa}}}%
            {%
                   \\ifthenelse%
                   {\\equal{\\py@noticetype}{important}}%
                   {\\colorbox{ImportantColor}{\\usebox{\\@tempboxa}}}%
                   {\\colorbox{OtherColor}{\\usebox{\\@tempboxa}}}%
            }%
         }%
          }%
        }\\makeatother

        \\makeatletter
        \\renewenvironment{notice}[2]{%
          \\def\\py@noticetype{#1}
          \\begin{coloredbox}{#1}
          \\bf\\it
          \\par\\strong{#2}
          \\csname py@noticestart@#1\\endcsname
        }
    {
          \\csname py@noticeend@\\py@noticetype\\endcsname
          \\end{coloredbox}
        }
    \\makeatother

     '''



# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'policy.tex', u'Geek of algorithm',
     u'duanwujie', 'book'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'policy', u'Kernel Geek',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'debian-policy', 'Debian Policy ManualX',
     author, 'debian-policy', 'Debian Policy ManualX.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Use a simpler file name.
epub_basename = 'policy'

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_description = """
This manual describes the policy requirements for the Debian distribution.
This includes the structure and contents of the Debian archive and several
design issues of the operating system, as well as technical requirements
that each package must satisfy to be included in the distribution.
"""

# The unique identifier of the text. This can be an ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
