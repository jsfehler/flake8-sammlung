# flake8-sammlung

Install [flake8](https://gitlab.com/pycqa/flake8) and the following plugins in one shot:

- [bandit](https://github.com/PyCQA/bandit)
- [dlint](https://github.com/dlint-py/dlint)
- [flake8-broken-line](https://github.com/sobolevn/flake8-broken-line)
- [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
- [flake8-commas](https://github.com/PyCQA/flake8-commas)
- [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
- [flake8-docstrings](https://github.com/PyCQA/flake8-docstrings)
- [flake8-import-order](https://github.com/PyCQA/flake8-import-order)
- [flake8-multiline-containers](https://github.com/jsfehler/flake8-multiline-containers)
- [flake8-mutable](https://github.com/ebeweber/flake8-mutable)
- [mccabe](https://github.com/PyCQA/mccabe)
- [pep8-naming](https://github.com/PyCQA/pep8-naming)

# Development

- Requirements are compiled using [pip-tools](https://github.com/jazzband/pip-tools)

- The compiled requirements.txt is parsed into the install_requires arguments for setup.

# Testing

[tox](https://github.com/tox-dev/tox) is used to build an environment and install the packages.
If installing the packages fails, there's most likely a version mismatch.
