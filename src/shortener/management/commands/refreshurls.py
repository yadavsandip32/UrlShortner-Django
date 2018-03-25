from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refreshes all kirr urls'

    def handle(self, *args, **kwargs):
        return KirrURL.objects.refresh_url()