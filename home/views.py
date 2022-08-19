from django.shortcuts import render,redirect, get_object_or_404
from datetime import date
from mylog.models import Schedule
from mylog.forms import ScheduleForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
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
    return render(request, 'home.html', {'schedules':schedules}, {'form':form})

def home1(request): 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = ScheduleForm(request.POST,request.FILES)
        if form.is_valid(): #정상적인 값이 입력된 경우
            unfinished = form.save(commit=False)
            unfinished.writer = request.user 
            unfinished.save()
        return redirect('home')
    else: #get 요청을 보낸 경우
        form = ScheduleForm()
    return render(request, 'home1.html',{'form':form})

@login_required(login_url='/accounts/naver/login/')
def calendar(request):
    schedules = Schedule.objects.all()
    return render(request, 'home.html', {'schedules': schedules})
