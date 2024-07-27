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

# def tasks(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks.html', {'tasks': tasks})

def tasks(request):
    # Get the filter status from query parameters; default to 'all'
    status = request.GET.get('status', 'all')

    # Filter tasks based on the selected status
    if status == 'completed':
        tasks = Task.objects.filter(completed_status=True)
    elif status == 'incomplete':
        tasks = Task.objects.filter(completed_status=False)
    else:
        tasks = Task.objects.all()  # 'all' or any other value

    # Render the template with the filtered tasks and current status
    return render(request, 'tasks.html', {'tasks': tasks, 'current_status': status})

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

@require_POST
def status_change(request, task_id):
    task_id = request.POST.get('task_id')
    task = get_object_or_404(Task, id=task_id)
    
    completed_status = request.POST.get('completed_status')
    completed_status = completed_status.lower() == 'true'
    
    task.completed_status = completed_status
    task.save()
    
    return redirect('tasks')

    
    