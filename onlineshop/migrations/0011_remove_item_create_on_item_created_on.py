# Generated by Django 4.2.6 on 2023-10-09 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0010_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="create_on",
        ),
        migrations.AddField(
            model_name="item",
            name="created_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
