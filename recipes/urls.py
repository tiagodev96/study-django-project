from django.urls import path

from .views import category, home, recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('<int:id>/', recipe, name='recipe'),
]
