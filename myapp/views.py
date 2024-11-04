from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask, CreateNewProject


# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Jimmy'
    return render(request, 'about.html', {
        'username':username
    })

def hello (request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)


def project(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def task(request):
    #tasks = Task.objects.get(id=id)
    #tasks = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html',{
        'task': tasks
    })

def create_task(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'create_task.html',{
            'form':CreateNewTask()
        })
    else:
      Task.objects.create(title = request.POST['title'], 
                          description = request.POST['description'], project_id=2)
      return redirect('task')

def create_project(request):

    if request.method == 'GET':
         return render(request, 'create_project.html', {
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')

def project_detail(request, id):
    detail_project = get_object_or_404(Project, id=id)
    detail_task=Task.objects.filter(project_id=id)
    return render(request, 'detail.html',{
        'detail_project': detail_project,
        'detail_task': detail_task
    })


 
        


   