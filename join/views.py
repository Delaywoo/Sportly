<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Join
from join.forms import Joinform
from distutils.command.clean import clean
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Join, JoinPass
from .forms import JoinModelForm, JoinPassForm
from distutils.command.clean import clean
from django.contrib import auth
from django.contrib.auth.models import User

>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
# Create your views here.
def joinall(request):
    posts= Join.objects.all().order_by('-date')
    return render(request, 'joinall.html', {'posts':posts})

def joinpw(request):
    return render(request,'joinpw.html')

def joinnew(request):
    return render(request,'joinnew.html')

<<<<<<< HEAD
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
=======
def modelformcreate(request):
    if request.method =='POST' or request.method =='FILES':
        form = JoinModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('joinall')

    else: 
        form = JoinModelForm()
    return render(request, 'form_create.html', {'form' : form})


def joindetail(request, join_id):
    join_detail =get_object_or_404(Join, pk=join_id)

    return render(request,'join_detail.html',{'join_detail':join_detail})

def joinpw(request, join_id):
    joinpwd =get_object_or_404(Join, pk=join_id)
    join_detail =get_object_or_404(Join, pk=join_id)

    return render(request,'joinpw.html',{'joinpw':joinpwd, 'join_detail':join_detail})


def joinpassword(request):
    form = JoinPassForm()
    return render(request, 'joinpassword.html',{'form':form})

def joinin(request, join_id):
    if request.method == 'POST':
        realpassword = get_object_or_404(Join.joinpw, pk=join_id)
        realpassword == get_object_or_404(JoinPass.joinpassword, pk=join_id)
        return render(request,'joinpassword')

    else :
        return render(request,'joinpw')
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
