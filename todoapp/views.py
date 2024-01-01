from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    # return HttpResponse('Welcmoe to the app.')
    content = {'todos': todos}
    return render(request, 'index.html', context = content)


def create(request):
    # 1. to get data from frontend after user post method
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        # 2. query to create data in db
        Todo.objects.create(name=name, description=description, status=status)
        # Todo.objects.create(name2=name, description2=description, status2=status)
        # name2 = name ===> yesma key(name2) chai model ma j cha tei hunu parcha i.e for database
                    #  ===> and value (name) is the variable after the POST function inside create function
        return redirect('home')
    content = {'mode':'create'}
    return render(request, 'create.html', context=content)

# to get the values in the form
# def edit(request, pk):
#     todo = Todo.objects.get(id=pk)
#     # print(todo)
#     content = {'mode': 'edit',
#                'todo' : todo}
#     return render(request, 'create.html', context=content)

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.name = name
        todo.description = description
        todo.status = status
        todo.save() # save method is used to create or save in the db
        return redirect('home')
    # print(todo)
    content = {'mode': 'edit',
               'todo' : todo}
    return render(request, 'create.html', context=content)

# def delete(request, pk):
#     todo = Todo.objects.get(id=pk)
#     todo.delete()
#     return redirect('home')

# def delete_all(request):
#     Todo.objects.all().delete()
#     return redirect('home')

def delete(request, pk=None):
    if pk is not None:
        todo = Todo.objects.get(id=pk)
        todo.delete()
    else:
        todo = Todo.objects.all()
        todo.delete()
        # Todo.objects.all().delete()

    return redirect('home')