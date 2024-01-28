from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={}))
    password = forms.CharField(label="Login", widget=forms.PasswordInput(attrs={}))
