from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField(default=date.today)
    
    def __str__(self):
        return self.title
