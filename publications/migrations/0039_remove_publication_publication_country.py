# Generated by Django 2.2.9 on 2020-01-31 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0038_auto_20200131_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='publication_country',
        ),
    ]
