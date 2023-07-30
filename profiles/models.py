from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Profile model, automatically created for each new user """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ilgf09'
    )

    class Meta:
        """ Sorting rule for profiles """
        ordering = ['-created_at']

    def __str__(self):
        """ Returns '(owner)'s profile' """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """ Create new profile for each new user and assigns owner """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
