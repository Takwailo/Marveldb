from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Heros

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
    return render(request, 'heros/detail.html', {'hero':hero})

