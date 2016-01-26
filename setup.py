# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-session-notifier',
    version='0.0.2',
    author=u'Will & Skill',
    author_email='info@willandskill.se',
    packages=find_packages(),
    url='https://github.com/willandskill/django-session-notifier',
    license='MIT licence, see LICENCE.txt',
    description='Displays notification box in all views if user is session authenticated',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True
)