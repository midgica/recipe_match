from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipe

# Create your views here.


def index(request):
    template = loader.get_template('recipe_match/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def browse(request):
    template = loader.get_template('recipe_match/browse.html')
    recipe_list = Recipe.objects.order_by()
    context = {'recipe_list': recipe_list}
    return HttpResponse(template.render(context, request))

def match(request):
    template = loader.get_template('recipe_match/match.html')
    context = {}
    return HttpResponse(template.render(context, request))

def random(request):
    template = loader.get_template('recipe_match/random.html')
    context = {}
    return HttpResponse(template.render(context, request))

def menu(request):
    template = loader.get_template('recipe_match/menu.html')
    context = {}
    return HttpResponse(template.render(context, request))

def shopping_list(request):
    template = loader.get_template('recipe_match/shopping_list.html')
    context = {}
    return HttpResponse(template.render(context, request))

def inventory(request):
    template = loader.get_template('recipe_match/inventory.html')
    context = {}
    return HttpResponse(template.render(context, request))

def recipe(request):
    template = loader.get_template('recipe_match/recipe.html')
    context = {}
    return HttpResponse(template.render(context, request))
