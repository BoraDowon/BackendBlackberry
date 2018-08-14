from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Django User model extension
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university_id = models.IntegerField(default=0)
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if Profile.objects.filter(user=instance):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)
