# Generated by Django 2.2.8 on 2020-01-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0018_auto_20200103_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.Country'),
        ),
    ]
