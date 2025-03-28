from django.shortcuts import render
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    if authorize(request):
        return render(request, "index.html")
    else:
        return render(request, "login.html")


def authorize(request):
    user = None
    if request.POST:
        print("Login Request!")

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            print(f"Authenticated: {user}")
        else:
            print("Authentication failed!")
    return user
