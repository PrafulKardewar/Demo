from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import datetime
import time
import random

def get_random_username():
    username = ''
    for item in range(1,random.randint(5,10)):      #7 8
        username = username + chr(random.randint(65,90))
    return username


def create_users(num):
    for item in range(num):
        try:
            User.objects.create_user(username=get_random_username(),
                                     email=get_random_username()+"@gmail.com",
                                     password=get_random_username())
            print('Normal -->  User Added Successfully....!')
            time.sleep(1)
        except:
            print('Duplicate -- Values generated ')

def create_super_users(num):
    for item in range(num):
        User.objects.create_superuser(username=get_random_username(),
                                 email=get_random_username() + "@gmail.com",
                                 password=get_random_username())
        print('Admin -->  User Added Successfully....!')
        time.sleep(1)

#manage.py add_sample_user_optional_param 7 --typeofuser super
#manage.py add_sample_user_optional_param 7
#manage.py add_sample_user_optional_param 7 --typeofuser guest
#manage.py add_sample_user_optional_param 7 --typeofuser abcd

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("numofusers",type=int)          #mandatory
        #parser.add_argument("-p","--typeofuser",type=str)  # optional param #   staff --> staff --> super --> superuser
        parser.add_argument("-a", "--present", action="store_true")   # flag arg

    def handle(self, *args, **kwargs):
        num = kwargs.get('numofusers')  # int
        usertype = kwargs.get('present') # str

        if usertype:
            create_super_users(num) # super user added means
        else:
            create_users(num)
        print('All Users Added Successfully....!')

