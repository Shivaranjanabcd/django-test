from django import forms
from django.forms import ModelForm 
from . models import app

class app_form(ModelForm):
    class Meta:
        model = app
        fields = "__all__"