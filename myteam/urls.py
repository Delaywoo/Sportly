
from django.urls import path
from .views import *

urlpatterns = [
    path('mayteam_all', myteam_all, name="myteam_all"),
    path('myteam_notice/<int:join_id>',myteam_notice,name="myteam_notice"),
    path('myteam_log/<int:join_id>',myteam_log,name='myteam_log'),
    path('myteam_tactic/<int:join_id>',myteam_tactic,name='myteam_tactic'),
    path('notice_create/',notice_create,name='notice_create'),
    path('tactic_create/',tactic_create,name='tactic_create'),
    path('teamlog_comment/',teamlog_comment,name='teamlog_comment'),
    path('teamlog_detail/',teamlog_detail,name='teamlog_detail'),
    path('noticemodelformcreate/',noticemodelformcreate ,name='noticemodelformcreate'),
    path('tacticmodelformcreate/',tacticmodelformcreate ,name='tacticmodelformcreate'),
    path('<int:notice_pk>/checks/',checks,name='checks',)
]

