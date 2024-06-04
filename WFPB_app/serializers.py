from rest_framework import serializers
from .models import NutritionData
from .nutrient_mapping import NUTRIENT_CATEGORIES

class NutritionDataSerializer(serializers.ModelSerializer):
    macronutrients = serializers.SerializerMethodField()
    vitamins = serializers.SerializerMethodField()
    minerals = serializers.SerializerMethodField()

    class Meta:
        model = NutritionData
        fields = ['id', 'macronutrients', 'vitamins', 'minerals']

    def get_macronutrients(self, obj):
        return {key: obj.data[key] for key in obj.data if NUTRIENT_CATEGORIES.get(key) == 'macronutrients'}

    def get_vitamins(self, obj):
        return {key: obj.data[key] for key in obj.data if NUTRIENT_CATEGORIES.get(key) == 'vitamins'}

    def get_minerals(self, obj):
        return {key: obj.data[key] for key in obj.data if NUTRIENT_CATEGORIES.get(key) == 'minerals'}