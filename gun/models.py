from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)