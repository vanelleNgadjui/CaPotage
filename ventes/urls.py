from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ventes'

urlpatterns = [
   
    path("", views.ventes_list, name="list"),
    path("categorie/<int:categorie_id>/", views.ventes_list_categorie, name="ventes_list_categorie"),
    path("ventes-en-cours/", views.ventes_list_en_cours, name="ventes_list_en_cours"),

    path('vendeur/<int:vendeur_id>/', views.vendeur_profil, name='vendeur_profil'),

    path('<int:vente_id>/', views.vente_detail, name='vente_detail'),

    path('<int:vente_id>/submit_comment/', views.submit_comment, name='submit_comment'),
     path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    path('create/', views.vente_create, name='create'),
    path('<int:vente_id>/update/', views.vente_update, name='vente_update'),
    path('<int:vente_id>/delete/', views.vente_delete, name='vente_delete'),

    path('mes_ventes/', views.mes_ventes, name='mes_ventes'),

    path('<int:vente_id>/demande-achat/', views.demande_achat, name='demande_achat'),
    path('<int:demande_id>/traiter-demande/', views.traiter_demande, name='traiter_demande'),
    path('mes-demandes/', views.mes_demandes, name='mes_demandes'),

    path('chatapp/', include('chatapp.urls')),

]

# Configuration pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)