# Generated by Django 3.2.8 on 2021-10-31 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ImageField',
            new_name='image',
        ),
    ]
