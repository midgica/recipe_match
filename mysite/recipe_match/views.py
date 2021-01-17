from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe, Category, Menu, Selection, Food, Unit
from .convert_servings import convert_servings
from .convert_more_units import convert_more_units
from .make_shopping_list import make_shopping_list
import random as rand
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignupForm #, ConversionForm

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

def add(request, recipe_id, desired_servings):
    #if user is logged in, add to their menu
    if request.user.is_authenticated:
        #create a menu if it doesn't exist, then add recipe
        try:
            my_menu = Menu.objects.get(user = request.user)
        except Menu.DoesNotExist:
            my_menu = Menu.objects.create(user = request.user)

        recipe = Recipe.objects.get(pk=recipe_id)
        selection = Selection.objects.create(menu = my_menu, recipe = recipe,
                                             desired_servings = desired_servings)

        #stay on browse page
        return browse(request, recipe_id, desired_servings)
    #else redirect to login page
    else:
        context = {}
        return render(request, 'recipe_match/login.html', context)
    ###this login page needs the form as context, where is it?


def delete_recipe(request, selection_id):
    my_menu = Menu.objects.get(user = request.user)
    selection = Selection.objects.filter(pk = selection_id)
    selection.delete()

    context = {}
    return menu(request)
    

def menu(request):
    if not request.user.is_authenticated:
        context = {} ###needs form as context
        return render(request, 'recipe_match/login.html', context)
    else:
        try:
            my_menu = Menu.objects.get(user = request.user)
        except Menu.DoesNotExist:
            my_menu = Menu.objects.create(user = request.user)
        selections = my_menu.selection_set.all()
        context = {'menu': my_menu,
                   'selections': selections}
        return render(request, 'recipe_match/menu.html', context)

def shopping_list(request):
    if not request.user.is_authenticated:
        context = {} ###needs form as context
        return render(request, 'recipe_match/login.html', context)
    else:
        try:
            my_menu = Menu.objects.get(user = request.user)
        except Menu.DoesNotExist:
            my_menu = Menu.objects.create(user = request.user)
        selections = my_menu.selection_set.all()
        shopping_list = make_shopping_list(my_menu)
        context = {'menu': my_menu,
                   'selections': selections,
                   'shopping_list': shopping_list}
        return render(request, 'recipe_match/shopping_list.html', context)

def conversion(request, food=None, amount=None, units_in=None, units_out=None):
    all_foods = Food.objects.all().order_by('name')
    all_units = Unit.objects.all().order_by('abbr')
    new_amount = convert_more_units(food, amount, units_in, units_out)
    #form = ConversionForm
    context = {'all_foods': all_foods,
               'all_units': all_units,
               'food': food,
               'amount': amount,
               'units_in': units_in,
               'units_out': units_out,
               'new_amount': new_amount,
               #'form': form
               }
    return render(request, 'recipe_match/conversion.html', context)

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
