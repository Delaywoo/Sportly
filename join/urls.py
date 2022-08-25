from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings #for media file
from django.conf.urls.static import static
from myteam.views import myteam_log

urlpatterns=[
    path('',joinall, name="joinall"),
    path('modelformcreate/', modelformcreate ,name='modelformcreate'),
    path('joinpw/<int:join_id>', joinpw, name='joinpw'),
    path('realjoin/<int:join_id>',realjoin, name = 'realjoin'),

    path('myteamlist', myteamlist, name='myteamlist'),
    path('myteam_log',myteam_log,name='myteam_log'),
    #path('realjoin/<int:join_id',realjoin, name = 'realjoin')
]