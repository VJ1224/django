from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from .models import resume
from .forms import resumeForm
from django.utils.http import urlencode
import ast


# Create your views here.
def home(request):
    context = {
        'form': resumeForm()
    }
    return render(request, "resume_builder/resume.html", context)

def build(request):
    if request.method == 'POST':
        form = resumeForm(request.POST)
        if form.is_valid():
            context = {
                'resume': form.cleaned_data
            }
            return render(request, "resume_builder/build.html", context)
    return HttpResponseRedirect("/resume/")