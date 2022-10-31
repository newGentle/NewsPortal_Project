from datetime import datetime
from django.db import models

# Create your models here.
class Appointment(models.Model):
    subscriber_name = models.CharField(max_length=64,)
    message = models.TextField()
    date = models.DateField(default=datetime.utcnow,)

    def __str__(self):
        return f'{self.subscriber_name}: {self.message}'

    