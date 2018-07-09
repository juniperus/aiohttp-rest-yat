import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.description}}',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: aiohttp",
    ],
    keywords="web services",
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.email}}',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'aiohttp'
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.app:main',
        ],
    })
