

from django.forms import ModelForm
from .models import Team,JoinPass

class JoinModelForm(ModelForm):
    class Meta:
        model = Team
        fields =['title','subtitle','body','joinpw','photo']

class JoinPassForm(ModelForm):
    class Meta:
        model = JoinPass
        fields = '__all__'

