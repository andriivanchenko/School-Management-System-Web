from django.contrib import admin
from .models import Homeworks

class HomeworksAdmin(admin.ModelAdmin):
    list_display = (
        "home_work_id",
        "home_work_name",
        "home_work_user_ref",
        "home_work_group_id_ref",
        "home_work_timetable_ref",
        "home_work_topic",
        "home_work_description",
        "home_work_deadline",
        "home_work_created_at",
    )

    search_fields = ("title", "description")

admin.site.register(Homeworks, HomeworksAdmin)