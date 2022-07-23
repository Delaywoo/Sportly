from django.shortcuts import render

# Create your views here.

#mylog_create.html을 보여주는 함수
def mylog_create(request):
    return render(request,'mylog_create.html')

#mylog_list.html을 보여주는 함수
def mylog_list(request):
    return render(request,'mylog_list.html')

#mylog_detail.html을 보여주는 함수
def mylog_detail(request):
    return render(request,'mylog_detail.html')

#schedule_create.html을 보여주는 함수
def schedule_create(request):
    return render(request,'schedule_create.html')