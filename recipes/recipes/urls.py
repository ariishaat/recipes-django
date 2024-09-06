"""
URL configuration for recipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory.html', views.inventory_view, name='inventory_view'),
    path('delete_ingredient.html', views.delete_ingredient, name='delete_ingredient'),
    path('menu.html', views.menu_view, name='menu_view'),
    path('recipes.html', views.recipes_view, name='recipes_view'),
    path('purchases.html', views.purchases_view, name='purchases_view'),
    path('revenue.html', views.view_revenue, name='view_revenue'),
    path('profit.html', views.view_profit, name='view_profit'),
]
