from django.contrib import admin
from .models import Vente, DemandeAchat, Comment, Categorie

admin.site.register(Categorie)
admin.site.register(Vente)
admin.site.register(Comment)
admin.site.register(DemandeAchat)
