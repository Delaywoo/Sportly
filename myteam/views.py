
import django
from django.shortcuts import redirect, render, get_object_or_404
from .models import Tactic,Notice
from django.utils import timezone
from .forms import TacticModelForm,NoticeModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def myteam_log(request):
    #팀원들의 log 모아오기.
    return render(request,'myteam_log.html')

@login_required(login_url='/login/')
def myteam_notice(request):
    posts=Notice.objects.filter().order_by('-date') #최신글 순서로 정렬
    return render(request,'myteam_notice.html',{'posts':posts})

@login_required(login_url='/login/')
def myteam_tactic(request):
    posts=Tactic.objects.filter().order_by('date') #최신글 순서로 정렬
    return render(request,'myteam_Tactic.html',{'posts':posts})

@login_required(login_url='/login/')
def notice_create(request):
    return render(request,'notice_create.html')

@login_required(login_url='/login/')
def tactic_create(request):
    return render(request,'tactic_create.html')

@login_required(login_url='/login/')
def noticemodelformcreate(request): 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = NoticeModelForm(request.POST,request.FILES)
        if form.is_valid(): #정상적인 값이 입력된 경우
            unfinished = form.save(commit=False)
            unfinished.writer = request.user 
            unfinished.save()
        return redirect('myteam_notice')
    else: #get 요청을 보낸 경우
        form = NoticeModelForm() #모델폼을 그대로 찍어 보내줘라.
    return render(request, 'notice_create.html', {'form':form})

@login_required(login_url='/login/')
def tacticmodelformcreate(request): 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = TacticModelForm(request.POST,request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.writer = request.user 
            unfinished.save()
        return redirect('myteam_tactic')
    else: 
        form = TacticModelForm() 
    return render(request, 'tactic_create.html', {'form':form})

@login_required(login_url='/login/')
def teamlog_comment(request):
    return render(request,'teamlog_comment.html')

@login_required(login_url='/login/')
def teamlog_detail(request):
    return render(request,'teamlog_detail.html')