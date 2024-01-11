from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todos(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        listItems=data.get('listItems')
        Todo.objects.create(listItems=listItems)  
         

    
    data=Todo.objects.all()
    
    context={'todoData':data}

   
    return render(request,'todolist.html',context=context)


def todoDelete (request,id):
       queryset=Todo.objects.get(id=id) 
       queryset.delete()
       return redirect('/todo/')

def todoUpdate(request,id):
      queryset=Todo.objects.get(id=id) 

      if request.method=="POST":
           data=request.POST
           listItems=data.get('listItems')
           queryset.listItems=listItems
           queryset.save()
           return redirect('/todo/')
           
      
      context={'todoItems':queryset}

      return render(request,'todoUpdate.html',context)
       


     