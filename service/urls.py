from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("", health),
]
