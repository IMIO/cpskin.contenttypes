# -*- coding: utf-8 -*-
"""Installer for the cpskin.contenttypes package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='cpskin.contenttypes',
    version='1.0.14.dev0',
    description="CPSkin content types",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Laurent Lasudry',
    author_email='laurent.lasudry@affinitic.be',
    url='https://pypi.python.org/pypi/cpskin.contenttypes',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['cpskin'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'plone.app.dexterity',
        'plone.api>=1.8.4',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'plone.app.dexterity<=2.1.1',
        'plone.app.referenceablebehavior',
        'plone.app.relationfield',
        'plone.app.lockingbehavior',
        'plone.schema',
        'plone.app.contenttypes',
        'plone.app.imagecropping',
        'cpskin.locales',
        'unidecode',
        'imio.behavior.teleservices',
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
