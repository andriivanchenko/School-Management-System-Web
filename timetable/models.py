from django.db import models

DAY_CHOICES = (
    ('Понеділок', 'Понеділок'),
    ('Вівторок', 'Вівторок'),
    ('Середа', 'Середа'),
    ('Четвер', 'Четвер'),
    ('П\'ятниця', 'П\'ятниця'),
    ('Субота', 'Субота'),
    ('Неділя', 'Неділя'),
)


class Timetables(models.Model):
    time_table_id = models.AutoField(primary_key=True, verbose_name="time_table_id")
    time_table_group_id_ref = models.ForeignKey(
        'groups.UserGroup',
        on_delete=models.CASCADE,
        verbose_name="time_table_group_id_ref",
        null=True,
        db_column="time_table_group_id_ref"
    )
    time_table_cabinet = models.SmallIntegerField(verbose_name="time_table_cabinet")
    time_table_start_time = models.TimeField(verbose_name="time_table_start_time")
    time_table_end_time = models.TimeField(verbose_name="time_table_end_time")
    time_table_day = models.CharField(choices=DAY_CHOICES, max_length=10, verbose_name="time_table_day")
    time_table_discipline_ref = models.ForeignKey(
        'DisciplineType',
        on_delete=models.CASCADE,
        verbose_name="time_table_discipline_ref",
        null=True,
        db_column="time_table_discipline_ref"
    )

    class Meta:
        db_table = "time_table"
        verbose_name = "Timetable"
        verbose_name_plural = "Timetables"
        ordering = ['time_table_id']

    def __str__(self):
        return f"{self.time_table_group_id_ref} - {self.time_table_day} - {self.time_table_start_time}"


class DisciplineType(models.Model):
    discipline_id = models.AutoField(primary_key=True, verbose_name="discipline_id")
    discipline_name = models.CharField(max_length=255, verbose_name="discipline_name")

    class Meta:
        db_table = "disciplines"
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"
        ordering = ['discipline_id']

    def __str__(self):
        return f"{self.discipline_name}"


class TeacherDiscipline(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    teacher_id = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name="teacher_id",
        db_column="teacher_id"
    )
    discipline_id = models.ForeignKey(
        'DisciplineType',
        on_delete=models.CASCADE,
        verbose_name="discipline_id",
        db_column="discipline_id"
    )

    class Meta:
        db_table = "teacher_discipline"
        verbose_name = "TeacherDiscipline"
        verbose_name_plural = "TeacherDisciplines"
        ordering = ['id']

    def __str__(self):
        return f"{self.teacher_id} - {self.discipline_id}"