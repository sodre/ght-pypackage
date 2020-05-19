{%- import '.github/ght/macros/selected.j2' as selected -%}
{% call(cli) selected.first(ght.command_line_interface) -%}
=====
Usage
=====

To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.project_slug }}

{%- if cli|lower == 'click' %}
To use {{ cookiecutter.project_name }} command line tool:

.. click:: {{ cookiecutter.project_namespace }}.{{ cookiecutter.project_slug }}.cli:{{ cookiecutter.project_slug }}
  :prog: {{ cookiecutter.project_namespace }}{% if cookiecutter.project_slug != "cli" %}{{ cookiecutter.project_slug.replace("_", "-") }}{% endif %}
  :show-nested:
{%- endif %}
{% -endcall %}
