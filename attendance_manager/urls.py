from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="attendance-home"),
    path("course/<int:key>/", views.course, name="attendance-home"),
    path("course/<int:key>/add", views.attended, name="attendance-add"),
    path("course/<int:key>/miss", views.missed, name="attendance-miss"),
    path("course/<int:key>/reset", views.reset, name="attendance-reset"),
    path("course/<int:key>/delete", views.delete, name="course-delete"),
    path("addcourse", views.addcourse, name="course-add"),
]
