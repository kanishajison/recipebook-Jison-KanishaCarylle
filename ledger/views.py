from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        print("get_context_data method is called")
        context = super().get_context_data(**kwargs)
        ingredients = self.object.ingredients.all()
        print("Ingredients:", ingredients)  # print ingredients, debugging
        context['recipe_ingredients'] = ingredients
        return context
