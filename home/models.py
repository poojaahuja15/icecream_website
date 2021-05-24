from django.db import models

# Create your models here.
class Flavors(models.Model):
        name = models.CharField(max_length=100)
        address = models.TextField()
        phone = models.CharField(max_length=12)
        city = models.CharField(max_length=50)
        email = models.CharField(max_length=255)
        flavour = models.TextField()

        def __str__(self):
                return self.name

class Contact(models.Model):
        f_name = models.CharField(max_length=25)
        email = models.CharField(max_length=255)
        phone = models.CharField(max_length=12)
        message = models.TextField()

        def __str__(self):
                return self.f_name