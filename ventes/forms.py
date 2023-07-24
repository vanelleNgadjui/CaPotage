from django import forms
from .models import Vente, DemandeAchat, Comment, Categorie
from django.utils import timezone
class VenteForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Categorie.objects.all(), required=True, widget=forms.SelectMultiple(attrs={'class': 'textinput'}))
    produit = forms.CharField(widget=forms.TextInput(attrs={'class': 'textinput form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'textinput form-control'}))
    tarif = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'textinput form-control'}))
    date_debut = forms.DateField(widget=forms.DateInput(attrs={'class': 'textinput form-control'}))
    date_fin = forms.DateField(widget=forms.DateInput(attrs={'class': 'textinput form-control'}))
    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'textinput form-control'}))

    class Meta:
        model = Vente
        fields = ['produit', 'description', 'categories', 'tarif', 'date_debut', 'date_fin', 'photos']

class CommentForm(forms.ModelForm):
    parent_comment = forms.ModelChoiceField(
        queryset=Comment.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textinput form-control'}))
    class Meta:
        model = Comment
        fields = ['content', 'parent_comment']    

class DemandeAchatForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textinput form-control'}))
    class Meta:
        model = DemandeAchat
        fields = ['message']
