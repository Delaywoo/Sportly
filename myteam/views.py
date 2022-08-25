
import django
from django.shortcuts import redirect, render, get_object_or_404
from .models import Tactic,Notice
from django.utils import timezone
from .forms import TacticModelForm,NoticeModelForm
from django.contrib.auth.decorators import login_required
from join.models import Team
from mylog.models import Mylog

# Create your views here.

@login_required(login_url='/login/')
def myteam_log(request):
    #팀원들의 log 모아오기.
    logs= Mylog.objects.all().order_by('-date')
    return render(request,'myteam_log.html',{'logs':logs})

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


#@require_POST
@login_required(login_url='/login/')
def checks(request, notice_pk):
    if request.user.is_authenticated: #로그인된 요저인 경우.
        notice = get_object_or_404(Notice, pk=notice_pk)

        if notice.check_users.filter(pk=request.user.pk).exists(): #해당 게시글을 좋아요한 사람중에 pk가 현재 유저의 pk랑 같은 것이 존재하는지 하지 않는지를 판단한다
           notice.check_users.remove(request.user) #왜 여기가 실행되지 않지?
           notice.check_count-=1
           notice.save()
            #notice.check_users.remove(request.user)
        else:
            notice.check_users.add(request.user) #왜 여기ㄴ가 실행되지 않지?
            notice.check_count+=1
            notice.save()
        return redirect('myteam_notice') # return redirect('articles:index')
    return redirect('myteam_notice') #return redirect('accouts:login')