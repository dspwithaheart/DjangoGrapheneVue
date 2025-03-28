.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at http://gitServer.domain-name.com/yadava/{{cookiecutter.project_slug}}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the gitlab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the gitlab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{cookiecutter.project_slug}} could always use more documentation, whether as part of the
official {{cookiecutter.project_slug}} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at http://gitServer.domain-name.com/yadava/{{cookiecutter.project_slug}}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{cookiecutter.project_slug}}` for local development.

1. Fork the `{{cookiecutter.project_slug}}` repo on gitlab.
2. Clone your fork locally::

    $ git clone git@gitServer.domain-name.com/:your_name_here:/{{cookiecutter.project_slug}}.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv {{cookiecutter.project_slug}}
    $ cd {{cookiecutter.project_slug}}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass tests and use black for code formatting::

    $ hatch test:cov
    $ hatch run black

   To get hatch, pytest and black, just pip install them into your virtualenv.

6. Commit your changes and push your branch to gitlab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the gitlab website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.8, 3.9 and for 3.10.

Tips
----

To run a subset of tests::

    $ pytest tests.test_{{cookiecutter.project_slug}}

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ hatch version minor # possible: major / minor / patch / release / b / a / dev
$ git push
$ git push --tags
