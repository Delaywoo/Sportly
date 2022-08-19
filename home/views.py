from django.shortcuts import render,redirect, get_object_or_404
from datetime import date
from .forms import ScheduleForm
from .models import Schedule
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
"""
def home1(request):
    # dateField가 오늘 날짜인 스케쥴만 전송 
    schedules = Schedule.objects.filter(date__range=[date.today(), date.today()]) #.order_by('time') 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = ScheduleForm(request.POST,request.FILES)
        if form.is_valid(): #정상적인 값이 입력된 경우
            unfinished = form.save(commit=False)
            unfinished.writer = request.user 
            unfinished.save()
        return redirect('home')
    else: #get 요청을 보낸 경우
        form = ScheduleForm()
    return render(request, 'home.html', {'schedules':schedules}, {'form':form})"""

def home(request):  #여기서 date_range에 오늘값이 아니라 화면에서 입력한 숫자가 들어가도록 해야함.
    return render(request, 'home.html')

def schedule_list(request):  #여기서 date_range에 오늘값이 아니라 화면에서 입력한 숫자가 들어가도록 해야함.
    if request.method == 'POST' or request.method == 'FILES':
        format = '%Y-%m-%d'
        date_choice=request.POST.get('date_choice')
    
        #date=datetime.datetime.strptime(date_choice,format)
        schedules = Schedule.objects.filter(date__range=[datetime.datetime.strptime(date_choice,format),datetime.datetime.strptime(date_choice,format)]) #.order_by('-date') #오늘 날짜만 가져옴.
        return render(request, 'home.html',{'schedules':schedules})
    else:
        #schedules = Schedule.objects.filter(date__range=[date.today(), date.today()])
        return render(request, 'home.html')

@login_required(login_url='/login/')
def schedulemodelformcreate(request): 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = ScheduleForm(request.POST,request.FILES)
        if form.is_valid(): #정상적인 값이 입력된 경우
            sche=Schedule()
            sche.title=request.POST.get('title')
            sche.writer=request.user
            format = '%Y-%m-%d'
            date=request.POST.get('date')
            sche.date= datetime.datetime.strptime(date,format)
            sche.save()
            #unfinished = form.save(commit=False)
            #unfinished.writer = request.user  #여기 unfinished.date는 입력받은 날짜를 넣어야함.
            #unfinished.save()
        return redirect('home')
    else: #get 요청을 보낸 경우
        form = ScheduleForm() #모델폼을 그대로 찍어 보내줘라.
    return render(request, 'home.html', {'form':form})

def schedule1(request):
    posts=Schedule.objects.filter().order_by('-sche_date') #최신글 순서로 정렬
    return render(request,'schedule1.html',{'posts':posts})
    
@login_required(login_url='/accounts/naver/login/')
def calendar(request):
    schedules = Schedule.objects.all()
    return render(request, 'home.html', {'schedules': schedules})
    