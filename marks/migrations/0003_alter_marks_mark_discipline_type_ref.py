# Generated by Django 5.1.5 on 2025-01-26 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0002_alter_marks_homework_id_ref'),
        ('timetable', '0002_alter_teacherdiscipline_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='mark_discipline_type_ref',
            field=models.ForeignKey(db_column='mark_discipline_type_ref', on_delete=django.db.models.deletion.CASCADE, to='timetable.disciplinetype', verbose_name='mark_discipline'),
        ),
    ]
