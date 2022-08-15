from turtle import textinput
from xml.dom.minidom import Comment
from django import forms
from .models import Tactic, Notice

class TacticModelForm(forms.ModelForm):
    class Meta:
        model = Tactic
        fields=['title','date','photo','video','contents']

class NoticeModelForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields=['title','date','tag','contents','photo','video','datetime','location']

        TAG_CHOICES = (
        ('긴급', '긴급'),
        ('일반', '일반'),
        ('훈련', '훈련'),
        )
        widgets = {
            'name':forms.TextInput (
                attrs={'class':'notice-input','placeholder':'제목 입력'}
            ),
            'tag':forms.RadioSelect}