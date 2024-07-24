from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    deadline=models.DateField(default=date.today)
    days_left=models.IntegerField(default=0)
    completed_status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
