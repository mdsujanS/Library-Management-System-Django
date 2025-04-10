from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": ("input input-bordered w-full max-w-xs"),
                    "placeholder": ("Type here"),
                }
            )


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": ("input input-bordered w-full max-w-xs"),
                    "placeholder": ("Type here"),
                }
            )
