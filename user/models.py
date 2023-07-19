from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        # ADMIN = "ADMIN", "Admin"
        ACHETEUR = "ACHETEUR", "Acheteur"
        VENDEUR = "VENDEUR", "Vendeur"
        ACHETEUR_VENDEUR = "ACHETEUR_VENDEUR", "AcheteurVendeur"

    # base_role = Role.ADMIN

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.ACHETEUR,
    )
    
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    company_address = models.CharField(max_length=255, blank=True)
    business_sector = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos", blank=True)
 

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)  # Appel à la méthode save() de la classe parente
        else:
            # Code supplémentaire à exécuter lorsque l'instance a déjà une clé primaire
            super().save(*args, **kwargs)

class AcheteurManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ACHETEUR)


class Acheteur(User):

    base_role = User.Role.ACHETEUR

    acheteur = AcheteurManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Uniquement pour Acheteurs"

class AcheteurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    acheteur_id = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=Acheteur)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ACHETEUR":
        AcheteurProfile.objects.create(user=instance)




class VendeurManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.VENDEUR)


class Vendeur(User):

    base_role = User.Role.VENDEUR

    vendeur = VendeurManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Uniquement pour Vendeurs"


class VendeurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendeur_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Vendeur)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "VENDEUR":
        VendeurProfile.objects.create(user=instance)



class AcheteurVendeurManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ACHETEUR_VENDEUR)


class AcheteurVendeur(User):

    base_role = User.Role.ACHETEUR_VENDEUR

    acheteur_Vendeur = AcheteurVendeurManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Uniquement pour Acheteurs et Vendeurs"

class AcheteurVendeurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    acheteur_Vendeur_id = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=AcheteurVendeur)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ACHETEUR_VENDEUR":
        AcheteurVendeurProfile.objects.create(user=instance)



