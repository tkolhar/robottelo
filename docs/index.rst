Robottelo
=========

`Robottelo`_ is a test suite which exercises `The Foreman`_. All tests are
automated, suited for use in a continuous integration environment, and `data
driven`_. There are three types of tests:

* UI tests, which rely on Selenium's `WebDriver`_.
* CLI tests, which rely on `Paramiko`_.
* API tests, which rely on `Requests`_.

Quickstart
==========

The following is only a brief setup guide for `Robottelo`_. More extensive
documentation `is available <http://robottelo.readthedocs.org/en/latest/>`_ at
Read the Docs.

Requirements
------------

Install Python header files. The package providing these files varies per
distribution. For example:

* Fedora 20 provides header files in the
  `python-devel <https://apps.fedoraproject.org/packages/python-devel>`_
  package.
* Ubuntu 14.04 provides header files in the
  `python-dev <http://packages.ubuntu.com/trusty/python-dev>`_ package.

Get the source code and install dependencies::

    $ git clone git://github.com/omaciel/robottelo.git
    $ pip install -r requirements.txt

That's it! You can now go ahead and start testing The Foreman. However, there
are a few other things you may wish to do before continuing:

1. You may want to install development tools (such as gcc) for your OS. If
   running Fedora or Red Hat Enterprise Linux, execute ``yum groupinstall
   "Development Tools"``.
2. You may wish to install the optional dependencies listed in
   ``requirements-optional.txt``. (Use pip, as shown above.) They are required
   for tasks like working with certificates, running the internal robottelo test
   suite and checking code quality with pylint.

Running the Tests
=================

Before running any tests, you must create a configuration file::

    $ cp robottelo.properties.sample robottelo.properties
    $ vi robottelo.properties

That done, you can run tests using ``make``::

    $ make test-robottelo
    $ make test-docstrings
    $ make test-foreman-api
    $ make test-foreman-cli
    $ make test-foreman-ui

If you want to run the test suite without the aid of ``make``, you can do that
with either `unittest`_ or `nose`_::

    $ python -m unittest discover -s tests -t .
    $ nosetests -c robottelo.properties

The following sections discuss, in detail, how to update the configuration file
and run tests directly.

Initial Configuration
---------------------

To configure Robottelo, create a file named ``robottelo.properties``. You can
use the ``robottelo.properties.sample`` file as a starting point. Then, edit the
configuration file so that at least the following attributes are set::

    server.hostname=[FULLY QUALIFIED DOMAIN NAME]
    server.ssh.key_private=[PATH TO YOUR SSH KEY]
    server.ssh.username=root
    project=foreman
    locale=en_US
    remote=0

    [foreman]
    admin.username=admin
    admin.password=changeme

Note that you only need to configure the SSH key if you want to run CLI tests.
There are other settings to configure what web browser to use for UI tests and
even configuration to run the automation using `SauceLabs`_. For more
information about what web browsers you can use, check Selenium's `WebDriver`_
documentation.

Testing With Unittest
---------------------

To run all tests::

    $ python -m unittest discover \
        --start-directory tests/ \
        --top-level-directory .

It is possible to run a specific subset of tests::

    $ python -m unittest tests.robottelo.test_decorators
    $ python -m unittest tests.robottelo.test_decorators.DataDecoratorTestCase
    $ python -m unittest tests.robottelo.test_decorators.DataDecoratorTestCase.test_data_decorator_smoke

To get more verbose output, or run multiple tests::

    $ python -m unittest discover -s tests/ -t . -v
    $ python -m unittest \
        tests.robottelo.test_decorators \
        tests.robottelo.test_cli

To test The Foreman's API, CLI or UI, use the following commands respectively::

    $ python -m unittest discover -s tests/foreman/api/
    $ python -m unittest discover -s tests/foreman/cli/
    $ python -m unittest discover -s tests/foreman/ui/

For more information about Python's `unittest`_ module, read the documentation.

Testing With Nose
-----------------

You must have `nose`_ installed to execute the ``nosetests`` command.

To run all tests::

    $ nosetests -c robottelo.properties

It is possible to run a specific subset of tests::

    $ nosetests -c robottelo.properties tests.robottelo.test_decorators
    $ nosetests -c robottelo.properties tests.robottelo.test_decorators:DataDecoratorTestCase
    $ nosetests -c robottelo.properties tests.robottelo.test_decorators:DataDecoratorTestCase.test_data_decorator_smoke

To get more verbose output, or run multiple tests::

    $ nosetests -c robottelo.properties -v
    $ nosetests -c robottelo.properties \
        tests.robottelo.test_decorators \
        tests.robottelo.test_cli

To test The Foreman's API, CLI or UI, use the following commands respectively::

    $ nosetests -c robottelo.properties tests.foreman.api
    $ nosetests -c robottelo.properties tests.foreman.cli
    $ nosetests -c robottelo.properties tests.foreman.ui

Many of the existing tests use the `DDT module`_ to allow for a more data-driven
methodology and in order to run a specific test you need override the way
``nosetests`` discovers test names. For instance, if you wanted to run only the
``test_positive_create_1`` data-driven tests for the ``foreman.cli.test_org``
module::

    $ nosetests -c robottelo.properties -m test_positive_create_1 \
        tests.foreman.cli.test_org

Running UI Tests On a Headless Server
-------------------------------------

It is possible to run UI tests on a headless server. To do this:

* Install Xvfb. It is provided by the ``xorg-x11-server-Xvfb`` package on
  Fedora and Red Hat.
* Install the ``PyVirtualDisplay`` Python package. (It is listed in
  ``requirements-optional.txt``.)
* Set ``virtual_display=1`` in the configuration file ``robottelo.properties``.
* Optionally, set the ``window_manager_command`` option in the configuration
  file. This option should be set to the name of a window manager executable.
  For example, ``fluxbox`` or ``openbox`` are suitable values if you have
  Fluxbox or Openbox installed, respectively. Setting this option causes a
  window manager to be launched before the web browser, thus allowing the web
  browser to be maximized.

This done, UI tests no longer launch a visible web browser. Instead, UI tests
launch a web browser within a virtual display.

API Reference
=============

If you are looking for information on a specific function, class or method, this
part of the documentation is for you. The following is an overview of the topics
covered by the API. For more granular information, follow one of the links.

.. toctree::
    :maxdepth: 2

    api/index

Miscellany
==========

Bugs are listed `on GitHub <https://github.com/omaciel/robottelo/issues>`_. If
you think you've found a new issue, please do one of the following:

* Open a new bug report on Github.
* Join the #robottelo IRC channel on Freenode (irc.freenode.net).

You can generate the documentation for Robottelo as follows, so long as you have
`Sphinx`_ and make installed::

    $ cd docs
    $ make html

You can generate a graph of Foreman entities and their dependencies, so long as
you have `graphviz`_ installed::

    $ make graph-entities

To check for code smells::

    $ ./lint.py | less

The design and development for this software is led by `Og Maciel`_.

.. _data driven: http://en.wikipedia.org/wiki/Data-driven_testing
.. _DDT module: http://ddt.readthedocs.org/en/latest/
.. _graphviz: http://graphviz.org/
.. _nose: https://nose.readthedocs.org/en/latest/index.html
.. _Og Maciel: http://www.ogmaciel.com
.. _Paramiko: http://www.paramiko.org/
.. _Requests: http://docs.python-requests.org/en/latest/
.. _Robottelo: https://github.com/omaciel/robottelo
.. _SauceLabs: https://saucelabs.com/
.. _Sphinx: http://sphinx-doc.org/index.html
.. _The Foreman: http://theforeman.org/
.. _unittest: http://docs.python.org/2/library/unittest.html
.. _WebDriver: http://docs.seleniumhq.org/projects/webdriver/
