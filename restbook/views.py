from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *

def home(request):
    rest = Rest.objects.all()
    title = {'title': "Home"}
    return render(request, 'restbook/home.html', {'rest': rest, 'title': title})

