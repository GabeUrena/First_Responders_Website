from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    department = models.CharField(max_length=225)