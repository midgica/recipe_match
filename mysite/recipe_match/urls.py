from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('browse/<int:recipe_id>/<int:desired_servings>/', views.browse, name='browse'),
    path('match/', views.match, name='match'),
    path('menu/', views.menu, name='menu'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('inventory/', views.inventory, name='inventory'),
    path('recipe/', views.recipe, name='recipe'),
    path('recipe/<int:recipe_id>/<int:desired_servings>/', views.recipe, name='recipe'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    ]
