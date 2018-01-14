from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm, NewTodo 
from django.views.decorators.http import require_POST
# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('id')
    # form = TodoForm()
    form2 = NewTodo()
    context = {'todo_list': todo_list, 'form': form2}
    return render(request, 'todoapp/index.html', context)


@require_POST
def addTodo(request):
    # form = TodoForm(request.POST)
    form = NewTodo(request.POST)
    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        new_todo = form.save()
    return redirect('index')


def completTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    
    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')