# Generated by Django 5.1 on 2024-08-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="point",
            field=models.IntegerField(default=1),
        ),
    ]
