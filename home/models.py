from django.db import models
import datetime
from django.utils import timezone


# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    stage_name = models.CharField(max_length=50)
    content = models.TextField()
    stage_number = models.IntegerField()

    def __str__(self):
        return f"{self.stage_name} is {self.stage_number} long"


class DateRel(models.Model):
    info_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.info_text
