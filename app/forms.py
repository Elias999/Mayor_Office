# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import crew

class NewCrew(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Memo Name",
                "class": "form-control",
                'maxlength': '20'

            }
        ))
    working_hours = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Working hours etc 12:00 - 16:00",
                "class": "form-control",
                'maxlength': '20'
            }
        ))

    crew_members = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Give crew name separeted with commas",
                'size': '40',
                'maxlength': '300'
            }
        ))

    complains_id = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Give complains_id separeted with commas",
                'size': '40',
                'maxlength': '300'
                }
        ))
    class Meta:
        model = crew
        fields = ['name', 'working_hours', 'crew_members' , 'complains_id']
