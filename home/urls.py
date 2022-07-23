from django.urls import path
from .views import *
<<<<<<< HEAD
from join.views import joinall

urlpatterns=[
    path('', home, name="home"),
    path('joinall', joinall, name="joinall" ),
=======
from mylog.views import mylog_list
from myteam.views import myteam_notice

urlpatterns=[
    path('', home, name="home"),
    path('mylog_list',mylog_list,name="mylog_list"),
    path('myteam_notice',myteam_notice,name="myteam_notice"),
>>>>>>> 5ffce5bf28603c9d7b6ac3db4c9ffc5d9cc66331
]
