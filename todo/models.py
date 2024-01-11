from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
     
     listItems=models.CharField(max_length=40)
     completed=models.IntegerField(default=0)
     incompleted=models.IntegerField(default=0)
     
     