from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SchoolUser(BaseUserManager):
    def create_user(self, user_email, password, **extra_fields):
        if not user_email:
            raise ValueError(_("The Email must be set"))
        extra_fields.setdefault("is_active", True)  # Default for all users
        user = self.model(user_email=user_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(user_email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    """
    Кастомна модель користувача де використовується email як унікальний ідентифікатор
    """
    user_id = models.AutoField(primary_key=True)
    user_login = models.CharField(max_length=50, unique=True)
    # password вже є в AbstractBaseUser
    user_first_name = models.CharField(max_length=255)
    user_last_name = models.CharField(max_length=255)
    user_surname = models.CharField(max_length=255, default='')
    user_phone = models.CharField(max_length=20, default='')
    user_email = models.EmailField(unique=True)
    user_sex = models.CharField(max_length=1)
    user_birthday = models.DateField()
    user_role = models.CharField(max_length=50)
    user_tax_number = models.CharField(max_length=25, default='')
    user_description = models.TextField()
    user_created_at = models.DateTimeField(auto_now_add=True)
    user_changed_at = models.DateTimeField(auto_now=True)
    # user_group_id_ref = models.ForeignKey('CustomGroup', on_delete=models.CASCADE, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = SchoolUser()

    USERNAME_FIELD = 'user_login'
    REQUIRED_FIELDS = ['user_first_name', 'user_last_name', 'user_email', 'user_birthday', 'user_role']

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name} ({self.user_email})"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True