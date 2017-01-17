from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='description default text')
