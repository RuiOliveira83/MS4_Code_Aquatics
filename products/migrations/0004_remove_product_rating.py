# Generated by Django 3.2.7 on 2021-10-19 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
