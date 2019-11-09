from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    reputation = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
