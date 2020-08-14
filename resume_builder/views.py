from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import resumeForm


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
