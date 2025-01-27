from django.contrib.auth import get_user_model
from django.shortcuts import render

from timetable.models import Timetables

User = get_user_model()

# Create your views here.

def timetable_view(request):
    if request.user.is_authenticated:
        timetables = Timetables.objects.filter(time_table_group_id_ref=request.user.user_group_id_ref_id)
    return render(request, 'timetable/timetable.html', {'timetables': timetables})