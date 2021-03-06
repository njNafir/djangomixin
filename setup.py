import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="djangomixin",
    version="1.0.0",
    description="djangomixin is set of mixins and snippets that can help you to utilize your django functionality.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/njnafir/djangomixin",
    author="Nj Nafir",
    author_email="njnafir@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=['djangomixin'],
    include_package_data=True,
    install_requires=[],
)
