# Generated by Django 4.2.3 on 2023-07-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0015_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='photos',
            field=models.ImageField(upload_to=''),
        ),
    ]
