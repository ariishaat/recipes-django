from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from itertools import groupby
from operator import attrgetter

from .models import Ingredient, MenuItem, RecipeReq, Purchase
from .forms import *

def home(request):
    return render(request, 'home.html')

def inventory_view(request):
    current_inventory = Ingredient.objects.all()
    return render(request, 'inventory.html', {'inventory': current_inventory})

def menu_view(request):
    menu = MenuItem.objects.all()
    return render(request,'menu.html', {'menu': menu})

def recipes_view(request):
    recipes = RecipeReq.objects.select_related('menu_item', 'ingredient').all()
    group_recipes = {}
    for menu_item, items in groupby(recipes, key=attrgetter('menu_item')):
        group_recipes[menu_item] = list(items)
    print(group_recipes)
    return render(request, 'recipes.html', {'group_recipes': group_recipes})

def purchases_view(request):
    purchases_made = Purchase.objects.all()
    return render(request, 'purchases.html', {'purchases': purchases_made})

def view_finances(request):
    revenue = Purchase.revenue()
    profit = Purchase.profit()
    return render(request, 'finances.html', {'revenue': revenue,'profit': profit})

def admin_login(request):
    return render(request,'admin-login.html')


## admin access only views:

def is_admin(user):
    # check if user is admin
    return user.is_superuser

@user_passes_test(is_admin)
def add_menu(request):
    if request.method == "POST":
        form = addMenu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_view')
    else:
        form = addMenu()
    return render(request, 'update-menu.html', {'form': form})

@user_passes_test(is_admin)
def add_ingredient(request):
    if request.method == "POST":
        form = addIngredients(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_view')
    else:
        form = addIngredients()
    return render(request, 'add-ingredient.html', {'form': form})

@user_passes_test(is_admin)
def update_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    
    if request.method == "POST":
        ## to update ingredient:
        if 'update' in request.POST:
            form = updateIngredients(request.POST, instance=ingredient)
            if form.is_valid():
                form.save()
                return redirect('inventory_view')
        ##to delete ingredient:
        elif 'delete' in request.POST:
            ingredient.delete()
            return redirect('inventory_view')
    else: 
        form = updateIngredients(instance=ingredient)
    
    return render(request, 'update-ingredient.html', {'form': form, 'inventory': ingredient})

@user_passes_test(is_admin)
def update_recipe(request):
    if request.method == "POST":
        form = updateRecipeReq(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_view')
    else:
        form = updateRecipeReq()
    return render(request, 'update-recipe.html', {'form': form})

@user_passes_test(is_admin)
def add_purchase(request):
    if request.method == "POST":
        form = addPurchase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchases_view')
    else:
        form = addPurchase()
    return render(request, 'update-purchases.html', {'form': form})


