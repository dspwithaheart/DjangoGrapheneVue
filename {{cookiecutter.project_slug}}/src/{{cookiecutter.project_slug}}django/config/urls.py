from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from django.views.static import serve
from django.conf import settings

from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

from {{cookiecutter.project_slug}}django.views import index,login

urlpatterns = [
    # Graphiql interface
    re_path(r'^graphql', jwt_cookie(GraphQLView.as_view(graphiql=True))),
    # LDAP login
    path("login/", login, name="login"),
    # django admin page
    path("admin/", admin.site.urls),
    # authentication
    path("accounts/", include("django.contrib.auth.urls")),
    path("", index, name="home"),
    # path("", include("{{cookiecutter.project_slug}}django.urls")),
        # to serve static files with django in PROD
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
