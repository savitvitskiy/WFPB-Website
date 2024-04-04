from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField(default=True)
    image = models.FileField(upload_to="img/", blank=True)

    def __str__(self):
        return self.name