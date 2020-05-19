{%- import '.github/ght/macros/selected.j2' as selected -%}
#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages
import os

with open("README.rst") as readme_file:
    readme = readme_file.read()

# The requirements section should be kept in sync with the environment.yml file
requirements = [
    # fmt: off
    {%- call(cli) selected.first(ght.command_line_interface) %}
    {%- if cli|lower == 'click' %}
    "click>=7.0",
    "click-plugins",
    "entrypoints",
    {%- endif %}
    {%- endcall %}
    # fmt: on
]

setup_requirements = [
    # fmt: off
    {%- if cookiecutter.use_pytest == 'y' %}
    "pytest-runner",
    "setuptools_scm",
    "setuptools_scm_git_archive",
    "wheel",
    {%- endif %}
    # fmt: on
]

test_requirements = [
    # fmt: off
    {%- if cookiecutter.use_pytest == 'y' %}
    "pytest>=3",
    "pytest-cov",
    {%- endif %}
    # fmt: on
]

conda_rosetta_stone = {
    # fmt: off
    "pypa-requirement": "conda-dependency"
    # fmt: on
}

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'BSD': 'License :: OSI Approved :: BSD License',
    'ISC': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache': 'License :: OSI Approved :: Apache Software License',
    'GNUv3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Proprietary': 'License :: Other/Proprietary License',
} %}

setup_kwargs = dict(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    use_scm_version={"write_to": "src/{{ cookiecutter.project_namespace }}/{{ cookiecutter.project_slug }}/_version.py"},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- call(license) selected.first(ght.license) %}
        "{{ license_classifiers[license] }}",
{%- endcall %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- call(cli) selected.first(ght.command_line_interface) %}
    {%- if 'no' not in cli|lower %}
    # fmt: off
    entry_points={
        {%- if cookiecutter.project_slug == "cli" %}
        "console_scripts": [
            "{{ cookiecutter.project_namespace }}
        {%- else %}
        "{{cookiecutter.project_namespace}}.cli": [
            "{{ cookiecutter.project_slug.replace("_","-") }}
        {%- endif -%}={{cookiecutter.project_namespace}}.{{ cookiecutter.project_slug }}.cli:{{ cookiecutter.project_slug }}",
        ],
    },
    # fmt: on
    {%- endif %}
    {%- endcall %}
    install_requires=requirements,
{%- call(license) selected.first(ght.license) %}
    license="{{ license }}",
{%- endcall %}
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }} {{ cookiecutter.project_namespace }}",
    name="{{cookiecutter.project_namespace}}-{{ cookiecutter.project_slug }}",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="./src"),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        # fmt: off
        "test": test_requirements
        # fmt: on
    },
    url="https://github.com/{{ cookiecutter.github_organization}}/{{ cookiecutter.project_repo}}",
    zip_safe=False,
)

if "CONDA_BUILD_STATE" in os.environ:
    try:
        from setuptools_scm import get_version

        setup_kwargs["version"] = get_version(**setup_kwargs["use_scm_version"])
        del setup_kwargs["use_scm_version"]
    except ModuleNotFoundError:
        print(
            "Error: {{ cookiecutter.project_repo }} requires that setuptools_scm be installed with conda-build!"  # noqa: E501
        )
        raise
    setup_kwargs["conda_rosetta_stone"] = conda_rosetta_stone

setup(**setup_kwargs)
