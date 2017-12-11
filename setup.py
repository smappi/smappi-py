from setuptools import setup
from smappi import __version__

try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    long_description = ''

setup(
    name='smappi',
    version=__version__,
    description="Python Client for Smappi API",
    long_description=long_description,
    keywords='smappi, api',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/smappi/smappi-py',
    license='MIT',
    packages=['smappi', ],
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
