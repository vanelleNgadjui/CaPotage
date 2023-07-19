from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms as formApp


# Importing django.forms under a special namespace because of my old mistake
from django import forms as d_forms
from allauth.account.forms import SignupForm

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "company_address",
            "business_sector",
            "profile_photo",
        ]



class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_username": _(
                "This username has already been taken."
            )
        }
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "address",
            "company_address",
            "business_sector",
            "profile_photo",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )
        
# SpyBookSignupForm inherits from django-allauth's SignupForm
class SpyBookSignupForm(SignupForm):
    class Meta:
        model = User
        fields = ["username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "address",
            "company_address",
            "business_sector",
            "profile_photo",
            "role",  
        ]
    # Specify a choice field that matches the choice field on our user model
    role = d_forms.ChoiceField(choices=[("ACHETEUR", "Acheteur"), ("VENDEUR", "Vendeur"), ("ACHETEUR_VENDEUR", "AcheteurVendeur")])
    # Override the init method
    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super().__init__(*args, **kwargs)
        # Vérifier si 'autofocus' existe avant de le supprimer
        if 'autofocus' in self.fields["username"].widget.attrs:
            del self.fields["username"].widget.attrs["autofocus"]
      # Remove autofocus because it is in the wrong place  

    # Put in custom signup logic
    def custom_signup(self, request, user):
        # Set the user's type from the form reponse
        user.role = self.cleaned_data["role"]
        # Save the user's type to their database record
        user.save()        


class ChangeRoleForm(formApp.Form):
    role = formApp.ChoiceField(choices=[])  # Supprimez le paramètre `choices` lors de la création du champ

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupérez l'objet `User` depuis les arguments kwargs
        super().__init__(*args, **kwargs)

        if user:
            if user.role == User.Role.ACHETEUR:
                self.fields['role'].choices = [
                    (User.Role.VENDEUR, "Vendeur"),
                    (User.Role.ACHETEUR_VENDEUR, "AcheteurVendeur"),
                ]
            elif user.role == User.Role.VENDEUR:
                self.fields['role'].choices = [
                    (User.Role.ACHETEUR_VENDEUR, "AcheteurVendeur"),
                ]
            elif user.role == User.Role.ACHETEUR_VENDEUR:
                self.fields['role'].choices = [
                    (User.Role.VENDEUR, "Vendeur"),
                    (User.Role.ACHETEUR, "Acheteur"),
                ]


# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')