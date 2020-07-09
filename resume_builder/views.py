from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from .models import resume
from .forms import resumeForm
from django.utils.http import urlencode


# Create your views here.
def home(request):
    context = {
        'form': resumeForm()
    }
    if request.method == 'POST':
        form = resumeForm(request.POST)
        context['form'] = form
        if form.is_valid():
            item = form.save()
            query = urlencode({'id': item.id})
            url = '{}?{}'.format('build/',query)
            return redirect(url)
        return render(request, "resume_builder/home.html", context)
    return render(request, "resume_builder/home.html", context)

def build(request):
    item_id = request.GET.get('id')
    data = resume.objects.get(id=item_id)
    context = {
        'resume': data
    }
    return render(request, "resume_builder/resume.html", context)

def save(request):
    item_id = request.GET.get('id')
    instance = resume.objects.get(id=item_id)
    instance.delete()
    return HttpResponseRedirect("/resume/")