from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import courseForm
from django.template import RequestContext

def getAttended(username):
    attended=0
    for course in Course.objects.filter(user=username):
        attended=attended+course.classesAttended
    return attended

def getTotal(username):
    total=0
    for course in Course.objects.filter(user=username):
        total=total+course.classes
    return total

def getMissed(username):
    return getTotal(username)-getAttended(username)

def calculatePercentage(username):
    total = getTotal(username)
    attended = getAttended(username)
    if(total!=0):
        percentage="{0:.1f}".format(100*attended/(total))+"%"
    else:
        percentage="%"
    return percentage

@login_required
def home(request):
    username=request.user
    context={
        'courses':Course.objects.filter(user=username),
        'attended':getAttended(username),
        'missed':getMissed(username),
        'total':getTotal(username),
        'percentage':calculatePercentage(username),
        'user':username
    }
    return render(request,"attendance_manager/home.html",context)

@login_required
def course(request,key):
    try:
        course=Course.objects.get(id=key)
        user=getattr(course,'user')
        if(user==request.user):
            username=request.user
            context={
                'courses':Course.objects.filter(user=username),
                'thisCourse':Course.objects.get(id=key),
            }
            return render(request,"attendance_manager/course.html",context)
        else:
            return HttpResponseRedirect("/attendance/")
    except:
        return HttpResponseRedirect("/attendance/")

@login_required
def attended(request,key):
    try:
        course=Course.objects.get(id=key)
        user=getattr(course,'user')
        if(user==request.user):
            course=Course.objects.get(id=key)
            course.addAttended
            course.save()
            return HttpResponseRedirect("/attendance/course/"+str(key)+"/")
        else:
            return HttpResponseRedirect("/attendance/")
    except:
        return HttpResponseRedirect("/attendance/")

@login_required
def missed(request,key):
    try:
        course=Course.objects.get(id=key)
        user=getattr(course,'user')
        if(user==request.user):
            course=Course.objects.get(id=key)
            course.addMissed
            course.save()
            return HttpResponseRedirect("/attendance/course/"+str(key)+"/")
        else:
            return HttpResponseRedirect("/attendance/")
    except:
        return HttpResponseRedirect("/attendance/")

@login_required
def delete(request,key):
    try:
        course=Course.objects.get(id=key)
        user=getattr(course,'user')
        if(user==request.user):
            instance = Course.objects.get(id=key)
            instance.delete()
            return HttpResponseRedirect("/attendance/")
        else:
            return HttpResponseRedirect("/attendance/")
    except:
        return HttpResponseRedirect("/attendance/")

@login_required
def reset(request,key):
    try:
        course=Course.objects.get(id=key)
        user=getattr(course,'user')
        if(user==request.user):
            course=Course.objects.get(id=key)
            course.reset
            course.save()
            return HttpResponseRedirect("/attendance/course/"+str(key)+"/")
        else:
            return HttpResponseRedirect("/attendance/")
    except:
        return HttpResponseRedirect("/attendance/")

@login_required
def addcourse(request):
    username=request.user
    context={
        'courses':Course.objects.filter(user=username),
        'form': courseForm()
    }
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        return HttpResponseRedirect("/attendance")
    return render(request,"attendance_manager/addcourse.html",context)
