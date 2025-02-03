from django.urls import path

from marks.views import MarksView

urlpatterns = [
    path('', MarksView.as_view(), name='marks'),
]
