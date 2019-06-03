from get_requirements import get_requirements

from setuptools import setup


setup(
    name="flake8-sammlung",
    version="0.0.3",
    description="Collection of flake8 plugins",
    author="Joshua Fehler",
    author_email="jsfehler@gmail.com",
    license="MIT",
    install_requires=get_requirements(),
)
