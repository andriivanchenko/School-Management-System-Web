from django.shortcuts import render

# Create your views here.

def timetable_view(request):
    return render(request, 'timetable/timetable.html')