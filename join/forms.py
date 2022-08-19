

from django.forms import ModelForm, forms
from .models import *

class JoinModelForm(ModelForm):
    class Meta:
        model = Team
        fields =['title','subtitle','body','joinpw','photo']

class JoinPassForm(ModelForm):
    class Meta:
        model = JoinPass
        fields = ['joinpassword']

class RealJoinForm(ModelForm):
    class Meta:
        model = RealJoin
        fields = '__all__'

class RealPwdForm(ModelForm):
    class Meta:
        model = RealPwd
        fields = ['realpwd']
class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = ['input']

