# Generated by Django 2.2.10 on 2020-08-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0078_remove_publication_coverfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='filecategory',
            name='list_view_priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]