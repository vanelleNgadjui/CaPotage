from django.db import models 
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=20)
    participants = models.ManyToManyField(User)
    slug = models.SlugField(max_length=100, unique=True)  # Ajout du champ slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # Générer le slug à partir du nom de la salle
        super().save(*args, **kwargs)

    def __str__(self):
        return "Room : " + self.name + " | Slug : " + self.slug
   

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Message is :- "+ self.content