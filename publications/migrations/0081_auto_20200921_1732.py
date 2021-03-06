# Generated by Django 2.2.13 on 2020-09-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0080_auto_20200904_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='collection_context',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='publication',
            name='price',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, default=None, max_digits=10),
            preserve_default=False,
        ),
    ]
