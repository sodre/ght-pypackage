{%- import '.github/ght/macros/selected.j2' as selected -%}
{% call(license) selected.first(cookiecutter.open_source_license) %}
{% set is_open_source = license != 'Proprietary' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

.. image:: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_repo }}/pypa-conda?label=pypa-conda&logo=github&style=flat-square
   :target: https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_repo }}/actions?query=workflow%3Apypa-conda

.. image:: https://img.shields.io/conda/v/{{ cookiecutter.anaconda_organization }}/{{ cookiecutter.project_repo }}?logo=anaconda&style=flat-square
   :target: https://anaconda.org/{{ cookiecutter.anaconda_organization }}/{{ cookiecutter.project_repo }}

{% if is_open_source %}
.. image:: https://img.shields.io/codecov/c/gh/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_repo }}?logo=codecov&style=flat-square
{%- else %}
.. image:: https://codecov.io/gh/{{  cookiecutter.github_organization }}/{{ cookiecutter.project_repo }}/branch/master/graph/badge.svg?token={{ codecov.badge_token }}
{%- endif %}
   :target: https://codecov.io/gh/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_repo }}

.. image:: https://img.shields.io/codacy/grade/{{ codacy.project_id }}?logo=codacy&style=flat-square
   :target: https://www.codacy.com/app/{{ cookiecutter.github_organization }}/{{  cookiecutter.project_repo }}
   :alt: Codacy Badge

.. image:: https://img.shields.io/badge/code--style-black-black?style=flat-square
   :target: https://github.com/psf/black

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_repo }}?logo=pypi&style=flat-square
   :target: https://pypi.python.org/pypi/{{ cookiecutter.project_repo }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_repo | replace("_", "-") }}/badge/?version=latest&style=flat-square
   :target: https://{{ cookiecutter.project_repo | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' and false %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo }}/shield.svg&style=flat-square
   :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo }}/
   :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ license }}
* Documentation: https://{{ cookiecutter.project_repo | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO


-------

This package was created with ght-render_ and the `sodre/ght-pypackage`_ project template.

.. _ght-render: https://github.com/sodre/action-ght-render
.. _`sodre/ght-pypackage`: https://github.com/sodre/ght-pypackage
{% endcall %}
