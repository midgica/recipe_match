from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.


def index(request):
    context = {}
    return render(request, 'recipe_match/index.html', context)

def browse(request):
    recipe_list = Recipe.objects.order_by()
    context = {'recipe_list': recipe_list}
    return render(request, 'recipe_match/browse.html', context)

def match(request):
    context = {}
    return render(request, 'recipe_match/match.html', context)

def random(request):
    context = {}
    return render(request, 'recipe_match/random.html', context)

def menu(request):
    context = {}
    return render(request, 'recipe_match/menu.html', context)

def shopping_list(request):
    context = {}
    return render(request, 'recipe_match/shopping_list.html', context)

def inventory(request):
    context = {}
    return render(request, 'recipe_match/inventory.html', context)

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipe_match/recipe.html', context)
