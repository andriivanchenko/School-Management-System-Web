from django.contrib import admin

from timetable.models import DisciplineType, Timetables, TeacherDiscipline


# Register your models here.

class TimetableAdmin(admin.ModelAdmin):
    list_display = (
        "time_table_id",
        "time_table_group_id_ref",
        "time_table_cabinet",
        "time_table_start_time",
        "time_table_end_time",
        "time_table_day",
        "time_table_discipline_ref",
    )

    search_fields = ("title", "description")

admin.site.register(Timetables, TimetableAdmin)


class DisciplineTypeAdmin(admin.ModelAdmin):
    list_display = (
        "discipline_id",
        "discipline_name",
    )

    search_fields = ("title", "description")

admin.site.register(DisciplineType, DisciplineTypeAdmin)


class TeacherDisciplineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "teacher_id",
        "discipline_id",
    )

    search_fields = ("title", "description")

admin.site.register(TeacherDiscipline, TeacherDisciplineAdmin)