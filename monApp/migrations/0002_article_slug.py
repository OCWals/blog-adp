# Generated by Django 4.2.5 on 2023-09-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]