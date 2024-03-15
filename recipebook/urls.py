"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from ledger.views import RecipeListView, RecipeDetailView
from ledger.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use the custom login view
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('ledger/', include('ledger.urls', namespace='ledger')),
    path('accounts/', include('django.contrib.auth.urls')),
]






