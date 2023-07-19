from django.contrib import admin
from .models import User, Acheteur, Vendeur, AcheteurVendeur, AcheteurProfile, VendeurProfile, AcheteurVendeurProfile

admin.site.register(User)
admin.site.register(Acheteur)
admin.site.register(Vendeur)
admin.site.register(AcheteurVendeur)
