from django.contrib import admin
from .models import resume
from .forms import resumeForm


class resumeAdmin(admin.ModelAdmin):
    form = resumeForm


# Register your models here.
admin.site.register(resume, resumeAdmin)
