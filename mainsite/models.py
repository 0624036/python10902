from django.db import models
from django.utils import timezone
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

class Visitor_202101(models.Model):
    date = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.date

class Visitor_202102(models.Model):
    date = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.date

class Visitor_202103(models.Model):
    date = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.date

class Visitor_202104(models.Model):
    date = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.date

class Visitor_202105(models.Model):
    date = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.date