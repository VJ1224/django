from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,'users/register.html',{'form': form})
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form': form})
