from django.db import models


# Create your models here.
class Sport(models.Model):
    key = models.CharField(max_length=255)
    active = models.BooleanField()
    group = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
