import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import {{cookiecutter.project_slug}}

project = '{{cookiecutter.project_name}}'
copyright = '2021 Boise State University'
author = '{{cookiecutter.full_name}}'

release = {{cookiecutter.project_slug}}.__version__

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
    'github_user': '{{cookiecutter.github_username}}',
    'github_repo': '{{cookiecutter.project_slug}}',
    # 'travis_button': False,
    # 'html_baseurl': 'https://csr.lenskit.org/'
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
