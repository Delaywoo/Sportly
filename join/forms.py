<<<<<<< HEAD
from django import forms
from .models import Join

class Joinform(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
=======

from django.forms import ModelForm
from .models import Join, JoinPass

class JoinModelForm(ModelForm):
    class Meta:
        model = Join
        fields ='__all__'

class JoinPassForm(ModelForm):
    class Meta:
        model = JoinPass
        fields = '__all__'
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
