# Generated by Django 4.2.3 on 2023-07-09 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0002_demandeachat_vente_remove_purchaserequest_buyer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='periode_vente',
        ),
        migrations.AddField(
            model_name='vente',
            name='date_debut',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vente',
            name='date_fin',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
