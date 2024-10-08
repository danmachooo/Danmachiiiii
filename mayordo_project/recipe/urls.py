from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('recipes/', views.recipes, name='recipes'),  # Recipes listing page
    path('submit-recipe/', views.submit_recipe, name='submit_recipe'),  # Recipe submission page
]
