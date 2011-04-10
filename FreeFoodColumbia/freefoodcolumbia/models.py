from django.db import models

class Event(models.Model):
  date = models.DateTimeField()
  location = models.CharField(max_length = 50)
  description = models.CharField(max_length = 500)
  source = models.CharField(max_length = 100)
# Create your models here.
