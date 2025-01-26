from django.contrib import admin
from .models import Homeworks, HomeworkResponses


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

    search_fields = ("home_work_name", "home_work_description")

admin.site.register(Homeworks, HomeworksAdmin)


class HomeworkResponsesAdmin(admin.ModelAdmin):
    list_display = (
        "home_work_response_id",
        "home_work_id_ref",
        "home_work_response",
        "home_work_user_id_ref",
        "home_work_mark_id_ref",
        "home_work_response_created_at",
    )

admin.site.register(HomeworkResponses, HomeworkResponsesAdmin)