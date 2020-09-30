from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text="Required. Add a valid email address"
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")


class CustomUserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email","profile_picture")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","profile_picture")

