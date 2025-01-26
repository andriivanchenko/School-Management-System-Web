from django.contrib.auth import get_user_model
from django.db import models
from groups.models import UserGroup

# Create your models here.

class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True, verbose_name='mark_id')
    mark_value = models.IntegerField(verbose_name='mark_value')
    mark_teacher_id = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='mark_teacher_id',
        db_column='mark_teacher_id',
        related_name='student_marks'  # унікальне ім'я для зворотнього зв'язку https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey.related_name
    )
    mark_student_id = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='mark_student_id',
        db_column='mark_student_id',
        related_name='teacher_marks'  # унікальне ім'я для зворотнього зв'язку https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey.related_name
    )
    mark_discipline_type_ref = models.ForeignKey('timetable.DisciplineType', on_delete=models.CASCADE, verbose_name='mark_discipline', db_column='mark_discipline')
    mark_type = models.ForeignKey('MarkTypes', on_delete=models.CASCADE, verbose_name='mark_type', db_column='mark_type')
    homework_id_ref = models.ForeignKey('homeworks.Homeworks', on_delete=models.CASCADE, verbose_name='homework_id', db_column='homework_id_ref', null=True)
    mark_created_at = models.DateField(auto_now_add=True, verbose_name='mark_created_at')

    class Meta:
        db_table = 'marks'
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'
        ordering = ['mark_id']

    def __str__(self):
        return self.mark_value

class MarkTypes(models.Model):
    mark_type_id = models.AutoField(primary_key=True, verbose_name='mark_type_id')
    mark_type_name = models.CharField(max_length=255, verbose_name='mark_type_name')

    class Meta:
        db_table = 'mark_types'
        verbose_name = 'Mark Type'
        verbose_name_plural = 'Mark Types'
        ordering = ['mark_type_id']

    def __str__(self):
        return self.mark_type_name




