from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .filters import HomeworksFilter
from .forms import HomeworkResponseForm
from .models import Homeworks

User = get_user_model()


class HomeworksView(View):
    model = Homeworks

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        homeworks = Homeworks.objects.filter(home_work_group_id_ref=request.user.user_group_id_ref)

        homework_filter = HomeworksFilter(
            request.GET,
            queryset=homeworks,
            request=request  # передаємо запит в фільтр за filters.py
        )

        context = {
            'homework_filter': homework_filter,
        }

        return render(request, 'homeworks/homeworks.html', context)


class HomeworkDetailsView(View):
    model = Homeworks

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        homework = get_object_or_404(Homeworks, home_work_id=kwargs['home_work_id'])
        form = HomeworkResponseForm()

        context = {
            'homework': homework,
            'homework_id': kwargs['home_work_id'],
            'form': form,
        }

        return render(request, 'homeworks/homework_details.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        homework = get_object_or_404(Homeworks, home_work_id=kwargs['home_work_id'])
        form = HomeworkResponseForm(request.POST)

        if form.is_valid():
            response = form.save(
                commit=False)  # TODO: зберігаємо форму та поки не комітимо в БД (виправити пілся тесту)
            response.home_work_id_ref = homework
            response.home_work_user_id_ref = request.user
            response.save()
            return redirect(reverse('homework_details', args=[homework.home_work_id]))

        context = {
            'homework': homework,
            'homework_id': kwargs['home_work_id'],
            'form': form,
        }

        return render(request, 'homeworks/homework_answer.html', context)  # TODO: перевід на сторінку з відводіддю


class HomeworkAnswerView(View):
    pass
