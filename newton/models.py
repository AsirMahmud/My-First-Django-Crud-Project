from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True,null=True)
    email = models.EmailField()
   
class Car(models.Model):
    id=models.AutoField(primary_key=True)
    car_name=models.CharField(max_length=255)
    speed=models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return  self.car_name 