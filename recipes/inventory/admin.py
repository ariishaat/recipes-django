from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeReq, Purchase

# Register the models
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeReq)
admin.site.register(Purchase)