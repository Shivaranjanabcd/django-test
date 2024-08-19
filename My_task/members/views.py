from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_reg(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('index')
                else:
                    return redirect('interface')  
            else:
                messages.error(request, "Invalid email or password")
                return redirect("login_reg")
        
        elif 'register' in request.POST:
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Email is already registered")
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, "Account created successfully")
                    return redirect('login_reg')  
                messages.error(request, "Passwords do not match")
    
    return render(request, 'login.html',{})