from django import forms
from .models import Join

class Joinform(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)