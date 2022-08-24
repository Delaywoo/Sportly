
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Team, JoinPass
from .forms import JoinModelForm, JoinPassForm, RealJoinForm
from distutils.command.clean import clean
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView

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
    realjoinform=RealJoinForm()
    return render(request,'joinpw.html',{'joinpw':joinpwd, 'join_detail':join_detail, 'joinpass':joinin_form, 'realjoin':realjoinform})


@login_required(login_url='/login/')
def realjoin(request, join_id):
    team=get_object_or_404(Team,pk=join_id)    
    #input = RealJoin()
    #input.pw = request.POST['realjoinpw']
    inputpw = request.POST['realjoinpw']
    print(inputpw)
    #original = Team.objects.filter()
    original = get_object_or_404(Team,pk=join_id)
    originalpw = original.joinpw
    print(originalpw)
    if inputpw == originalpw:
        team.member.add(request.user)
        return redirect('myteamlist')
        #return render(request,'myteam_all.html') 원래
    else:
        return redirect('joinall') 

@login_required(login_url='/login/')
def myteamlist(request):
    myteams=Team.objects.filter(member=request.user)
    return render(request,'myteamlist.html',{'myteams':myteams})



"""
@login_required(login_url='/login/')
def joinin(request, join_id):
    #joinpwd =get_object_or_404(Team, pk=join_id)
    #join_detail =get_object_or_404(Team, pk=join_id)
    team=get_object_or_404(Team,pk=join_id)
    joinpassword = Team.objects.get(pk =join_id)
    join_filled = JoinPassForm(request.POST)
    #real_filled = Team(request.POST)
    if join_filled.is_valid():
        #real = get_object_or_404(Team, pk = join_id)
        realpassword = joinpassword.joinpw
        #real_filled.joinpw = get_object_or_404(Team, pk=joi
        # n_id)
        if realpassword == join_filled:
            team.member.add(request.user)
            return render(request,'myteam_log.html')
        else:
            return render(request,'myteam_log.html')
            redirect('joinall')
    else :
        #return render(request,'myteam_log.html')
        redirect('joinall')
"""
