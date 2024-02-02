from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    #path('register/', register, name='register'),
    path('register/api/', Register.as_view(), name='register'),
    ]