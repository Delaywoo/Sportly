from django.shortcuts import render, redirect
from .models import Join
from .forms import Joinform
from distutils.command.clean import clean
# Create your views here.
def joinall(request):
    return render(request, 'joinall.html')

def joinpw(request):
    return render(request,'joinpw.html')

def joinnew(request):
    return render(request,'joinnew.html')

def formcreate(request):
    if request.method =='POST':
        form =Joinform(request.POST)
        if form.is_valid():
            post= Join()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()

            return redirect('joinall')
    
    else:
        form =Joinform()
    
    return render(request, 'form_create.html',{'form':form})