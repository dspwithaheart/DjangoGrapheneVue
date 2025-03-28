from django.urls import include, path, re_path
from rest_framework import routers, permissions
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from {{cookiecutter.project_slug}}django.{{cookiecutter.project_slug}}django.views import  index

router = routers.DefaultRouter()

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Swagger interface
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # permission_classes = [IsAuthenticated]
)


urlpatterns = [
    # Swagger interface
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]