from django.db import models

class Move(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField()