# Generated by Django 4.2.3 on 2023-07-09 19:35

from django.db import migrations, models
import ventes.models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0003_remove_vente_periode_vente_vente_date_debut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandeachat',
            name='traitee',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vente',
            name='photos',
            field=models.ImageField(upload_to=ventes.models.upload_to),
        ),
    ]
