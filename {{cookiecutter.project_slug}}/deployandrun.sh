echo 'Build {{cookiecutter.project_slug}}ui'
# npm run --prefix ./src/{{cookiecutter.project_slug}}ui build:shclean
npm run --prefix ./src/{{cookiecutter.project_slug}}ui build
echo 'Done...'

echo 'Format index.html as Jinja template'
cp ./src/{{cookiecutter.project_slug}}django/static/index.html ./src/{{cookiecutter.project_slug}}django/templates/index.html
python ./src/{{cookiecutter.project_slug}}django/format_index_html.py
echo 'Done...'

# echo 'Collect static'
# python ./src/{{cookiecutter.project_slug}}django/manage.py collectstatic --noinput
# echo 'Done...'

# DB Operations
#echo 'Run migrations'
#python ./src/{{cookiecutter.project_slug}}django/manage.py showmigrations {{cookiecutter.project_slug}}django
#python ./src/{{cookiecutter.project_slug}}django/manage.py makemigrations {{cookiecutter.project_slug}}django
#python ./src/{{cookiecutter.project_slug}}django/manage.py migrate
##python ./src/{{cookiecutter.project_slug}}django/manage.py migrate --run-syncdb
#echo 'Done...'

export PORT=8000
echo 'Server runnning on port ' $PORT
python ./src/{{cookiecutter.project_slug}}django/manage.py runserver
