from django.shortcuts import render
from WFPB_app.models import Category, Season, Seasonal, Resources
from .utils import search_food

# Create your views here.
def home(request):
    categories = Category.objects.all()
    seasons = Season.objects.all()
    seasonals = Seasonal.objects.all()
    context = {"categories": categories, "seasons": seasons, "seasonals": seasonals}
    return render(request, "home.html", context)


def nutrition(request):
    # return render(request, "nutrition.html")
    if request.method == 'POST':
        query = request.POST.get('query', '')
        api_key = "u6b0HO7rTfnJtfbgbehB5ThSQcqhABLg6dE9Pc2p"
        
        search_results = search_food(query, api_key)
        if search_results:
            return render(request, "nutrition.html", {"results": search_results["foods"]})
        else:
            return render(request, "nutrition.html", {"error": "No search results found."})
    else:
        return render(request, "nutrition.html")


def planner(request):
    return render(request, "meal_planner.html")


def about(request):
    resources = Resources.objects.all()
    context = {"resources": resources}
    return render(request, "about.html", context)
