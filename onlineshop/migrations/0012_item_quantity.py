# Generated by Django 4.2.3 on 2023-10-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0011_remove_item_create_on_item_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
