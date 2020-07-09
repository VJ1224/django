from django.db import models

# Create your models here.

class resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    education = models.CharField(max_length=10000, blank=True)
    work = models.CharField(max_length=10000, blank=True)
    skills = models.CharField(max_length=10000, blank=True)