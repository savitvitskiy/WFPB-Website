# Generated by Django 5.0.4 on 2024-04-09 03:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WFPB_app", "0004_alter_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="static/img"),
        ),
    ]
