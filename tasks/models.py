from django.db import models

# Create your models here.

class ApiInfo(models.Model):
    slack_name = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
