from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings #for media file
from django.conf.urls.static import static

urlpatterns=[
    path('',joinall, name="joinall"),
    path('modelformcreate/', modelformcreate ,name='modelformcreate'),
    path('joinpw/<int:join_id>', joinpw, name='joinpw'),
    path('joinpassword', joinpassword, name="joinpassword" ),
    path('joinin', joinin, name='joinin' )

]