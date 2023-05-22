from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.core.exceptions import BadRequest


@login_required(login_url='/login')
def home(request):
    tasks = Task.objects.filter(author=request.user)
    context = {"tasks": tasks}
    return render(request, 'app/home.html', context)


@login_required(login_url='/login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'app/create_task.html', {'form': form})


@login_required(login_url='/login')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if task.author == request.user:
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request, 'app/update_task.html', {'form': form})
    else:
        raise BadRequest("You do not have permission to see this site")


@login_required(login_url='/login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.author == request.user:
        if request.method == 'POST':
            task.delete()
            return redirect('/')
        return render(request, 'app/delete_task.html', {'task': task})
    else:
        raise BadRequest("You do not have permission to see this site")


def change_task_completion(request, pk):
    task = Task.objects.get(id=pk)
    print(task.completed)
    task.completed = not task.completed
    print(task.completed)
    task.save()
    return redirect('/')




