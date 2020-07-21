from django.db import models

# Create your models here.

class resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    education = models.TextField(blank=True)
    work = models.TextField(blank=True)
    skills = models.TextField(blank=True)