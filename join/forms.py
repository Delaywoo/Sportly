
from django.forms import ModelForm
from .models import Join, Comment

class JoinModelForm(ModelForm):
    class Meta:
        model = Join
        fields ='__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']