from django.db import models

# Create your models here.
class Heros(models.Model):
    name=models.CharField(max_length=100)
    abilities=models.CharField(max_length=200)
    real_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name