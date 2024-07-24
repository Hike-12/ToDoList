from django.shortcuts import render,redirect, get_object_or_404
from home.models import Task
from datetime import date,datetime
from django.views.decorators.http import require_POST
from .forms import TaskForm

# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            title = request.POST['title'] 
            desc = request.POST['desc']
            deadline=request.POST['deadline']
            deadline_date = datetime.strptime(deadline, '%Y-%m-%d').date()
            days_left= abs((date.today()-deadline_date).days)
            new_task = Task(title=title,desc=desc,deadline=deadline,days_left=days_left)
            new_task.save()
    except:
        working=True
    return render(request,'home.html')

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


    
    