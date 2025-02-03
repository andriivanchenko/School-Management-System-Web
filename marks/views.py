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

        marks = self.model.objects.filter(mark_student_id=request.user.user_id)
        return render(request, 'marks/marks.html', {'marks': marks})
