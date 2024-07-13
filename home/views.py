from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def tasks(request):
    return render(request,'tasks.html')