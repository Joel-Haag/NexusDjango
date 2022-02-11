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
    list_order = models.IntegerField()

    def __str__(self):
        return f"{self.stage_name} performing on stage {self.stage_number} "


class Attraction(models.Model):
    title = models.CharField(max_length=200)
    list_order = models.IntegerField()

    def __str__(self):
        return self.title


class AboutInfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class DateRel(models.Model):
    info_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.info_text
