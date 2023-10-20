from django.db import models
from . import views

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    amount=models.IntegerField()

    def __str__(self):
        return self.name