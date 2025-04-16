from django.db import models

# Create your models here.
class newdb(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()