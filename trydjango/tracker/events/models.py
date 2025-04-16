from django.db import models

# Create your models here.
class Event(models.Model):
    event_type=models.CharField(max_length=50)
    key_or_button=models.CharField(max_length=50)
    x=models.IntegerField(null=True,blank=True)
    y=models.IntegerField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.event_type}: {self.key_or_button}"