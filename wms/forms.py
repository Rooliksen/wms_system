from django import forms

from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']
        labels = {'name': 'Наименование:'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Запись:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
