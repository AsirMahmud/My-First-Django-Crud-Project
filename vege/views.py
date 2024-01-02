from django.shortcuts import render,redirect
from .models import Receipe
from django.http import HttpResponse
# Create your views here.

def receipes(request):

    if request.method=="POST":
            data=request.POST
            print(data)
            name=data.get('name')
            description=data.get( 'description')
            img=request.FILES.get('img')
            Receipe.objects.create(

            name=name,
            description=description,
            img=img
            ) 
            
           
            return redirect('/receipes/')
    
    

    reci=Receipe.objects.all()
                              
    
    return render(request,'rs.html',context={'receipes':reci})

def delete(request,id):
      queryset=Receipe.objects.get(id=id)
      queryset.delete()
      return redirect('/receipes/')

def update(request,id):
      queryset=Receipe.objects.get(id=id)
       
      if request.method=="POST":
            data=request.POST

            name=data.get('name')
            description=data.get('description')
            img=request.FILES.get('img')

            queryset.name=name
            queryset.description=description
            queryset.img=img

            queryset.save()
            return redirect('/receipes/')
                  

      
      context={"receipes":queryset}
      return render(request,'update.html',context)