import os
from shutil import rmtree

REMOVE_PATHS = [
    '{% if cookiecutter.include_data != "y" %} data {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            rmtree(path)
        else:
            os.unlink(path)