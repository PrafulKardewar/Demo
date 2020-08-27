from django.core.management.base import BaseCommand




from django.contrib.auth.models import User
import  datetime
import time
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("numofusers",type=int)

    def handle(self, *args, **kwargs):
        num = kwargs.get('numofusers')  # int
        for item in range(num):
            User.objects.create_user(username="yogymax{}".format(item), email="yogymax{}@gmail.com".format(item), password="Yogymax{}".format(item))
            print('{} User Added Successfully....!'.format("yogymax{}".format(item)))
            time.sleep(1)

        print('All Users Added Successfully....!')