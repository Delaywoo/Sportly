<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns=[
    path('',joinall, name="joinall"),
    path('joinpw', joinpw, name="joinpw" ),
=======
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

>>>>>>> c0466361541fa0c31472cb4d21a422deff3e789f
]