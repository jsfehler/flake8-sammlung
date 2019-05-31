# flake8-sammlung

Install flake8 and the following plugins in one shot:

- flake8-blind-except
- flake8-broken-line
- flake8-builtins
- flake8-bugbear
- flake8-commas
- flake8-comprehensions
- flake8-docstrings
- flake8-import-order
- flake8-multiline-containers
- flake8-mutable
- mccabe
- pep8-naming

# Development

- Requirements are compiled using [pip-tools](https://github.com/jazzband/pip-tools)

- The compiled lint.txt is parsed into the install_requires arguments for setup.
