# Generated by Django 2.2.13 on 2020-07-23 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0076_filecategory_order_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedfile',
            options={'ordering': ('filecategory__order_index',)},
        ),
    ]