from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(title=title)
        return redirect('index')
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('index')

def delete(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect('index')
