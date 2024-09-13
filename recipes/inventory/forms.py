from django import forms
from .models import Ingredient

class addIngredients(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'qty', 'units', 'price']