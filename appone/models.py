from django.db import models


class Emp(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    balance = models.FloatField()
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='user_photos/',default='NA')
    active = models.BooleanField(default=True)

class Address(models.Model):
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    emps = models.ManyToManyField(Emp,related_name='adrs')

class Company(models.Model):
    name = models.CharField(max_length=10)
    desig = models.CharField(max_length=10)
    age = models.IntegerField()

# 0--> True -->     python --False