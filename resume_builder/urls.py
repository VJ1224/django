from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="resume-home"),
    path("build/", views.build, name="resume-built"),
    path("save/", views.save, name="resume-save")
]
