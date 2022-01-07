#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from __future__ import absolute_import
# from __future__ import unicode_literals
# import os

# from setuptools import setup, find_packages

# try:
#     with open('README.rst') as f:
#         readme = f.read()
# except IOError:
#     readme = ''

# def _requires_from_file(filename):
#     return open(filename).read().splitlines()

# # version
# here = os.path.dirname(os.path.abspath(__file__))
# version = next((line.split('=')[1].strip().replace("'", '')
#                 for line in open(os.path.join(here,
#                                               'pypipkg',
#                                               '__init__.py'))
#                 if line.startswith('__version__ = ')),
#                '0.0.dev0')

# setup(
#     name="optical_tracer",
#     version=version,
#     url='https://github.com/pokurin123/optical_tracer',
#     author='pokurin123',
#     author_email='s1922074@stu.musashino-u.ac.jp',
#     maintainer='pokurin123',
#     maintainer_email='s1922074@stu.musashino-u.ac.jp',
#     description='The system detects and tracks characteristic moving objects from the video, and traces their movement to create a 3D graph.',
#     long_description=readme,
#     packages=find_packages(),
#     install_requires=_requires_from_file('requirements.txt'),
#     license="MIT",
#     classifiers=[
#         'Framework :: Matplotlib',
#         'Programming Language :: Python :: 3.8',
#         'License :: OSI Approved :: MIT License',
#     ],
#     entry_points={
#         'console_scripts': [
#             "optical_tracer=optical_tracer.main:main"
#         ]
#     },
# )

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="optical_tracer",
    version="0.1.2",
    author="pokurin123",
    author_email="s1922074@stu.musashino-u.ac.jp",
    description="The system detects and tracks characteristic moving objects from the video, and traces their movement to create a 3D graph.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pokurin123/optical_tracer",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        'Framework :: Matplotlib',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)