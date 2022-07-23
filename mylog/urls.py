from django.urls import path
from .views import *

urlpatterns = [
    path('',mylog_list,name="mylog_list"),
    path('create/',mylog_create,name='mylog_create'),
    path('detail/',mylog_detail,name='mylog_detail'),
    path('schedule_create/',schedule_create,name='schedule_create'),
]