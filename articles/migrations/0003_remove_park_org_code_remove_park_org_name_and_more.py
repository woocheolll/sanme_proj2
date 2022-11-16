# Generated by Django 4.1.3 on 2022-11-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_park"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="park",
            name="org_code",
        ),
        migrations.RemoveField(
            model_name="park",
            name="org_name",
        ),
        migrations.AlterField(
            model_name="park",
            name="created_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]
