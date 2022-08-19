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
        ('긴급 공지', '긴급 공지'),
        ('일반 공지', '일반 공지'),
        ('훈련 공지', '훈련 공지'),
        )
        widgets = {
            'tag':forms.RadioSelect}