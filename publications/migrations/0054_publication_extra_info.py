# Generated by Django 2.2.10 on 2020-03-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0053_auto_20200306_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='extra_info',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
