from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.forms import LoginForm, RegisterForm
from .serializer import UserSerializer
from .models import User

from rest_framework.views import APIView



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    extra_context = {'title': 'Authentication'}

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user
            login(request, user)

            # Redirect to the home page or any other desired page
            return redirect(reverse('home'))
        else:
            # Invalid credentials, raise AuthenticationFailed
            raise AuthenticationFailed("Invalid credentials")


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()
        return redirect(reverse('home'))





