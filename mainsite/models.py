from django.db import models
from django.utils import timezone
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

class StationTPTC(models.Model):
    stations = []
    with open('staticfiles/station_TPTC.csv','r', encoding='utf-8-sig') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        for row in rows:
            print("models.py的欄位輸出測試：")
            print(row)
            stations.append(row)
    i = 0
    for s in stations:
        s[i] = models.PositiveIntegerField(default=0)
        i = i+1 

