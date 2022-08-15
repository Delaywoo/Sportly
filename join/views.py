
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Team, JoinPass
from .forms import JoinModelForm, JoinPassForm
from distutils.command.clean import clean
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def joinall(request):
    posts= Team.objects.all().order_by('-date')
    return render(request, 'joinall.html', {'posts':posts})

def joinpw(request):
    return render(request,'joinpw.html')


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
    join_detail =get_object_or_404(Team, pk=join_id)

    return render(request,'join_detail.html',{'join_detail':join_detail})

def joinpw(request, join_id):
    joinpwd =get_object_or_404(Team, pk=join_id)
    join_detail =get_object_or_404(Team, pk=join_id)
    joinin_form =JoinPassForm()
    return render(request,'joinpw.html',{'joinpw':joinpwd, 'join_detail':join_detail, 'joinpass':joinin_form})

#def joinpassword(request,join_id):
 #   if request.method == 'POST':
  #      realpassword = get_object_or_404(Team.joinpw, pk=join_id)
   #     realpassword == get_object_or_404(JoinPass.joinpassword, pk=join_id)
    #    return render(request,'joinall')

    #else :
     #   return render(request,'joinpw')    
    #pwd = Team.joinpw
    #form = JoinPassForm()
    #return render(request, 'joinpassword.html',{'form':form})

@login_required(login_url='/login/')
def joinin(request, join_id):
    joinpwd =get_object_or_404(Team, pk=join_id)
    join_detail =get_object_or_404(Team, pk=join_id)
    join_filled = JoinPassForm(request.POST)
    #real_filled = Team(request.POST)
    if join_filled.is_valid():
        real = get_object_or_404(Team, pk = join_id)
        realpassword = real.joinpw
        #real_filled.joinpw = get_object_or_404(Team, pk=join_id)
        if realpassword == join_filled:
            return render(request,'myteam_log.html')
        else:
            return render(request,'joinpw.html',{'joinpw':joinpwd, 'join_detail':join_detail})

    else :
        return render(request,'joinpw.html',{'joinpw':joinpwd, 'join_detail':join_detail})
