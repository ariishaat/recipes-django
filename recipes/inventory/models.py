from django.db import models

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    pricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class MenuItem(models.model):
    name = models.CharField(max_length=200)
    pricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class RecipeReq(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    qty_req = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('menu_item', 'ingredient')

    def __str__(self):
        return f'{self.menu_item} requires {self.qty_req} of {self.ingredient}'
        
class Expense(models.Model):
    date = models.DateField(auto_now_add=True)
    menu_time = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'Purchase of {self.menu_time} on {self.date}'