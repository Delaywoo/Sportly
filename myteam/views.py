from django.shortcuts import render

# Create your views here.

def myteam_log(request):
    return render(request,'myteam_log.html')

def myteam_notice(request):
    return render(request,'myteam_notice.html')

def myteam_tactic(request):
    return render(request,'myteam_Tactic.html')

def notice_create(request):
    return render(request,'notice_create.html')

def tactic_create(request):
    return render(request,'tactic_create.html')

def teamlog_comment(request):
    return render(request,'teamlog_comment.html')

def teamlog_detail(request):
    return render(request,'teamlog_detail.html')