from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
)
from django.shortcuts import render, redirect
from .forms import ChangeRoleForm
from django.contrib import messages


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    # login_url = '/accounts/login/'  # Modifier l'URL de connexion si nécessaire
    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "address",
        "company_address",
        "business_sector",
        "profile_photo",
    ]

    # ...


    # We already imported user in the View code above,
    #   remember?
    model = User

    # Send the User Back to Their Own Page after a
    #   successful Update
    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        # Only Get the User Record for the
        #   User Making the Request
        return User.objects.get(
            username=self.request.user.username
        )


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


user_redirect_view = UserRedirectView.as_view()



@login_required
def change_role(request):
    user = request.user

    if request.method == 'POST':
        form = ChangeRoleForm(request.POST, user=user)  # Passez l'objet `User` en tant qu'argument `user` au formulaire
        if form.is_valid():
            new_role = form.cleaned_data['role']
            user.role = new_role
            user.save()
            messages.success(request, 'Votre rôle a été mis à jour avec succès.')
            return redirect('users:detail', username=user.username)
    else:
        form = ChangeRoleForm(user=user)  # Passez l'objet `User` en tant qu'argument `user` au formulaire

    return render(request, 'user/change_role.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SpyBookSignupForm(request.POST)
#         if form.is_valid():
#             form.custom_signup(request, form.user)
#             user = form.save(request)
#             login(request, user)
#             return redirect('signup_success')
#     else:
#         form = SpyBookSignupForm()

#     return render(request, 'account/signup.html', {'form': form})
