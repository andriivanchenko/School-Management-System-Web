from django.contrib import admin

from marks.models import Marks, MarkTypes


# Register your models here.

class MarksAdmin(admin.ModelAdmin):
    list_display = (
        "mark_id",
        "mark_value",
        "mark_teacher_id",
        "mark_student_id",
        "mark_discipline_type_ref",
        "mark_type",
        "homework_id_ref",
        "mark_created_at",
    )

    search_fields = ("mark_type", "mark_value")

admin.site.register(Marks, MarksAdmin)


class MarkTypesAdmin(admin.ModelAdmin):
    list_display = (
        "mark_type_id",
        "mark_type_name",
    )

admin.site.register(MarkTypes, MarkTypesAdmin)