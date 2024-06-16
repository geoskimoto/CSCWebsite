from django.db import models

# Create your models here.

class Bunk(models.Model):
    area = models.CharField(max_length=100)
    bunk_number = models.BigIntegerField(unique=True)
    reservation = models.CharField(max_length=100)  #need to make this a foreign key and have it reference a table with all members.

class Room(models.Model):
    room = models.CharField(max_length=100)


