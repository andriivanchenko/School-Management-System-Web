import django_filters
from django.contrib.auth import get_user_model

from homeworks.models import Homeworks
from timetable.models import DisciplineType

User = get_user_model()


class HomeworksFilter(django_filters.FilterSet):
    home_work_discipline_ref = django_filters.ModelChoiceFilter(
        label='Назва предмету',
        queryset=DisciplineType.objects.none()  # пустий `queryset`
    )

    class Meta:
        model = Homeworks
        fields = ['home_work_discipline_ref']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request is not None:
            user_group_id = request.user.user_group_id_ref_id  # Отримуємо ID групи користувача

            # Находим дисциплины, которые связаны с ДЗ этой группы
            disciplines = DisciplineType.objects.filter(
                homeworks__home_work_group_id_ref_id=user_group_id
            ).distinct()

            self.filters['home_work_discipline_ref'].queryset = disciplines
