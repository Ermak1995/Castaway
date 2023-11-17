from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Password', 'autocomplete': "new-password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'required': ''}),
        }
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off'})

