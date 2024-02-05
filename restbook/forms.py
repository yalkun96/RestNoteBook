from django import forms
from .models import *
from .models import Rest

class AddForm(forms.ModelForm):
    class Meta:
        model = Rest
        fields = [ 'restaurant_name', 'cuisine', 'notes', 'images', 'is_published']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewModel
        fields = ['notes', 'price', 'date']





