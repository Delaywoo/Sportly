import django
from django.shortcuts import redirect, render, get_object_or_404
from .models import Comment, Mylog
from django.utils import timezone
from .forms import MylogModelForm,CommentForm
# Create your views here.

#mylog_create.html을 보여주는 함수
def mylog_create(request):
    return render(request,'mylog_create.html')

#mylog_list.html을 보여주는 함수
def mylog_list(request):
    #작성한 로그들을 띄우는 코드
    #posts = Mylog.objects.all() 
    posts=Mylog.objects.filter().order_by('-log_date2') #최신글 순서로 정렬
    return render(request,'mylog_list.html',{'posts':posts})

#mylog_id번째 로그를 mylog_detail.html에 보여주는 함수
def mylog_detail(request, mylog_id):
    mylog_detail = get_object_or_404(Mylog, pk=mylog_id)
    comment_form = CommentForm()
    return render(request,'mylog_detail.html', {'mylog_detail':mylog_detail, 'comment_form':comment_form})

#schedule_create.html을 보여주는 함수
def schedule_create(request):
    return render(request,'schedule_create.html')

#장고 모델 폼
def modelformcreate(request): 
    if request.method == 'POST' or request.method == 'FILES': #해당되는 urls.py에서 요청한 대상이 post 요청을 보낸 경우
        form = MylogModelForm(request.POST,request.FILES)
        if form.is_valid(): #정상적인 값이 입력된 경우
            form.save() #form에서 입력된 값 저장
        return redirect('mylog_list')
    else: #get 요청을 보낸 경우
        form = MylogModelForm() #모델폼을 그대로 찍어 보내줘라.
    return render(request, 'mylog_create.html', {'form':form})

def create_comment(request, mylog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid(): 
        filled_form = filled_form.save(commit=False) #아직은 저장하지 말고 대기하라는 뜻.
        filled_form.post = get_object_or_404(Mylog, pk= mylog_id ) #게시물 id 불러옴
        filled_form.save() #이제 저장하세요.
    return redirect('mylog_detail',mylog_id)
"""
    #mood
def transition0(request):
    Mylog.mood='😡'
    Mylog.save()
    return redirect('mylog_create')

def transition1(request):
    
    Mylog.mood='😠'
    Mylog.save()
    return redirect('mylog_create')

def transition2(request):
    Mylog.mood='😐'
    Mylog.save()
    return redirect('mylog_create')

def transition3(request):
    Mylog.mood='🙂'
    Mylog.save()
    return redirect('mylog_create')

def transition4(request):
    Mylog.mood='😜'
    Mylog.save()
    return redirect('mylog_create')
"""