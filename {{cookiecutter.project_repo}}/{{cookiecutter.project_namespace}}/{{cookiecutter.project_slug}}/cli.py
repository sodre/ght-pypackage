"""Console script for {{cookiecutter.project_repo}}."""

import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.project_slug == 'cli' %}
from click_plugins import with_plugins
from entrypoints import get_group_named


@with_plugins(get_group_named("{{cookiecutter.project_namespace}}.cli"))
@click.group()
def main(args=None):
    """{{cookiecutter.project_namespace}} command-line-interface"""
    return 0
{%- elif cookiecutter.command_line_interface|lower == 'click' %}


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_repo}}."""
    # fmt: off
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    # fmt: on
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
