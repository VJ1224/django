from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def home(request):
    return render(request,'home/home.html')
