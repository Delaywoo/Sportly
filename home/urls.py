from django.urls import path
from .views import *
from join.views import joinall
from mylog.views import mylog_list
from myteam.views import myteam_notice
from accounts.views import login,logout,signup

urlpatterns=[
    path('', home, name="home"),
    path('joinall', joinall, name="joinall" ),
    path('', home, name="home"),
    path('mylog_list',mylog_list,name="mylog_list"),
    path('myteam_notice',myteam_notice,name="myteam_notice"),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
]
