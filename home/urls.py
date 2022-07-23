from django.urls import path
from .views import *
from join.views import joinall

urlpatterns=[
    path('', home, name="home"),
    path('joinall', joinall, name="joinall" ),
]
