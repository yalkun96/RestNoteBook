from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.files import images
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import *
from .forms import *
from .urls import *

def home(request):
    rest = Rest.objects.filter(is_published=1)
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
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def edit(request, slug):
    model = get_object_or_404(Rest, slug=slug)
    if request.user != model.user:
        # Redirect or show an error message indicating the user doesn't have permission
        return render(request, 'restbook/exceptions.html')

    form = AddForm(instance=model)

    if request.method == 'POST':
        form = AddForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'restbook/updatenote.html', {'form': form})

@login_required
def delete_post(request, slug):
    model = get_object_or_404(Rest, slug=slug)
    if request.user != model.user:
        # Redirect or show an error message indicating the user doesn't have permission
        return render(request, 'restbook/exceptions.html')

    if request.method == 'GET':
        return render(request, 'restbook/delete.html', {'model': model})

    elif request.method == 'POST':
        model.delete()
        return redirect('home')



@login_required()
def profile(request):
    prof = Profile.objects.get(user=request.user)
    title = {'title': "Profiles"}
    return render(request, 'restbook/profile.html', {'prof': prof})



def visit(request, slug):
    post = get_object_or_404(Rest, slug=slug)
    review = ReviewModel.objects.all()

    return render(request, 'restbook/visit.html', {'post': post, 'review': review})
@login_required()
def leave_comment(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'restbook/leave_comment.html', {'form': form})





