# Generated by Django 4.2.3 on 2023-07-23 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0013_remove_categorie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
