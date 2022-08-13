<<<<<<< HEAD

from django.shortcuts import render, redirect
from django.contrib.auth.models import User #장고에 이미 내장되어 있는 객체
from django.contrib import auth
from django.contrib.auth import login, authenticate
#from django.core.exceptions import ValidationError

#from .forms import SignupForm
#from .models import Customuser

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']: 
            username=request.POST.get('username')
            if User.objects.filter(username=username).exists(): #기존 아이디와 중복될 경우.
                return render(request, 'alert.html')
                #raise ValidationError(username +"은 기존 아이디와 중복됩니다.")
            password=request.POST.get('password')
            email=request.POST.get('email')
            last_name=request.POST.get('last_name')
            # user 객체를 새로 생성 및 저장
            user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name)
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'badlogin.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')

"""
# Create your views here.
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = auth.authenticate(request, user_id=user_id, password=password) 
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request,'badlogin.html')

    else: #POST가 아닌 GET 요청일 경우
        return render(request,'login.html') #로그인form이 담긴 페이지를 띄워준다.

def login2(request):
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(user_id=request.POST['user_id'], password=request.POST['password'])
            # 로그인
            new_user.save()#추가0806
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'signup.html')
"""

"""
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


        return redirect('home')"""
=======
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
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
