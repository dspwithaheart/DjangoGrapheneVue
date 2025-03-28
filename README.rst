===========================
Cookiecutter Tempalte
===========================


Cookiecutter_ template for Django + Vue + Vite.

Features
--------

* Testing setup with ``hatch`` and ``uv``
* Gitlab CI
* Multi python version testing: Setup to easily test for various python versions with ``hatch`` matrix environment
* Version handling: Utilize ``hatch`` version handling (can use ``hatch-vcs``)
* Release to nexus: using ``hatch publish`` feature

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (Cookiecutter 1.4.0+)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter ssh://git@<project_url>.git

Then:
  * Modify project specific settings within the ``pyproject.toml``.
  * Setup DB (For Oracle, you need to install the Oracle Instant Client and set the environment variables ``LD_LIBRARY_PATH`` 
    ``export LD_LIBRARY_PATH=/pathTo/instantclient-basic-linux.x64-23.4.0.24.05/instantclient_23_4``)
  * Init UI with ``hatch run dev:buildui``
  * Build Django with UI and run dev server with ``hatch run dev:build``
  * Create a dev environment with ``hatch``.
  * Add tests to your code and use ``hatch run test:cov``
  * Create a gitlab repo to upload your code.
  * Modify the ``.gitlab-ci.yml`` to reflect your intended CI chain
  * Release your package by pushing a new tag to master (CI pipe including release to nexus uses tagging).

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html


