from django.contrib import admin
from WFPB_app.models import Category, Season, Seasonal, Resources, NutritionData

# Register your models here.
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Seasonal)
admin.site.register(Resources)
admin.site.register(NutritionData)
