from django.shortcuts import render
from django.http import HttpResponse

def recipe_list(request):
    recipes = [
        {"name": "Recipe 1", "link": "/recipe/1"},
        {"name": "Recipe 2", "link": "/recipe/2"}
    ]
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_1(request):
    ingredients = [
        {"name": "tomato", "quantity": "3pcs"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "pork", "quantity": "1kg"},
        {"name": "water", "quantity": "1L"},
        {"name": "sinigang mix", "quantity": "1 packet"}
    ]
    return render(request, 'recipe_detail.html', {'recipe_name': 'Recipe 1', 'ingredients': ingredients})

def recipe_2(request):
    ingredients = [
        {"name": "garlic", "quantity": "1 head"},
        {"name": "onion", "quantity": "1pc"},
        {"name": "vinegar", "quantity": "1/2cup"},
        {"name": "water", "quantity": "1 cup"},
        {"name": "salt", "quantity": "1 tablespoon"},
        {"name": "whole black peppers", "quantity": "1 tablespoon"},
        {"name": "pork", "quantity": "1 kilo"}
    ]
    return render(request, 'recipe_detail.html', {'recipe_name': 'Recipe 2', 'ingredients': ingredients})
