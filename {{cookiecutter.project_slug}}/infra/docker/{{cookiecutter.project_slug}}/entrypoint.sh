#!/bin/bash
set -e

echo 'Format index.html as Jinja template'

cp static/index.html templates/index.html
python format_index_html.py
echo 'Done...'

# copies static to $STATIC_ROOT
python manage.py collectstatic --noinput

# DB Operations (Enable for Oracle)
# python ./src/{{cookiecutter.project_slug}}django/manage.py makemigrations {{cookiecutter.project_slug}}django

# echo 'Show migrations'
# python ./src/{{cookiecutter.project_slug}}django/manage.py showmigrations {{cookiecutter.project_slug}}django

# echo 'Run migrations'
# python ./src/{{cookiecutter.project_slug}}django/manage.py migrate

#python manage.py runserver 0.0.0.0:8000

export PORT=8000
echo 'Server runnning on port ' $PORT

gunicorn --workers 8  --timeout 60 config.wsgi