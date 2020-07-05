from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import toDoItem
from .forms import toDoForm

@login_required
def home(request):
    username=request.user
    context={
        'things':toDoItem.objects.filter(user=username),
        'today':timezone.now().date(),
        'user':username
    }
    return render(request,"to_do/home.html",context)

@login_required
def additem(request):
    username=request.user
    context={
        'things':toDoItem.objects.filter(user=username),
        'form': toDoForm(),
        'today':timezone.now().date(),
        'user':username
    }

    if request.method == 'POST':
        form = toDoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return HttpResponseRedirect("/todo")
        return render(request,"to_do/home.html",context)
    return render(request,"to_do/home.html",context)

@login_required
def markDone(request,key):
    try:
        item=toDoItem.objects.get(id=key)
        user=getattr(item,'user')
        if(user==request.user):
            item=toDoItem.objects.get(id=key)
            item.markDone
            item.save()
        return HttpResponseRedirect("/todo")
    except:
        return HttpResponseRedirect("/todo")

@login_required
def deleteItem(request,key):
    try:
        item=toDoItem.objects.get(id=key)
        user=getattr(item,'user')
        if(user==request.user):
            item=toDoItem.objects.get(id=key)
            item.delete()
        return HttpResponseRedirect("/todo")
    except:
        return HttpResponseRedirect("/todo")

@login_required
def undo(request,key):
    try:
        item=toDoItem.objects.get(id=key)
        user=getattr(item,'user')
        if(user==request.user):
            item=toDoItem.objects.get(id=key)
            item.undo
            item.save()
        return HttpResponseRedirect("/todo")
    except:
        return HttpResponseRedirect("/todo")
