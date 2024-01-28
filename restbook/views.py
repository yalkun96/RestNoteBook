from django.core.files import images
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *
from .forms import *
from .urls import *

def home(request):
    rest = Rest.objects.all()
    title = {'title': "Home"}
    return render(request, 'restbook/articles.html', {'rest': rest, 'title': title})

def add_note(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:

                Rest.objects.create(
                    restaurant_name=form.cleaned_data['restaurant_name'],
                    cuisine=form.cleaned_data['cuisine'],
                    notes=form.cleaned_data['notes'],
                    images=form.cleaned_data['images']
                )
                return redirect('home')
            except IntegrityError:
                form.add_error(None, "Error: Duplicate entry or database integrity issue")
            except Exception as e:
                form.add_error(None, f"Error: {str(e)}")

    form = AddForm()
    return render(request, 'restbook/addnote.html', {'form': form})