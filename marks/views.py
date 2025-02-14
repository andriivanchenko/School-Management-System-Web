from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Marks

User = get_user_model()


class MarksView(View):
    model = Marks

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))

        marks_grouped_list = {}
        role = request.user.user_role.user_role_id
        if role == 2:
            marks = self.model.objects.filter(mark_teacher_id=request.user.user_id)
        else:
            marks = self.model.objects.filter(mark_student_id=request.user.user_id)
        for mark in marks:
            group_title = mark.mark_discipline_type_ref.discipline_name
            if role == 2:
                group_name = mark.mark_student_id.user_group_id_ref.group_name
                group_title = f"{group_title} - {group_name}"
            if group_title not in marks_grouped_list:
                marks_grouped_list[group_title] = []

            marks_grouped_list[group_title].append(mark)
        return render(request, 'marks/marks.html', {'marks_grouped_list': marks_grouped_list})
