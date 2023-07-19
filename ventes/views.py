from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vente, DemandeAchat, Comment, Categorie
from chatapp.models import Room
from .forms import VenteForm, DemandeAchatForm, CommentForm
from django.contrib.auth import get_user_model, login
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

User = get_user_model()

def home(request):
    categories = Categorie.objects.all()
    ventes_en_cours = Vente.objects.filter(date_fin__gt=timezone.now())[:5]  # Modifier le nombre de ventes à afficher selon vos besoins
    produits_recherches = Vente.objects.all()[:5]  # Modifier le nombre de produits à afficher selon vos besoins

    return render(request, 'pages/home.html', {
        'categories': categories,
        'ventes_en_cours': ventes_en_cours,
        'produits_recherches': produits_recherches
    })



# views.py
def ventes_list(request):
    categories = Categorie.objects.all()
    ventes = Vente.objects.all()
    search_query = request.GET.get('search_query')

    if search_query:
        ventes = ventes.filter(produit__icontains=search_query)

    return render(request, 'ventes/ventes_list.html', {
        'categories': categories,
        'ventes': ventes,
    })

def ventes_list_categorie(request, categorie_id):
    categories = Categorie.objects.all()
    categorie = get_object_or_404(Categorie, id=categorie_id)
    ventes = Vente.objects.filter(categories=categorie)
    search_query = request.GET.get('search_query')

    if search_query:
        ventes = ventes.filter(produit__icontains=search_query)

    return render(request, 'ventes/ventes_list.html', {
        'categories': categories,
        'ventes': ventes,
    })

def ventes_list_en_cours(request):
    categories = Categorie.objects.all()
    ventes = Vente.objects.filter(date_fin__gte=timezone.now())
    search_query = request.GET.get('search_query')

    if search_query:
        ventes = ventes.filter(produit__icontains=search_query)

    return render(request, 'ventes/ventes_list.html', {
        'categories': categories,
        'ventes': ventes,
    })



@login_required
def vente_detail(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    comments = Comment.objects.filter(vente=vente, parent_comment=None)
    comment_form = CommentForm(initial={'vente': vente})

    if request.method == 'POST':
        # Vérifiez si l'utilisateur clique sur le lien "Discuter avec le vendeur"
        if 'chat_with_seller' in request.POST:
            # Créez un slug unique pour la salle de chat
            slug = slugify(vente.produit)

            # Créez la salle de chat entre le vendeur et l'acheteur s'ils ne sont pas déjà participants
            room, created = Room.objects.get_or_create(name=vente.produit, slug=slug)
            room.participants.add(request.user, vente.vendeur)

            # Redirigez l'utilisateur vers la salle de chat
            return redirect('chatapp:room', slug=slug)
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.vente = vente
                parent_comment_id = request.POST.get('parent_comment')
                if parent_comment_id:
                    parent_comment = Comment.objects.get(id=parent_comment_id)
                    comment.parent_comment = parent_comment
                comment.save()
                return redirect('ventes:vente_detail', vente_id=vente_id)
                
    return render(request, 'ventes/vente_detail.html', {
        'vente': vente,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def submit_comment(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.vente = vente
            comment.save()
            return redirect('ventes:vente_detail', vente_id=vente_id)
    else:
        comment_form = CommentForm()

    return render(request, 'ventes/vente_detail.html', {
        'vente': vente,
        'comment_form': comment_form
    })



@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return redirect('ventes:vente_detail', vente_id=comment.vente.id)
        else:
            comment_form = CommentForm(instance=comment)

        return render(request, 'ventes/edit_comment.html', {
            'comment': comment,
            'comment_form': comment_form
        })
    else:
        return redirect('ventes:vente_detail', vente_id=comment.vente.id)


@user_passes_test(lambda u: u.is_superuser)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    vente_id = comment.vente.id

    if request.method == 'POST':
        comment.delete()
        return redirect('ventes:vente_detail', vente_id=vente_id)

    return render(request, 'ventes/delete_comment.html', {'comment': comment})


@login_required
def vente_create(request):
    if request.user.role not in [User.Role.VENDEUR, User.Role.ACHETEUR_VENDEUR]:
        return redirect('ventes:list')

    if request.method == 'POST':
        form = VenteForm(request.POST, request.FILES)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.vendeur = request.user
            vente.save()
            form.save_m2m()
            return redirect('ventes:list')
    else:
        form = VenteForm()
    return render(request, 'ventes/vente_create.html', {'form': form})

@login_required
def vente_update(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    if vente.vendeur != request.user:
        return redirect('ventes:list')
    if request.method == 'POST':
        form = VenteForm(request.POST, request.FILES, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('ventes:list')
    else:
        form = VenteForm(instance=vente)
    return render(request, 'ventes/vente_update.html', {'form': form, 'vente': vente})

@login_required
def vente_delete(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    if vente.vendeur != request.user:
        return redirect('ventes:list')
    vente.delete()
    return redirect('ventes:list')


@login_required
def mes_ventes(request):
    ventes = Vente.objects.filter(vendeur=request.user)
    return render(request, 'ventes/mes_ventes.html', {'ventes': ventes})

@login_required
def demande_achat(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    if request.user.role not in [User.Role.ACHETEUR, User.Role.ACHETEUR_VENDEUR]:
        return redirect('ventes:list')

    if request.method == 'POST':
        form = DemandeAchatForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.acheteur = request.user
            demande.vente = vente
            demande.save()
            return redirect('ventes:list')
    else:
        form = DemandeAchatForm()
    
    return render(request, 'ventes/demande_achat.html', {'form': form, 'vente': vente})

@login_required
def traiter_demande(request, demande_id):
    demande = get_object_or_404(DemandeAchat, pk=demande_id)
    if demande.vente.vendeur != request.user:
        return redirect('ventes:list')

    if request.method == 'POST':
        # Récupérer l'action (accepter ou refuser) à partir du formulaire
        action = request.POST.get('action')
        if action == 'accepter':
            demande.acceptee = True
        elif action == 'refuser':
            demande.acceptee = False
        demande.traitee = True
        demande.save()
        # Envoyer une notification ou un message à l'acheteur pour l'informer de la décision
        
    return redirect('ventes:mes_demandes')

@login_required
def mes_demandes(request):
    if request.user.role in ['ACHETEUR', 'ACHETEUR_VENDEUR']:
        demandes = DemandeAchat.objects.filter(acheteur=request.user)
        return render(request, 'ventes/mes_demandes.html', {'demandes': demandes})
    elif request.user.role in ['VENDEUR', 'ACHETEUR_VENDEUR']:
        ventes = Vente.objects.filter(vendeur=request.user)
        demandes = DemandeAchat.objects.filter(vente__in=ventes)
        return render(request, 'ventes/mes_demandes.html', {'demandes': demandes})
    else:
        # Handle the case where the user does not have an appropriate role
        return redirect('ventes:list')


def recherche_ventes(request):
    if request.method == 'GET':
        categories = request.GET.getlist('categories')
        ventes = Vente.objects.filter(categories__in=categories).distinct()
        return render(request, 'ventes/recherche_ventes.html', {'ventes': ventes})