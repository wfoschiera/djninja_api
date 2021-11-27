from django.contrib import admin
from django.urls import path

from ninja_api_doc.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", api.urls),
]
