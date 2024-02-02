from django.contrib.auth.models import User
from django.db import models

class Rest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    restaurant_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    images = models.FileField(upload_to='images/', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.restaurant_name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username



