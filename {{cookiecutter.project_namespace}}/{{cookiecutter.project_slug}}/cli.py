{%- import '.github/ght/macros/selected.j2' as selected -%}
{% call(cli) selected.first(ght.command_line_interface) -%}
"""Console script for {{cookiecutter.project_repo}}."""

import sys
{%- if cli|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.project_slug == 'cli' %}
from click_plugins import with_plugins
from entrypoints import get_group_named


@with_plugins(get_group_named("{{cookiecutter.project_namespace}}.cli").values())
@click.group()
def {{ cookiecutter.project_slug }}(args=None):
    """{{cookiecutter.project_namespace}} command-line-interface"""
    return 0
{%- elif cli|lower == 'click' %}


@click.command()
def {{ cookiecutter.project_slug }}(args=None):
    """Console script for {{cookiecutter.project_repo}}."""
    # fmt: off
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    # fmt: on
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit({{ cookiecutter.project_slug }})  # pragma: no cover
{%- endcall %}
