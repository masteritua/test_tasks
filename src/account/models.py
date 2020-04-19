from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def save_log(sender, instance, created, raw, using, update_fields):
    action = instance.__class__.__name__

    if created:
        Log.objects.create(commit=False)
        Log.model_name = action
        Log.action = 'created'
    else:
        Log.objects.create(commit=False)
        Log.model_name = action
        Log.action = 'update'

    Log.save()


def delete_log(sender, instance, using):
    action = instance.__class__.__name__
    Log.objects.create(commit=False)
    Log.model_name = action
    Log.action = 'delete'
    Log.save()


class LogConfig(AppConfig):
    name = 'log'
    verbose_name = _('log')

    def ready(self):
        post_save.connect(save_log, sender=User)
        post_delete.connect(delete_log, sender=User)


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


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(null=True, blank=True, max_length=50)
    action = models.CharField(null=True, blank=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
