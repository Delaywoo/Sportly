from django.urls import path
from .views import *

urlpatterns = [
    path('',mylog_list,name="mylog_list"),
    path('create/',mylog_create,name='mylog_create'),
    #path('detail/',mylog_detail,name='mylog_detail'),
    path('schedule_create/',schedule_create,name='schedule_create'),
    
    #장고 modelform을 이용한 객체 생성
    path('mylogmodelformcreate/',mylogmodelformcreate ,name='mylogmodelformcreate'),
    #각 log에 대한 detail 페이지 url은 127.0.0.1:8000/mylog_detail/(id) 가 될 것
    path('mylog_detail/<int:mylog_id>',mylog_detail,name='mylog_detail'),
    #댓글 작성
    path('create_comment/<int:mylog_id>', create_comment, name='create_comment'),
    #mood 변경
    path('schedulemodelformcreate/',schedulemodelformcreate,name='schedulemodelformcreate'),
    #삭제할 경로
    path('schedule1/',schedule1,name='schedule1'),
]