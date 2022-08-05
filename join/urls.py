from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',joinall, name="joinall"),
    path('joinpw/', joinpw, name="joinpw" ),
    path('joinnew/', joinnew, name="joinnew" ),
    path('modelformcreate/', modelformcreate ,name='modelformcreate'),
    path('join_detail/<int:join_id>', joindetail, name='joindetail'),
    path('create_comment/<int:join_id>', create_comment, name='create_comment'),
]