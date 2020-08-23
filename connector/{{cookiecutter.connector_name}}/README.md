# {{ cookiecutter.connector_name }}
![Run Tests](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}/workflows/Run%20Tests/badge.svg)
[![license](https://img.shields.io/github/license/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}.svg)](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.connector_name }}.svg)](https://pypi.org/project/{{ cookiecutter.connector_name }}/)
[![release](https://img.shields.io/github/release/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}.svg)](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}.svg)](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.connector_name }}/releases)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=opsani/{{ cookiecutter.connector_name }})](https://dependabot.com)

{{ cookiecutter.description }}

## Configuration

```yaml
{{ cookiecutter.connector_name }}:
  setting: value
```

A starting point configuration can be added to your servo assembly via: `servo generate --defaults {{ cookiecutter.connector_name }}`.

## Installation

{{ cookiecutter.connector_name }} is distributed as an installable Python package via PyPi and can be added to a servo assembly via Poetry:

```console
❯ poetry add {{ cookiecutter.connector_name }}
```

## Usage

...

## Testing

Automated tests are implemented via [Pytest](https://docs.pytest.org/en/stable/): `pytest .`

## License

{{ cookiecutter.connector_name }} is distributed under the terms of the Apache 2.0 Open Source license.

A copy of the license is provided in the [LICENSE](LICENSE) file at the root of the repository.
