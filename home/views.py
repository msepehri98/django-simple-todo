from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoCreateForm, TodoUpdateForm
from django.contrib import messages


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, id):
    Todo.objects.get(id=id).delete()
    messages.success(request, 'Deleted successfully.', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            Todo.objects.create(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                created=form.cleaned_data['created']
            )
            messages.success(request, 'Created successfully.', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully.', 'success')
            return redirect('details', id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})




