# Generated by Django 2.2.10 on 2020-08-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0077_auto_20200812_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='coverfile',
        ),
    ]