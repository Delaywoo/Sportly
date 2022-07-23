from django.shortcuts import render

# Create your views here.
def joinpw(request):
    if request.method == 'PASSWORD':
        pass
    else:
        return render(request,'joinall.html')