# Generated by Django 4.2.5 on 2023-09-25 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]