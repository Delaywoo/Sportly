from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password1']== request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                                                )
            auth.login(request,user)
            return redirect('home')
        return render(request,'signup.html')

    return render(request,'signup.html')
