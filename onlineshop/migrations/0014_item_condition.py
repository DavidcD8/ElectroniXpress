# Generated by Django 4.2.6 on 2023-10-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0013_item_sku"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="condition",
            field=models.CharField(
                choices=[("new", "New"), ("used", "Used")], default="new", max_length=50
            ),
        ),
    ]
