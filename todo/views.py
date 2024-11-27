from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

def login_view(request):
    "Login: a view  to validate if a user is validated or not"
    if request.method == "POST":
        form =  AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            """Initialize to the response data to variables"""
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(user=request.user, title=title, complete=False)
        return redirect('task-list')
    return render(request, 'todo/create_task.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})