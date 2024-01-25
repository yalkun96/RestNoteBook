from django.db import models

class Rest(models.Model):
    restaurant_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.notes





