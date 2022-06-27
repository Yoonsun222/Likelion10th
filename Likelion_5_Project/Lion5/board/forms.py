from dataclasses import field
from django import forms
from .models import Board

class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'
