import os
import sys
sys.path.insert(0, os.path.abspath('..'))

## FIXME use the correct import
import my_module
release = my_module.__version__

## FIXME change project and author names
project = 'lk-common'
copyright = '2021 Boise State University'
author = 'Michael Ekstrand'


extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = '.rst'

pygments_style = 'sphinx'
highlight_language = 'python3'

html_theme_options = {
    'github_user': 'lenskit',
    ## FIXME correct GitHub repository name
    'github_repo': 'lk-common',
}
templates_path = ['_templates']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'lenskit': ('https://lkpy.lenskit.org/en/stable/', None),
    'csr': ('https://csr.lenskit.org/en/stable/', None),
    'binpickle': ('https://binpickle.lenskit.org/en/stable/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'numba': ('https://numba.readthedocs.io/en/stable/', None),
}

autodoc_default_options = {
    'member-order': 'bysource'
}
