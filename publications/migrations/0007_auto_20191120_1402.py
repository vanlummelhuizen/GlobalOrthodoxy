# Generated by Django 2.0.13 on 2019-11-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_auto_20191120_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.Country'),
        ),
    ]