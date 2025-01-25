from django.contrib import admin
from .models import UserGroup

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'group_name', 'group_teacher_id')
    search_fields = ('group_id', 'group_name', 'group_teacher_id')
    list_filter = ('group_id', 'group_name', 'group_teacher_id')

admin.site.register(UserGroup, UserGroupAdmin)