from django.contrib.auth import get_user_model
from django.db import models

from groups.models import UserGroup
from timetable.models import Timetables

User = get_user_model()

class Homeworks(models.Model):
    home_work_id = models.AutoField(primary_key=True, verbose_name="home_work_id")
    home_work_name = models.CharField(max_length=255, verbose_name="home_work_name")
    home_work_user_ref = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="homework_user_ref", null=True)
    home_work_group_id_ref = models.ForeignKey(
        'groups.UserGroup',
        on_delete=models.CASCADE,
        verbose_name="home_work_group_id_ref",
        null=True,
        db_column="home_work_group_id_ref"
    )
    home_work_timetable_ref = models.ForeignKey(
        'timetable.Timetables',
        on_delete=models.CASCADE,
        verbose_name="home_work_timetable_ref",
        null=True,
        db_column="home_work_timetable_ref"
    )
    home_work_topic = models.CharField(max_length=255, verbose_name="home_work_topic")
    home_work_description = models.TextField(verbose_name="home_work_description")
    home_work_deadline = models.DateTimeField(verbose_name="home_work_deadline")
    home_work_created_at = models.DateTimeField(auto_now_add=True, verbose_name="home_work_created_at")

    class Meta:
        db_table = "homeworks"
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ['home_work_id']

    def __str__(self):
        return self.home_work_name


class HomeworkResponses(models.Model):
    home_work_response_id = models.AutoField(primary_key=True, verbose_name="home_work_response_id")
    home_work_id_ref = models.ForeignKey(
        'homeworks.Homeworks',
        on_delete=models.CASCADE,
        verbose_name="home_work_id_ref",
        db_column="home_work_id_ref"
    )
    home_work_response = models.TextField(verbose_name="homework_response")
    home_work_user_id_ref = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="home_work_user_id_ref",
        db_column="home_work_user_id_ref"
    )
    home_work_mark_id_ref = models.ForeignKey(
        'marks.Marks',
        on_delete=models.CASCADE,
        verbose_name="home_work_mark_id_ref",
        null=True,
        db_column="home_work_mark_id_ref"
    )
    home_work_response_created_at = models.DateTimeField(auto_now_add=True, verbose_name="home_work_response_created_at")

    class Meta:
        db_table = "homework_responses"
        verbose_name = "Homework Response"
        verbose_name_plural = "Homework Responses"
        ordering = ['home_work_response_id']

    def __str__(self):
        return self.home_work_response_id