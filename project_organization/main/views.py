from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Project, Tariff, Leader, ConsultationQueue
from .forms import ProjectForm, ConsultationQueueForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def tariffs(request):
    tariffs = Tariff.objects.all()
    return render(request, 'main/tariffs.html', {'tariffs': tariffs})

def leaders(request):
    leaders = Leader.objects.all()
    return render(request, 'main/leaders.html', {'leaders': leaders})

def become_client(request):
    if request.method == 'POST':
        form = ConsultationQueueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('consultation_queue')
    else:
        form = ConsultationQueueForm()
    return render(request, 'main/become_client.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'main/add_project.html', {'form': form})

def consultation_queue(request):
    queue = ConsultationQueue.objects.all()
    queue_count = queue.count()
    return render(request, 'main/consultation_queue.html', {'queue': queue, 'queue_count': queue_count})

def consultation_detail(request, pk):
    applicant = get_object_or_404(ConsultationQueue, pk=pk)
    return render(request, 'main/consultation_detail.html', {'applicant': applicant})

def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST) 
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:  
        form = UserCreationForm()  
    return render(request, 'registration/register.html', {'form': form})