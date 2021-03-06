{%- import '.github/ght/macros/selected.j2' as selected -%}
{% call(cli) selected.first(ght.command_line_interface) -%}
#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_repo }}` package."""

import pytest
{%- if cli|lower == 'click' %}
from click.testing import CliRunner
from {{cookiecutter.project_namespace}}.{{ cookiecutter.project_slug }} import cli
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cli|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.{{ cookiecutter.project_slug }})
    assert result.exit_code == 0
    {%- if cookiecutter.project_slug != "cli" %}
    assert "Replace this message" in result.output
    {%- else %}
    assert "Usage: {{ cookiecutter.project_slug }}" in result.output
    {%- endif %}
    help_result = runner.invoke(cli.{{ cookiecutter.project_slug }}, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
{%- endcall %}
