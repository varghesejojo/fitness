
from django.db import models

class inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
