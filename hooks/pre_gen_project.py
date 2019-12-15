import os
import re
import sys

try:
    import git
except ModuleNotFoundError:
    print('{{ cookiecutter._template }} requires gitpython.')
    raise

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

namespace_name = '{{ cookiecutter.project_namespace }}'
module_name = '{{ cookiecutter.project_slug }}'


def assert_project_slug_is_valid_module_name():
    if not re.match(MODULE_REGEX, module_name):
        print(
            'ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)
        # Exit to cancel project
        sys.exit(1)


def assert_project_namespace_is_valid():
    if not re.match(MODULE_REGEX, namespace_name):
        print(
            'ERROR: The project namespace (%s) is not a valid Python module name. Please do not use a - and use _ instead' % namespace_name)
        # Exit to cancel project
        sys.exit(1)


def initialize_git():
   r = git.Repo.init(PROJECT_DIRECTORY)


if __name__ == '__main__':
    assert_project_namespace_is_valid()
    assert_project_slug_is_valid_module_name()

    initialize_git()


