from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from homeworks.models import Homeworks
from timetable.models import TeacherDiscipline
from users.models import Group

User = get_user_model()
# Create your views here.

class HomeworksView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        homeworks = Homeworks.objects.filter(home_work_group_id_ref=request.user.user_group_id_ref)

        context = {
            'homeworks': homeworks,
        }

        return render(request, 'homeworks/homeworks.html', context)
