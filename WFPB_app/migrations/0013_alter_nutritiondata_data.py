# Generated by Django 5.0.4 on 2024-06-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WFPB_app", "0012_nutritiondata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nutritiondata",
            name="data",
            field=models.TextField(),
        ),
    ]