from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserRoles


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "user_id",
        "user_login",
        "user_first_name",
        "user_last_name",
        "user_surname",
        "user_phone",
        "user_email",
        "user_sex",
        "user_tax_number",
        "user_birthday",
        "user_role",
        "user_description",
        "user_created_at",
        "user_changed_at",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = ("user_login", "user_email")
    list_filter = ("user_role", "is_active", "is_staff", "is_superuser")

    fieldsets = (  # Поля для редагування нового юзера
        (None, {"fields": ("user_login", "user_email", "password")}),
        ("Personal Info", {
            "fields": (
                "user_first_name",
                "user_last_name",
                "user_surname",
                "user_phone",
                "user_sex",
                "user_tax_number",
                "user_birthday",
                "user_description",
            )
        }),
        ("Permissions", {
            "fields": (
                "user_role",
                "is_active",
                "is_superuser",
                "is_staff",
            )
        }),
    )

    add_fieldsets = (  # Поля для створення нового юзера
        (None, {
            "classes": ("wide",),
            "fields": (
                "user_login",
                "password1", # Пароль буде хешований
                "password2", # підтвердження паролю
                "user_first_name",
                "user_last_name",
                "user_surname",
                "user_phone",
                "user_email",
                "user_sex",
                "user_tax_number",
                "user_birthday",
                "user_role",
                "user_description",
                "is_active",
                "is_superuser",
                "is_staff",
            ),
        }),
    )

    filter_horizontal = ()
    ordering = ["user_login"]

    def save_model(self, request, obj, form, change):
        """
        Зміна пароля користувача
        """
        if 'password' in form.changed_data:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)


class UserRolesAdmin(admin.ModelAdmin):
    list_display = ("user_role_id", "user_role_name")
    search_fields = ("user_role_id", "user_role_name")
    list_filter = ("user_role_id", "user_role_name")


admin.site.register(UserRoles, UserRolesAdmin)
