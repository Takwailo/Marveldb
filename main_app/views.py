from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Heros, Villian
from .forms import MovieForm

class HeroCreate(CreateView):
    model = Heros
    fields = '__all__'

class HeroUpdate(UpdateView):
  model = Heros
  fields = ['abilities', 'real_name']

class HeroDelete(DeleteView):
  model = Heros
  success_url = '/heros/'

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def heros_index(request):
    heros = Heros.objects.all()
    return render(request, 'heros/index.html', { 'heros': heros })

def heros_detail(request, hero_id):
    hero = Heros.objects.get(id=hero_id)
    movie_form = MovieForm()
    return render(request, 'heros/detail.html', {'hero':hero, 'movie_form':movie_form})

def add_movie(request, hero_id):
  form = MovieForm(request.POST)
  if form.is_valid():
    new_movie=form.save(commit=False)
    new_movie.hero_id= hero_id
    new_movie.save()
  return redirect ('hero_detail', hero_id=hero_id)

class VillianCreate(CreateView):
    model = Villian
    fields = '__all__'

class VillianUpdate(UpdateView):
  model = Villian
  fields = ['abilities', 'real_name']

class VillianDelete(DeleteView):
  model = Villian
  success_url = '/villians/'

def villians_index(request):
  villians = Villian.objects.all()
  return render(request, 'villians/index.html', { 'villians': villians })

def villian_detail(request, villian_id):
    villian = Villian.objects.get(id=villian_id)
    movie_form = MovieForm()
    return render(request, 'villians/detail.html', {'villian':villian, 'movie_form':movie_form})