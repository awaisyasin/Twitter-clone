from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'birth_date')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['new_password1'].label = 'Password'
        self.fields['new_password2'].label = 'Confirm Password'


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'