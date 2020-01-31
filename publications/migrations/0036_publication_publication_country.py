# Generated by Django 2.2.9 on 2020-01-31 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('publications', '0035_auto_20200131_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='publication_country',
            field=models.ForeignKey(default='NL', on_delete=django.db.models.deletion.CASCADE, to='countries_plus.Country'),
            preserve_default=False,
        ),
    ]
