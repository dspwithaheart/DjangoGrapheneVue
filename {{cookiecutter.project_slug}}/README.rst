==============
{{cookiecutter.project_slug}}
==============

Template for a Django project with standalone UI.

{{cookiecutter.project_description}}

Features
--------

* Testing setup with ``hatch`` and ``uv``
* Gitlab CI
* Multi python version testing: Setup to easily test for various python versions with ``hatch`` matrix environment
* Version handling: Utilize ``hatch`` version handling (can use ``hatch-vcs``)


Quickstart
----------
* Modify project specific settings within the ``pyproject.toml``.
* Setup DB (For Oracle, you need to install the Oracle Instant Client and set the environment variables ``LD_LIBRARY_PATH``::

    export LD_LIBRARY_PATH=/pathTo/instantclient-basic-linux.x64-23.4.0.24.05/instantclient_23_4

* If you have a seperate UI repo as a submodule, pull submodules with::

    git submodule update --init --recursive

* Generate Models from DB(make sure db connection parameters are set in .env file)::

    hatch run dev:generatemodels

* Init UI with::

    hatch run dev:buildui

* Build Django with UI and run dev server with::

    hatch run dev:build

* Add tests to your code and use::

    hatch run test:cov

* Modify the ``.gitlab-ci.yml`` to reflect your intended CI chain
* Release your package by pushing a new tag to master (CI pipe including release to nexus uses tagging).
* Create a gitlab repo to upload your code

Now you have a GraplQL API for your DB
--------------------------------------
  

Project Structure overview::

        .
        ├── AUTHORS.rst
        ├── CONTRIBUTING.rst
        ├── deployandrun.sh
        ├── deploy{{cookiecutter.project_slug}}ui.sh
        ├── docker-compose-swarm.yml
        ├── docker-compose.yml
        ├── Dockerfile
        ├── docs
        │   └── ...
        ├── entrypoint.sh
        ├── .env
        ├── .env.dd
        ├── .env.pp
        ├── .env.tc
        ├── .env.to
        ├── .gitignore
        ├── .gitlab-ci.yml
        ├── .gitmodules
        ├── HISTORY.rst
        ├── infra
        │   └── docker
        │       └── {{cookiecutter.project_slug}}
        │           ├── Dockerfile
        │           ├── Dockerfile__
        │           └── entrypoint.sh
        ├── .pre-commit-config.yaml
        ├── pyproject.toml
        ├── README.rst
        ├── src
        │   ├── {{cookiecutter.project_slug}}django
        │   │   ├── config
        │   │   │   ├── asgi.py
        │   │   │   ├── __init__.py
        │   │   │   ├── routers.py
        │   │   │   ├── schemaFromModels.py
        │   │   │   ├── schema.py
        │   │   │   ├── settings.py
        │   │   │   ├── urls.py
        │   │   │   └── wsgi.py
        │   │   ├── {{cookiecutter.project_slug}}django
        │   │   │   ├── app.py
        │   │   │   ├── __init__.py
        │   │   │   ├── models.py
        │   │   │   ├── urls.py
        │   │   │   └── views.py
        │   │   ├── format_index_html.py
        │   │   ├── manage.py
        │   │   ├── requirements.txt
        │   │   ├── static
        │   │   │   ├── favicon.ico
        │   │   │   └── index.html
        │   │   └── templates
        │   │       └── .index.html.placeholder
        │   └── vite.config.ts.default
        └── tests
            ├── __init__.py
            └── test_{{cookiecutter.project_slug}}.py

