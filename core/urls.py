"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from user import views as user
from ventes import views as ventes
from . import views
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "400/",
        default_views.bad_request,
        kwargs={"exception": Exception("Bad Request!")},
    ),
    path(
        "403/",
        default_views.permission_denied,
        kwargs={"exception": Exception("Permission Denied")},
    ),
    path(
        "404/",
        default_views.page_not_found,
        kwargs={"exception": Exception("Page not Found")},
    ),
    path("500/", default_views.server_error),
    # path(
    #     "",
    #     TemplateView.as_view(template_name="pages/home.html"),
    #     name="home",
    # ),
    path("", ventes.home, name="home"), 
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    # path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("user.urls", namespace="users"),
    ),
    path(
        "ventes/", 
        include("ventes.urls", namespace="ventes")
    ),

    path(
        "accounts/", 
        include("allauth.urls")
    ),
    path("chatapp/",
        include("chatapp.urls" , namespace="chats")
    ),
    # path('categories', ventes.categories, name='categories'),

    # Your stuff: custom urls includes go here
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)