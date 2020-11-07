# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
import datetime
from todolist import forms
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request): #the index view
	todos = TodoList.objects.all() #quering all todos with the object manager
	categories = Category.objects.all()#getting all categories with object manager
	if request.method == "POST": #checking if the request method is a POST
		if "taskAdd" in request.POST: #checking if there is a request to add a todo
			title = request.POST["description"] #title
			date = str(request.POST["date"]) #date
			category = request.POST["category_select"] #category
			content = title + " -- " + date + " s" + category #content	
			TodoList.user=request.user
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() #saving the todo
			return redirect("/todolist") #reloading the page
		
		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo
		elif "taskUpdate" in request.POST: #checking if there is a request to update a todo
			checkedlist = request.POST["checkedbox"] #checked update 
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))
				print(todo)
				#edit_item(request,todo)
				return render(request,"edit_form.html",{"list_item_id":todo,"categories":categories})#updatingtodo
				#return redirect('/edititem',args={"list_item_id":todo,"categories":categories})


	return render(request, "index.html", {"todos": todos, "categories":categories})

def edit_item(request,id):
	categories = Category.objects.all()
	todo = TodoList.objects.get(id=id)#getting all categories with object manager
	if request.method == "GET":
		 #checking if the request method is a POST                      
		todo.title = request.GET["description"] #title
		todo.date = str(request.GET["date"]) #dates
		todo.Category = request.GET["category_select"] #category
		todo.save() #saving the todo
		return redirect("/todolist") #reloading the page
		


	return render(request, "edit_form.html", {"todos": todo, "categories":categories})
    
	
	

   
	