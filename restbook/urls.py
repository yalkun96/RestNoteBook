from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('addnote', AddNoteView.as_view(),  name='addnote'),
    path('profile/', profile, name='profile'),
    path('visit/<slug:slug>/', visit, name='visit'),
    path('leave_comment/', leave_comment, name='leave_comment'),
    path('edit/<slug:slug>/', edit, name='edit'),
    path('delete/<slug:slug>/', delete_post, name='delete'),


]

