from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('match/', views.match, name='match'),
    path('random/', views.random, name='random'),
    path('menu/', views.menu, name='menu'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('inventory/', views.inventory, name='inventory'),
    path('recipe/', views.recipe, name='recipe'),
    path('<int:recipe_id>/', views.recipe, name='recipe'),
    path('<int:recipe_id>/<int:desired_servings>/', views.recipe_servings, name='servings'),
    ]
