from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserChangeForm, CustomUserCreationFrom
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "name",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("name", )}), )
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("name", )}),)

admin.site.register(CustomUser, CustomUserAdmin)