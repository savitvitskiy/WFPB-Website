# Generated by Django 5.0.4 on 2024-04-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WFPB_app", "0005_alter_category_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Seasonal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("season", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="static/img"),
                ),
            ],
        ),
    ]
