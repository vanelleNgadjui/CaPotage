from django import forms
from .models import Vente, DemandeAchat, Comment, Categorie

class VenteForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Categorie.objects.all(), required=True, widget=forms.SelectMultiple)
    
    class Meta:
        model = Vente
        fields = ['produit','description', 'categories', 'tarif', 'date_debut', 'date_fin', 'photos']

class CommentForm(forms.ModelForm):
    parent_comment = forms.ModelChoiceField(
        queryset=Comment.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ['content', 'parent_comment']

        
class DemandeAchatForm(forms.ModelForm):
    class Meta:
        model = DemandeAchat
        fields = ['message']
