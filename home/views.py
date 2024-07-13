from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            title = request.POST.get('title', '') 
            desc = request.POST.get('desc', '') 
            print(title,desc)
            new_task = Task(title=title,desc=desc)
            new_task.save()
    except:
        working=True
    return render(request,'home.html')

def tasks(request):
    tasks = Task.objects.all()  
    return render(request, 'tasks.html', {'tasks': tasks})
    