<<<<<<< HEAD
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import Customuser  #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.
#admin.site.register(Customuser,UserAdmin) # 등록
=======
from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=(
        'username',
        'user_id',
        'password',
        'email',
        'user_register_dttm'
    )

admin.site.register(User,UserAdmin)
>>>>>>> 0896b30a8ed8da04e50de5dafd52929b87d4a1da
