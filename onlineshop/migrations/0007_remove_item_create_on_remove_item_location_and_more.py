# Generated by Django 4.2.5 on 2023-11-07 13:51

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0006_rename_ad_item_alter_location_name_delete_createad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='create_on',
        ),
        migrations.RemoveField(
            model_name='item',
            name='location',
        ),
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='new', max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
