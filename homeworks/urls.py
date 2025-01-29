from django.urls import path

from homeworks.views import HomeworksView

urlpatterns = [
    path("", HomeworksView.as_view(), name="homeworks"),
]
