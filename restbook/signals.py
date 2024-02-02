from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from restbook.models import Profile
from users.models import *



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:

        profile = instance.profile

    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()