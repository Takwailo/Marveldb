from django.db import models
from django.urls import reverse


# Create your models here.
class Heros(models.Model):
    name=models.CharField(max_length=100)
    abilities=models.CharField(max_length=200)
    real_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hero_detail', kwargs={'hero_id': self.id})

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    release_date = models.DateFiled()

    hero = models.ForeignKey(Heros, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie_name} released on {self.release_date}"
