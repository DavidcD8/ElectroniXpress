# Generated by Django 4.2.3 on 2023-10-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0006_rename_ad_item_alter_location_name_delete_createad"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="is_sold",
        ),
        migrations.AddField(
            model_name="item",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
