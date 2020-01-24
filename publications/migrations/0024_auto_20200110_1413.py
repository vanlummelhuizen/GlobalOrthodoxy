# Generated by Django 2.2.8 on 2020-01-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0023_auto_20200103_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='title_subtitle_european',
            new_name='title_subtitle_European',
        ),
        migrations.AlterField(
            model_name='publication',
            name='documents',
            field=models.ManyToManyField(blank=True, null=True, to='publications.Document'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='illustration_and_layout_type',
            field=models.ManyToManyField(blank=True, null=True, to='publications.IllustrationLayoutType'),
        ),
    ]