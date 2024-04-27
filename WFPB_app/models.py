from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField(default=True)
    image = models.ImageField(upload_to="static/img", null=True, blank=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name 

class Seasonal(models.Model):
    name = models.CharField(max_length=20)
    # season = models.CharField(max_length=20)
    season = models.ManyToManyField(Season, related_name="seasonals")
    image = models.ImageField(upload_to="static/img", null=True, blank=True)

    def __str__(self):
        return self.name