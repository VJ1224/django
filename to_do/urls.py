from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="todo-home"),
    path("additem", views.additem, name="todo-add"),
    path("done/<int:key>", views.markDone, name="todo-done"),
    path("undo/<int:key>", views.undo, name="todo-undo"),
    path("delete/<int:key>", views.deleteItem, name="todo-delete"),
]
