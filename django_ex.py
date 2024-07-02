from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Tak.objects.all()
    return render(request, 'task_list.html', {'tasks':tasks})
    