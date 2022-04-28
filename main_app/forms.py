from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
  class Meta:
    model = Movie
    fields = ['movie_name', 'release_date']