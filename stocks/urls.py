from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list, name="list" ),
    path("submit-form/", views.submit_form, name ="submit_form"),
]