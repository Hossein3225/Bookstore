from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm , CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
            "username",
            "email",
            "is_superuser",
            ]

admin.site.register(CustomUser,CustomUserAdmin)
