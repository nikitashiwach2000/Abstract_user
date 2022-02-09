# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'mobile_number', 'birth_date']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('mobie_number','birth_date')}),
    )


admin.site.register(MyUser, MyUserAdmin)
