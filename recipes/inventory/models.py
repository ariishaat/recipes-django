from django.db import models, transaction
from django.utils import timezone

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    qty = models.PositiveIntegerField()
    units = models.CharField(max_length=200, default="unit")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    pricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    def inventoryUpdate(self):
        with transaction.atomic():
            recipe_reqs = RecipeReq.objects.filter(menu_item=self)

            for item in recipe_reqs:
                ingredient = item.ingredient
                req_qty = item.qty_req

                if ingredient.qty < req_qty:
                    raise ValueError(f"Not enough {ingredient.name} in inventory!")
                ingredient.qty -= req_qty
                ingredient.save()
            Purchase.objects.create(menu_item=self)

class RecipeReq(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty_req = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('menu_item', 'ingredient')

    def __str__(self):
        return f'{self.menu_item} requires {self.qty_req} of {self.ingredient}'
        
class Purchase(models.Model):
    date = models.DateTimeField(default=timezone.now)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    @classmethod
    def revenue(cls):
        total = cls.objects.aggregate(total=models.Sum('menu_item__pricePerUnit'))['total']
        return total or 0 #zero for no purchases
    
    @classmethod
    def cost(cls):
        total_cost = 0
        purchases = cls.objects.all()
        for purchase in purchases:
            cost = sum(
                req.qty_req * req.ingredient.price for req in purchase.menu_item.recipe_requirements.all())
            total_cost += cost
        return total_cost
    
    @classmethod
    def profit(cls):
        revenue = cls.revenue()
        cost = cls.cost()
        return round(revenue - cost,2)

    def __str__(self):
        return f'Customer purchased {self.menu_item} on {self.date}!'
