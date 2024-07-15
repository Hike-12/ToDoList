from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            title = request.POST['title'] 
            desc = request.POST['desc']
            date=request.POST['date'] 
            print(title,desc)
            new_task = Task(title=title,desc=desc,date=date)
            new_task.save()
    except:
        working=True
    return render(request,'home.html')

def tasks(request):
    tasks = Task.objects.all()  
    return render(request, 'tasks.html', {'tasks': tasks})
    