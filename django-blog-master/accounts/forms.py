from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required. We\'ll send you a link to verify')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']