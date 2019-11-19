from django.db import models
from datetime import datetime, timedelta


# Create your models here.
"""class Book(models.Model):
    Source = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Train_Name = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    CC_fare = models.CharField(max_length=100)
    Ac3_fare = models.CharField(max_length=100)
    Ac2_fare = models.CharField(max_length=100)
    Ac1_fare = models.CharField(max_length=100)
    Departure_time = models.CharField(max_length=100)
    Arrival_time = models.CharField(max_length=10)"""


class Train(models.Model):
    name = models.CharField(max_length=100)
    train_no = models.IntegerField(default=0, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    #date = models.CharField(max_length=100)
    cc_fare = models.CharField(max_length=10,default=0)
    ac1_fare = models.CharField(max_length=100,default=0)
    ac2_fare = models.CharField(max_length=100,default=0)
    ac3_fare = models.CharField(max_length=100,default=0)
    distance = models.IntegerField(default=0)
    arrival_time = models.DateTimeField('Arrival Date')
    departure_time = models.DateTimeField('Departure Date')
    
     
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
