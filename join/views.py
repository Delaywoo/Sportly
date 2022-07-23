from django.shortcuts import render

# Create your views here.
def joinall(request):
    return render(request, 'joinall.html')

def joinpw(request):
    return render(request,'joinpw.html')