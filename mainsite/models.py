from django.db import models
from django.utils import timezone
import os
import csv
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class StationTRTC(models.Model):
    """with open('../staticfiles/station_TPTC.csv','r', encoding='utf-8-sig', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            pass
    """
#    i = 0
#    for s in rows:
#        s[i] = models.PositiveIntegerField(default=0)
#        i = i+1 

