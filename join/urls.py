from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings #for media file
from django.conf.urls.static import static

urlpatterns=[
    path('',joinall, name="joinall"),
<<<<<<< HEAD
    path('joinpw', joinpw, name="joinpw" ),
    path('joinnew', joinnew, name="joinnew" ),
=======
    path('modelformcreate/', modelformcreate ,name='modelformcreate'),
    path('joinpw/<int:join_id>', joinpw, name='joinpw'),
    path('joinpassword', joinpassword, name="joinpassword" ),
    path('joinin', joinin, name='joinin' )

>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
]