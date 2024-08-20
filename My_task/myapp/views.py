from django.shortcuts import redirect, render
from.forms import app_form
from.models import app,user_task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics

def index(request):
    if request.method=="POST":
        form = app_form(request.POST,request.FILES)
        print("POST")
        if form.is_valid():
            form.save()
            print("form saved!")
            return redirect("index")
    return render(request,"index.html",{})
def interface(request):
    data = app.objects.all()
    points,created = user_task.objects.get_or_create(user=request.user)
    return render(request,"interface.html",{"data":data,"points":points.user_point})

def details(request,task_id):
    task_detail = app.objects.get(pk=task_id)
    return render(request,"details.html",{"task_detail":task_detail})

@login_required
def counter(request):
    user_pro,created = user_task.objects.get_or_create(user=request.user)
    if request.method == "POST":
        print("post request!")
        user_pro.user_point += 10
        
        user_pro.save()
        print(user_pro.user_point)
        print("saved done!")
        return redirect(request.path)
    else:
        user_point = user_pro.user_point
        return render(request,"task.html",{"user_point":user_point})
    
def user_logout(request):
    logout(request)
    return redirect("login_reg")

