{%- if cookiecutter.project_slug == 'cli' -%}
"""Console script for {{cookiecutter.project_repo}}."""
import sys
import click
from click_plugins import with_plugins
from entrypoints import get_group_named


@with_plugins(get_group_named("{{cookiecutter.project_namespace}}.cli"))
@click.group()
def main(args=None):
    """{{cookiecutter.project_namespace}} command-line-interface"""
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
{%- endif %}
