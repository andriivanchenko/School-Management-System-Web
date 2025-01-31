from django.urls import path

from homeworks.views import HomeworksView, HomeworkDetailsView, HomeworkAnswerView

urlpatterns = [
    path("", HomeworksView.as_view(), name="homeworks"),
    path("<int:home_work_id>", HomeworkDetailsView.as_view(), name="homework_details"),
    path("<int:home_work_id>/answer", HomeworkAnswerView.as_view(), name="homework_answer"),
]
