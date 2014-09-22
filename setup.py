# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '1.2.dev0'

setup(
    name='plone.app.imagecropping',
    version=version,
    description="allows images to be manually cropped using JCrop JS library",
    long_description='\n\n'.join([
        open('README.rst').read(),
        open('CONTRIBUTORS.rst').read(),
        open('CHANGES.rst').read(),
    ]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone image crop',
    author='',
    author_email='',
    url='https://github.com/collective/plone.app.imagecropping',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Pillow',
        'plone.app.imaging',
        'Products.CMFPlone>=4.2'
    ],
    extras_require={
        'test': [
            'Products.DateRecurringIndex',
            'plone.app.testing[robot]>=4.2.2',
            'plone.app.robotframework',
            'plone.app.contenttypes',
            'plone.namedfile>=2.0.1',
            'zope.globalrequest',
        ],
        'archetypes': [
            'Products.ATContentTypes',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
