"""
Flask-EasyWebDAV
-------------

This is the description for that library
"""
from setuptools import setup

setup(
    name='Flask-EasyWebDAV',
    version='0.1',
    url='http://github.com/ghachey/flask-easywebdav',
    license='MIT',
    author='Ghislain Hachey',
    author_email='ghachey@outlook.com',
    description='Very simple extension to add support for easywebdav',
    long_description=__doc__,
    py_modules=['flask_easywebdav'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_easywebdav'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'easywebdav'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
