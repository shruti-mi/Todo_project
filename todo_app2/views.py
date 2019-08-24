from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems

def todoView(request):
	all_todo_items = TodoItems.objects.all()
	return render(request,'todo.html', {'all_items': all_todo_items})

def addTodo(request):
	(TodoItems(content = request.POST['content'])).save()
	return HttpResponseRedirect('/todo/')

def deleteTodo(request , todo_id):
	(TodoItems.objects.get(id=todo_id)).delete()
	return HttpResponseRedirect('/todo/')