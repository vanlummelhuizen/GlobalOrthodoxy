# Generated by Django 2.2.9 on 2020-01-31 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('publications', '0034_auto_20200129_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='publication_country',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default='NL', on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='countries_plus.Country'),
            preserve_default=False,
        ),
    ]
