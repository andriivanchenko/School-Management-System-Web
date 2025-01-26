from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserRoles


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
        "user_group_id_ref",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = ("user_login", "user_email")

    list_filter = ("user_role", "is_active", "is_staff", "is_superuser")

    list_editable = (
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
        "user_group_id_ref",
        "is_active",
        "is_staff",
        "is_superuser",
    )

admin.site.register(CustomUser, CustomUserAdmin)


class UserRolesAdmin(admin.ModelAdmin):
    list_display = ("user_role_id", "user_role_name")
    search_fields = ("user_role_id", "user_role_name")
    list_filter = ("user_role_id", "user_role_name")

admin.site.register(UserRoles, UserRolesAdmin)


