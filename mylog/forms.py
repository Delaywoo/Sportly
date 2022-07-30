from xml.dom.minidom import Comment
from django import forms
from .models import Mylog,Comment

class MylogModelForm(forms.ModelForm): #괄호 안은 forms 안의 ModelForm을 상속받은 클래스라는 것을 의미
    class Meta: 
        model=Mylog #meta클래스 하에 어떤 모델을 기반으로 자동으로 입력받을 form을 만들 것인지 명시
        fields = ['log_date2','mood','learned','lacked','improve','photo','video']#어떤 입력값(필드)를 입력받을지 명시
                # list 안에 원하는 필드를 작성하면 됨.
                #모두 입력 받을거면 '__all__'이라고 우측에 쓰면 됨.
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']