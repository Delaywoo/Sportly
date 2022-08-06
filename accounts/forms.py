from django.contrib.auth.forms import UserCreationForm
from .models import Customuser

class SignupForm(UserCreationForm):
  class Meta:
    model = Customuser
    fields = ['username', 'password', 'nickname', 'useremail']
