from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=100)
    #train_no = models.IntegerField()
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    #distance = models.IntegerField()
    #arrival_time = models.DateTimeField(datetime.time(datetime.now()))
    #departure_time = models.DateTimeField(datetime.time(datetime.now()))
    
     