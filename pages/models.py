from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=100)
    train_no = models.IntegerField(default=0, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)
    arrival_time = models.DateTimeField('date published')
    departure_time = models.DateTimeField('date published')
    
     
class Ticket(models.Model):
    # train_no = models.IntegerField(default=0)
    #train = models.ForeignKey(to=Train)
    PNR = models.IntegerField(default=0)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)
    coach = models.CharField(max_length=100)
    fare = models.FloatField(blank=True, null=True)
    arrival_time = models.DateTimeField('date published')
    departure_time = models.DateTimeField('date published')
    seat_no = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    date = models.DateTimeField('date published')


class Coach(models.Model):
    fare = models.FloatField(blank=True, null=True)
    AC1 = models.CharField(max_length=100)
    AC2 = models.CharField(max_length=100)
    AC3 = models.CharField(max_length=100)
    Sleeper = models.CharField(max_length=100)
    General = models.CharField(max_length=100)
    train_no = models.IntegerField(default=0)
