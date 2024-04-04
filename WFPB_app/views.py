from django.shortcuts import render
from WFPB_app.models import Category


# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "home.html", context)


def nutrition(request):
    return render(request, "nutrition.html")


def planner(request):
    return render(request, "meal_planner.html")


def about(request):
    return render(request, "about.html")
