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