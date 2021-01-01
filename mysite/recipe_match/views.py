from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe, Category
from .convert_servings import convert_servings
import random as rand
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from .forms import SignupForm

# Create your views here.


def index(request):
    context = {}
    return render(request, 'recipe_match/index.html', context)

def browse(request, recipe_id = 0, desired_servings = 0):
    recipe_list = Recipe.objects.order_by('name')
    breakfast = Recipe.objects.filter(category='2').order_by('name')
    snack = Recipe.objects.filter(category='5').order_by('name')
    dinner = Recipe.objects.filter(category='3').order_by('name')
    dessert = Recipe.objects.filter(category='4').order_by('name')
    beverage = Recipe.objects.filter(category='1').order_by('name')
    #rand_breakfast = rand.randrange(len(breakfast))
    #rand_breakfast_recipe = breakfast[rand_breakfast]
    #rand_snack = rand.randrange(len(snack))
    #rand_snack_recipe = snack[rand_snack]    
    rand_dinner = rand.randrange(len(dinner))
    rand_dinner_recipe = dinner[rand_dinner]
    #rand_dessert = rand.randrange(len(dessert))
    #rand_dessert_recipe = dessert[rand_dessert]
    rand_beverage = rand.randrange(len(beverage))
    rand_beverage_recipe = beverage[rand_beverage]
    if recipe_id != 0:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        ingredient_list = convert_servings(recipe, desired_servings)
        instructions = recipe.instructions.split('`')
    else:
        recipe = None
        ingredient_list = []
        instructions = ""
    context = {'recipe_list': recipe_list,
               'breakfast': breakfast,
               'snack': snack,
               'dinner': dinner,
               'dessert': dessert,
               'beverage': beverage,
               #'rand_breakfast_recipe': rand_breakfast_recipe,
               #'rand_snack_recipe': rand_snack_recipe,
               'rand_dinner_recipe': rand_dinner_recipe,
               #'rand_dessert_recipe': rand_dessert_recipe,
               'rand_beverage_recipe': rand_beverage_recipe,
               'recipe_id': recipe_id,
               'desired_servings': desired_servings,
               'recipe': recipe,
               'ingredient_list': ingredient_list,
               'instructions': instructions}
    return render(request, 'recipe_match/browse.html', context)

def match(request):
    context = {}
    return render(request, 'recipe_match/match.html', context)

def menu(request):
    context = {}
    return render(request, 'recipe_match/menu.html', context)

def shopping_list(request):
    context = {}
    return render(request, 'recipe_match/shopping_list.html', context)

def inventory(request):
    context = {}
    return render(request, 'recipe_match/inventory.html', context)

def recipe(request, recipe_id, desired_servings):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredient_list = convert_servings(recipe, desired_servings)
    instructions = recipe.instructions.split('`')
    context = {'recipe': recipe,
               'ingredient_list': ingredient_list,
               'instructions': instructions}
    return render(request, 'recipe_match/recipe.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('browse')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
