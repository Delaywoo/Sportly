
from django.forms import ModelForm
from .models import Team, Member, JoinPass

class JoinModelForm(ModelForm):
    class Meta:
        model = Team
        fields ='__all__'

class JoinPassForm(ModelForm):
    class Meta:
        model = JoinPass
        fields = '__all__'