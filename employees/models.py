from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    birth_date = models.DateField()