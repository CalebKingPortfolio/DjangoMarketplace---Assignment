from typing import Self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Listing

from.models import Order

from.models import Messages

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = {"title", "description", "location", "price", "image", "type"}




class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = {"message"}
        labels = {"message": ""}
     

