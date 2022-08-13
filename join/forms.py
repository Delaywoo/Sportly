

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

