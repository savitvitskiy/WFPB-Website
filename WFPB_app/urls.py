from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("nutrition/", views.nutrition, name="nutrition"),
    path("meal_planner/", views.planner, name="meal_planner"),
    path("about/", views.about, name="about"),
]