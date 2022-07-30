from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=userid, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'badlogin.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')

    elif request.method == "POST":
        username=request.POST.get('username', None)
        user_id=request.POST.get('user_id', None)
        password=request.POST.get('password',None)
        email=request.POST.get('email',None)
        re_password = request.POST.get('re_password',None)


        if (username and user_id and password and re_password and email) == '':
            return redirect('signup')                                    
        elif password != re_password:
            return redirect('signup')

        else:
            user = User(
                password=password, 
                user_id= user_id, 
                username=username, 
                email=email)    
            
            user.save()


        return redirect('home')