import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from RestNoteBook import settings


class Rest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    restaurant_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    images = models.FileField(upload_to='images/',)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.restaurant_name

    def get_absolute_url(self):
        return reverse('visit', kwargs={'slug': self.slug})



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    avatar = models.ImageField(null=True, upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username




class ReviewModel(models.Model):
    notes = models.TextField(max_length=300)
    price = models.FloatField()
    date = models.DateField()


    def __str__(self):
        return self.notes



