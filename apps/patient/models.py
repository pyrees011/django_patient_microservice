from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

