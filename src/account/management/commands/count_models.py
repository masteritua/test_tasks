from django.core.management.base import BaseCommand, CommandError
from account.models import User, Profile, Log


class Command(BaseCommand):
    help = 'Command that prints all models and object counts'

    def handle(self, *args, **options):
        print(f"Models: User count'{User.objects.count()}', "
              f"Profile count'{Profile.objects.count()}',  "
              f"Log count'{Log.objects.count()}',")
