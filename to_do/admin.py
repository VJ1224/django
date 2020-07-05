from django.contrib import admin
from .models import toDoItem
from .forms import toDoForm


class toDoAdmin(admin.ModelAdmin):
    form = toDoForm


# Register your models here.
admin.site.register(toDoItem, toDoAdmin)
