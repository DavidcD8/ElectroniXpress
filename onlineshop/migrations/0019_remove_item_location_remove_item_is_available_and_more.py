# Generated by Django 5.0.1 on 2024-01-17 20:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0018_subscriber_alter_item_image_delete_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="location",
        ),
        migrations.RemoveField(
            model_name="item",
            name="is_available",
        ),
        migrations.DeleteModel(
            name="Location",
        ),
    ]
