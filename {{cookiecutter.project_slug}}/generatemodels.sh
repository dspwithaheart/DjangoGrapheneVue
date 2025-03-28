echo 'Generate Models from DB'

python ./src/{{cookiecutter.project_slug}}django/manage.py inspectdb > ./src/{{cookiecutter.project_slug}}django/{{cookiecutter.project_slug}}django/models_temp.py

sed -i -e 's/models.FloatField(primary_key=True)/models.BigAutoField(primary_key=True)/g' ./src/{{cookiecutter.project_slug}}django/{{cookiecutter.project_slug}}django/models_temp.py

mv ./src/{{cookiecutter.project_slug}}django/{{cookiecutter.project_slug}}django/models_temp.py ./src/{{cookiecutter.project_slug}}django/{{cookiecutter.project_slug}}django/models.py

echo 'Done...'