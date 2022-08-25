
import django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from mylog.models import Mylog
from .models import Tactic,Notice
from join.models import Team
from django.utils import timezone
from .forms import TacticModelForm,NoticeModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def myteam_log(request): #,team_id
    #팀원들의 log 모아오기.
    #this_team = get_object_or_404(Team, pk = team_id) #팀 이름을 구분키로 사용
    #members = User.objects.filter(id=this_team.member)
    #logs = Mylog.objects.filter(writer=members)
    logs= Mylog.objects.all().order_by('-log_date2')
    return render(request,'myteam_log.html',{'logs':logs}) #{'logs':logs}
    #return redirect ('myteam_log')

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

"""
@login_required(login_url='/login/')
def teamlog_detail(request,teamlog_id):
    myteamlog_detail=get_object_or_404(Mylog,pk=teamlog_id)
    return render(request,'teamlog_detail.html',{'myteamlog_detail':myteamlog_detail})
"""

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