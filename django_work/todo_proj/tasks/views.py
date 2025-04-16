from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from .models import Task
from .forms import Taskform
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'tasks/signup.html',{'form':form})        





@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks=Task.objects.all().order_by('-created_at')
    else:
        tasks=Task.objects.filter(user=request.user).order_by('-created_at')

    

    if request.method=='POST':
        form=Taskform(request.POST,request.FILES)
        if form.is_valid():
            new_task=form.save(commit=False)
            new_task.user=request.user         #here im associating the task with the user
            new_task.save()
            return redirect('task_list')
    else:
        form=Taskform()    
    context={
        'tasks':tasks,
        'form' :form,
    }    
    return render(request,'tasks/task_list.html',context)

@login_required
def update_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if not request.user.is_superuser and task.user != request.user:
        return redirect('task_list')
    
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Taskform(instance=task)
    return render(request,'tasks/update_task.html',{'form':form,'task':task})     
   
@login_required
def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if not request.user.is_superuser and task.user != request.user:
        return redirect('task_list')
    if request.method=='POST':
        task.delete()
        return redirect('task_list')
    return render(request,'tasks/delete_task.html',{'task':task})
