from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("~redirect/", view=views.user_redirect_view, name="redirect"),
    path("~update/", view=views.user_update_view, name="update"),
    path('change_role/', views.change_role, name='change_role'),
    path("<str:username>/", view=views.UserDetailView.as_view(), name="detail"),
]
