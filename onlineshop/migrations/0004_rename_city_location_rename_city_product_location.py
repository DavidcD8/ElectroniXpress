# Generated by Django 4.2.5 on 2023-10-04 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0003_rename_profile_userprofile"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="City",
            new_name="Location",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="city",
            new_name="location",
        ),
    ]
