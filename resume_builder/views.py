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
    if request.method == 'POST':
        form = resumeForm(request.POST)
        context['form'] = form
        if form.is_valid():
            query = urlencode({'data': form.cleaned_data})
            url = '{}?{}'.format('build/',query)
            return HttpResponseRedirect(url)
        return render(request, "resume_builder/resume.html", context)
    return render(request, "resume_builder/resume.html", context)

def build(request):
    data = request.GET['data']
    resume = ast.literal_eval(data)
    context = {
        'resume': resume
    }
    return render(request, "resume_builder/build.html", context)