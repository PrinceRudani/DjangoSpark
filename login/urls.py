from django.urls import path

from . import views

urlpatterns = [
    path("", views.admin_load_login, name="admin_load_login"),
]
