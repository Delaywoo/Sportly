<<<<<<< HEAD
from django.urls import path
from .views import *
#from accounts import views as accounts_views #한 urs.pyl에서 모든 앱 url을 다 관리할 경우, 이름 충돌 방지를 위해 다른 이름(별명)으로 불러주기


urlpatterns=[
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
]
=======
from django.urls import path
from .views import *
from accounts import views as accounts_views


urlpatterns=[
    path('', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
