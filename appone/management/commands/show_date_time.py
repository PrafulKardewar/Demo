from django.core.management.base import BaseCommand
import  datetime




class Command(BaseCommand):
    def handle(self, *args, **options):
        time = datetime.datetime.now()
        print('Current Time Is --> {}'.format(time))