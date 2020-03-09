# Generated by Django 2.2.10 on 2020-03-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0054_publication_extra_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='year_of_birth',
        ),
        migrations.AddField(
            model_name='author',
            name='extra_info',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='author',
            name='name_original_language',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='publication',
            name='editor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
