from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("", TemplateView.as_view(template_name="login.html")),
]
