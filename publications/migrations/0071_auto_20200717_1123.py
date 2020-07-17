# Generated by Django 2.2.10 on 2020-07-17 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0070_publication_coverfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='filecategory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.FileCategory'),
        ),
    ]
