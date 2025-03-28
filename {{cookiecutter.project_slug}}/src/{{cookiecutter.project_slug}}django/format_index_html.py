import sys, os
import fileinput

file = "templates/index.html"
file = os.path.join(os.path.dirname(__file__), file)

with open(file, "r+") as f:
    s = f.read()
    f.seek(0)
    f.write("{% load static %}\n" + s)

for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace("/assets/", "{% static 'assets/"))
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace(".css", ".css' %}"))
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace(".js", ".js' %}"))
for i, line in enumerate(fileinput.input(file, inplace=1)):
    sys.stdout.write(line.replace("/favicon.ico", "{% static 'favicon.ico' %}"))
