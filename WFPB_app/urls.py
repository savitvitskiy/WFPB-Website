from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.home, name="home"),
    path("nutrition/", views.nutrition, name="nutrition"),
    path("meal_planner/", views.planner, name="meal_planner"),
    path("about/", views.about, name="about"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)