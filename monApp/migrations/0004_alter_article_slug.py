# Generated by Django 4.2.5 on 2023-09-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
