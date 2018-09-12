Python Client for Smappi API
=============================

Support python>=2.7, python>=3.0

.. image:: https://secure.travis-ci.org/smappi/smappi-py.png
    :target: http://travis-ci.org/smappi/smappi-py

More information on https://smappi.org/

Installation
-------------

This client is delivered without any dependencies!

.. code:: bash

   pip install smappi


Examples
--------

Use the helper:

.. code:: python

   >>> from smappi import smappi
   >>> smappi('adw0rd/example').greeting(name='friend')
   "Hello, friend!"

Or use the full version:

.. code:: python

   >>> import smappi
   >>> smappi.Request('adw0rd/example', 'json').calculator(digits=[42, 42, 42])
   126
   >>> smappi.Request('adw0rd/example', 'json').calculator(digits='42,42,42')
   126
   
For local development and debug specify host as path:

.. code:: python

    >>> from smappi import smappi
    >>> smappi('localhost:8000').greeting(name='friend')
    "Hello, friend!"
