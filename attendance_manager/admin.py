from django.contrib import admin
from .models import Course
from .forms import courseForm

class courseAdmin(admin.ModelAdmin):
    form = courseForm

# Register your models here.
admin.site.register(Course,courseAdmin)
