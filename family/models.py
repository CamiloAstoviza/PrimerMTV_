from tkinter.tix import Tree
from django.db import models
from numpy import datetime_data

class family(models.Model):
    Name = models.CharField(max_length=40)
    Lastname = models.CharField(max_length=40)
    Age = models.IntegerField()
    Date_of_Birth = models.DateField(auto_now=True,null=Tree, blank=True)
