# Generated by Django 4.1.3 on 2022-11-10 01:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("day_time", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("park_address", models.CharField(max_length=80)),
                ("pet", models.BooleanField(default=False)),
                ("content", models.TextField()),
                (
                    "like_user",
                    models.ManyToManyField(
                        related_name="like_post", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
