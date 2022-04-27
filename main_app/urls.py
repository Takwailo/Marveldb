from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('heros/', views.heros_index, name='index'),
      path('heros/<int:hero_id>/', views.heros_detail, name='herodetail')
]