from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo


# Create your views here.

def home(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'home.html', context)
    
def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {'todo': todo}
    return render(request, 'details.html', context)

def addTodo(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        todo = Todo(title=title, content=content)
        todo.save()
        return HttpResponseRedirect('/') 
        
    else:
        return HttpResponse("Make sure you are sending a post request")
  
   
def deleteTodo(request, todo_id):
    item_to_delete = Todo.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect("/")
  

