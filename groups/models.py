from django.db import models

class UserGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    group_teacher_id = models.ForeignKey(
        'users.CustomUser',  # Рядкове посилання на модель CustomUser
        on_delete=models.CASCADE,
        verbose_name="group_teacher_id",
        null=True
    )

    class Meta:
        db_table = "groups"
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ['group_id']

    def __str__(self):
        return self.group_name
