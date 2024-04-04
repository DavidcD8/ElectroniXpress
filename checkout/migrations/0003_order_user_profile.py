# Generated by Django 4.2.3 on 2023-11-04 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("onlineshop", "0015_userprofile_default_country_and_more"),
        ("checkout", "0002_order_original_bag_order_stripe_pid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="onlineshop.userprofile",
            ),
        ),
    ]
