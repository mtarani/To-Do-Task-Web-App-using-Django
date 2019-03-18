from django.shortcuts import render,redirect
from .models import TodoList
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required

def add_task(request):
    if not request.user.is_authenticated:
        return render(request,'loginapp/login.html')
    success=False
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        date = str(request.POST["date"])
        time = str(request.POST["time"])
        date_time = date+" "+time;
        username = request.user.username
        Todo = TodoList(title=title, description=description, due_time=date_time, created_by=username)
        Todo.save()
        success=True;
        return render(request, "todolist/add_task.html", {"success": success})
    return render(request, "todolist/add_task.html", {"success": success})

def view_task(request):
    if not request.user.is_authenticated:
        return render(request,'loginapp/login.html')
    todos = TodoList.objects.filter(created_by=request.user.username)
    return render(request, "todolist/view_task.html", {"todos": todos})


def remove_task(request):
    todos = TodoList.objects.filter(created_by=request.user.username)
    if "taskDelete" in request.POST:
        checkedlist = request.POST.get("checkedbox", False)
        if(checkedlist):
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "todolist/remove_task.html", {"todos": todos})

def update_task(request):
    if not request.user.is_authenticated:
        return render(request,'loginapp/login.html')
    success=False
    if request.method == "GET":
        todo_id = request.GET.get('todo_id')
        todo = TodoList.objects.get(id=int(todo_id))
    if request.method == "POST":
        todo_id = request.POST["todo_id"];
        todo = TodoList.objects.get(id=int(todo_id))
        title = request.POST["title"]
        description = request.POST["description"]
        date = str(request.POST["date"])
        time = str(request.POST["time"])
        date_time = date+" "+time;
        todo.title = title
        todo.description = description
        todo.due_time = date_time
        todo.save() 
        success=True;
        return render(request, "todolist/update_task.html", {"success": success, "todo": todo})
    dt=todo.due_time
    dt=dt + timedelta(hours=5,minutes=30)
    return render(request, "todolist/update_task.html", {"success": success,
                                                        "todo": todo,
                                                        "date": str(dt).split()[0],
                                                        "time": str(dt).split()[1].split('+')[0]})
