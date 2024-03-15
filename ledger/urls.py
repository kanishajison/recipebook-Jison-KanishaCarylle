from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = "ledger"

urlpatterns = [
    path('', RecipeListView.as_view(), name='ledger_home'),  
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),  
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),  
]
