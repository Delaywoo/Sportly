from django.urls import path
from .views import *
from accounts import views as accounts_views


urlpatterns=[
    path('', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]
