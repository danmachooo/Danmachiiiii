from django.shortcuts import render

def index(request):
    return render(request, 'recipe/index.html')

def recipes(request):
    # In a real application, you would fetch the recipe data from the database
    return render(request, 'recipe/recipes.html')

def submit_recipe(request):
    if request.method == 'POST':
        # Handle form submission logic here
        # You would typically save the submitted recipe data to the database
        pass
    return render(request, 'recipe/submit_recipe.html')
