# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import complain


class ComplainForm(forms.Form):
    afm = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Give ΑΦΜ",
                "class": "form-control",
                'maxlength': '9'

            }
        ))
    infrastructure = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Give infrastructure ID",
                "class": "form-control",
                'maxlength': '36'
            }
        ))

    notes = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Give Additional Info",
                'size': '40',
                'maxlength': '300'
            }
        ))
    class Meta:
        model = complain
        fields = ['afm', 'infrastructure', 'notes']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
