from django.contrib.auth import get_user_model
from django.shortcuts import render

from timetable.models import Timetables, TeacherDiscipline

User = get_user_model()


def timetable_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_id=request.user.user_id)

        timetables = Timetables.objects.filter(time_table_group_id_ref=user.user_group_id_ref)

        timetables_with_teachers = {}

        for timetable in timetables:
            # Отримання вчителя по дисципліні
            teacher_discipline = TeacherDiscipline.objects.select_related('teacher_id').filter(
                discipline_id=timetable.time_table_discipline_ref
            ).first()

            if teacher_discipline:
                teacher = teacher_discipline.teacher_id
                teacher_name = f"{teacher.user_first_name} {teacher.user_last_name} {teacher.user_surname or ''}"
            else:
                teacher_name = "Не вказано" # Якщо вчителя не вказано
            if timetable.time_table_day not in timetables_with_teachers:
                timetables_with_teachers[timetable.time_table_day] = []

            timetables_with_teachers[timetable.time_table_day].append({
                'discipline': timetable.time_table_discipline_ref.discipline_name,
                'start_time': timetable.time_table_start_time,
                'end_time': timetable.time_table_end_time,
                'cabinet': timetable.time_table_cabinet,
                'teacher': teacher_name,
            })

    else:
        user = None
        timetables_with_teachers = {}

    # Контекст для передачи в шаблон
    context = {
        'user': user,
        'timetables_with_teachers': timetables_with_teachers,
    }

    return render(request, 'timetable/timetable.html', context)
