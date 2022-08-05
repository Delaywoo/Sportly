from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Join
from .forms import JoinModelForm, CommentForm
from distutils.command.clean import clean
# Create your views here.
def joinall(request):
    posts= Join.objects.all().order_by('-date')
    return render(request, 'joinall.html', {'posts':posts})

def joinpw(request):
    return render(request,'joinpw.html')

def joinnew(request):
    return render(request,'joinnew.html')

def modelformcreate(request):
    if request.method =='POST' or request.method =='FILES':
        form = JoinModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit =False)
            post.save()
            return redirect('joinall')

    else: 
        form = JoinModelForm()
    return render(request, 'form_create.html', {'form' : form})


def joindetail(request, join_id):
    join_detail =get_object_or_404(Join, pk=join_id)
    comment_form =CommentForm()

    return render(request,'join_detail.html',{'join_detail':join_detail},{'comment_form':comment_form})

def create_comment(request, join_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form= filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Join, pk=join_id)
        finished_form.save()

    return redirect('joindetail', join_id)