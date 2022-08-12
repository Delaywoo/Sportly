from django.urls import path
from .views import *

urlpatterns=[
    path('',joinall, name="joinall"),
    path('joinpw', joinpw, name="joinpw" ),
]