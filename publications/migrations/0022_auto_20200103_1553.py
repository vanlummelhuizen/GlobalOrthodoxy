# Generated by Django 2.2.8 on 2020-01-03 14:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0021_auto_20200103_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
