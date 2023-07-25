from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
import os
from PIL import Image


User = get_user_model()

def upload_to(instance, filename):
    # Construction du chemin de stockage du fichier
    image_id = instance.id  # ID de la vente
    filename_base, filename_ext = os.path.splitext(filename)
    return f'ventes/{filename_base}{filename_ext}'


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Vente(models.Model):
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categorie)
    produit = models.CharField(max_length=100)
    description=models.TextField(default="")
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    date_debut = models.DateField(default=timezone.now)
    date_fin = models.DateField(default=timezone.now)
    photos = models.ImageField(upload_to='ventes/')
    comments = models.ManyToManyField(User, through='Comment', related_name='vente_comments')
  

    def delete(self, *args, **kwargs):
        self.photos.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class DemandeAchat(models.Model):
    acheteur = models.ForeignKey(User, on_delete=models.CASCADE)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    message = models.TextField()
    # montant_propose = models.DecimalField(max_digits=10, decimal_places=2)
    date_demande = models.DateTimeField(auto_now_add=True)
    acceptee = models.BooleanField(default=False)
    traitee = models.BooleanField(default=False)
    def __str__(self):
        return f"Demande d'achat #{self.id}" 

    
