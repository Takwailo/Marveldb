from django.contrib import admin
from .models import Heros, Movie, Villian
# Register your models here.
admin.site.register(Heros)
admin.site.register(Movie)
admin.site.register(Villian)