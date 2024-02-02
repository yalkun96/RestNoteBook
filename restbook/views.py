from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import images
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *
from .urls import *

def home(request):
    rest = Rest.objects.all()
    title = {'title': "Home"}
    return render(request, 'restbook/articles.html', {'rest': rest, 'title': title})

def articles(requst):
    pass


class AddNoteView(LoginRequiredMixin, CreateView):
    model = Rest
    form_class = AddForm
    template_name = 'restbook/addnote.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Set the user field to the currently logged-in user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def profile(request):
    prof = Profile.objects.all()
    title = {'title': "Profiles"}
    return render(request, 'restbook/profile.html', {'prof': prof})



def visit(request, id):

    return render(request, 'restbook/visit.html')