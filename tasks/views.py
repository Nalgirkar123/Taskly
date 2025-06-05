from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task
from django.contrib import messages
from .forms import TaskForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Login failed. Please check your credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='complete').count()
    pending_tasks = tasks.exclude(status='complete').count()
    overdue_tasks = tasks.exclude(status='complete').filter(due_date__lt=timezone.now()).count()
    progress_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    upcoming_tasks = tasks.exclude(status='complete').filter(due_date__gte=timezone.now()).order_by('due_date')[:5]
    high_priority_tasks = tasks.filter(priority='High').exclude(status='complete')
    recent_activity = tasks.order_by('-id')[:5]

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'progress_percentage': int(progress_percentage),
        'upcoming_tasks': upcoming_tasks,
        'high_priority_tasks': high_priority_tasks,
        'recent_activity': recent_activity,
    }
    return render(request, 'dashboard.html', context)

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    status_filter = request.GET.get('status')
    if status_filter in dict(Task._meta.get_field('status').choices):
        tasks = tasks.filter(status=status_filter)
    return render(request, 'task_list.html', {'tasks': tasks, 'status_filter': status_filter})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('task_list')
        else:
            messages.error(request, "Error adding task. Please try again.")
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('task_list')
        else:
            messages.error(request, "Error updating task. Please try again.")
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    new_status = request.GET.get('status')
    
    if new_status in ['pending', 'complete']:
        task.status = new_status
        task.save()
        if new_status == 'complete':
            messages.success(request, "Task marked as complete!")
        else:
            messages.info(request, "Task marked as pending.")
    else:
        messages.error(request, "Invalid status update.")

    return redirect('task_list')
