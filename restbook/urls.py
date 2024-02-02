from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('addnote', AddNoteView.as_view(),  name='addnote'),
    path('profile/', profile, name='profile'),
    path('visit/<int:pk>/', visit, name='visit'),
]

