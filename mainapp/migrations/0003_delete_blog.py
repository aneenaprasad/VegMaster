# Generated by Django 4.2.7 on 2023-12-21 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]