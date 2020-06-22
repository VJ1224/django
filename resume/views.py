from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request,'resume/home.html')
