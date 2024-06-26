from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["-id"]
