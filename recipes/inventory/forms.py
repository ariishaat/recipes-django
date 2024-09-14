from django import forms
from .models import Ingredient, MenuItem, RecipeReq, Purchase

class addIngredients(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'qty', 'units', 'price']

class addMenu(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'pricePerUnit']

class updateRecipeReq(forms.ModelForm):
    class Meta:
        model = RecipeReq
        fields = ['menu_item','ingredient','qty_req']
        menu_dropdown = {'menu_item': forms.Select(attrs={'class': 'form-control'})}

class addPurchase(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['date', 'menu_item']
        menu_dropdown = {'menu_item': forms.Select(attrs={'class': 'form-control'}),
        'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class updateIngredients(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'qty', 'units', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'qty': forms.TextInput(attrs={'class': 'form-control'}),
            'units': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }