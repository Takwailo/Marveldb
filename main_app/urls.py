from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('heros/', views.heros_index, name='index'),
      path('heros/<int:hero_id>/', views.heros_detail, name='hero_detail'),
      path('heros/create/', views.HeroCreate.as_view(), name='hero_create'),
      path('heros/<int:pk>/update/', views.HeroUpdate.as_view(), name='hero_update'),
      path('heros/<int:pk>/delete/', views.HeroDelete.as_view(), name='hero_delete'),
]