from django.urls import path
from .views import HomePage


urlpatterns = [
    path("", HomePage, name="home_page"),
    path("", HomePage, name="home_page"),
    path("category/<slug:category_slug>/", HomePage, name="category_wise"),
]
