from django.db import models
from datetime import datetime


# Create your models here.
class UserData(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    # date = models.DateTimeField(auto_now_add=True)
    
