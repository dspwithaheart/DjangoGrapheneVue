#!/bin/bash
set -e
npm run dev
# ./deploy{{cookiecutter.project_slug}}ui.sh
# echo 'Format index.html as Jinja template'
# mv static/index.html templates/index.html
# python format_index_html.py
# echo 'Done...'

# # !!! Don't need to run migrations as no DB is used
# # python manage.py migrate

# # copies static to $STATIC_ROOT
# python manage.py collectstatic --noinput

# # uwsgi --socket  0.0.0.0:8000 --master --enable-threads --module config.wsgi -b 65535
# python manage.py runserver 0.0.0.0:8000