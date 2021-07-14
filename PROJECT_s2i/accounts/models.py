from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

