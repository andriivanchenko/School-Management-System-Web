from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "user_login",
        "user_first_name",
        "user_last_name",
        "user_surname",
        "user_phone",
        "user_email",
        "user_sex",
        "user_birthday",
        "user_role",
        "user_tax_number",
        "user_description",
        "user_created_at",
        "user_changed_at",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = ("user_login", "user_email")

