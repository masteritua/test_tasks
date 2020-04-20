from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    pass


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user')
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
