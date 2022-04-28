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
      path('heros/<int:hero_id>/add_movie/', views.add_movie, name='add_movie'),
      path('heros/<int:hero_id>/assoc_villian/<int:villian_id>/', views.assoc_villian, name='assoc_villian'),
      path('villians/', views.villians_index, name='villians_index'),
      path('villians/<int:villian_id>/', views.villian_detail, name='villian_detail'),
      path('villians/create/', views.VillianCreate.as_view(), name='villian_create'),
      path('villians/<int:pk>/update/', views.VillianUpdate.as_view(), name='villian_update'),
      path('villians/<int:pk>/delete/', views.VillianDelete.as_view(), name='villian_delete'),
]