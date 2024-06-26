# Generated by Django 5.0.4 on 2024-04-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WFPB_app", "0006_seasonal"),
    ]

    operations = [
        migrations.CreateModel(
            name="Season",
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
            ],
        ),
        migrations.RemoveField(
            model_name="seasonal",
            name="season",
        ),
        migrations.AddField(
            model_name="seasonal",
            name="seasons",
            field=models.ManyToManyField(to="WFPB_app.season"),
        ),
    ]
