from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    user_login = forms.CharField(
        label="Логін",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть логін',
        }),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть пароль',
        }),
    )

    def clean(self):
        cleaned_data = super().clean()
        user_login = cleaned_data.get('user_login')
        password = cleaned_data.get('password')

        if user_login and password:
            user = authenticate(username=user_login, password=password)
            if not user:
                raise ValidationError("Неправильний логін або пароль")
        return cleaned_data

