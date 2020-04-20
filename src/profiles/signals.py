from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from profiles.models import Log


@receiver([post_delete, post_save])
def save_log(sender, instance, **kwargs):
    action = instance.__class__.__name__

    Log.objects.create(
        model_name=action,
    )



