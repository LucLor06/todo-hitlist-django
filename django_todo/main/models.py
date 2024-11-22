from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ...
    
class Task(models.Model):
    user = models.ForeignKey('User', related_name='tasks', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=64)
    
    def __str__(self):
        return self.task
    