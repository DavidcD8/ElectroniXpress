# Generated by Django 4.2.6 on 2023-10-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0012_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
