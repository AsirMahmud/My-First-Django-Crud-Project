from django.shortcuts import render,redirect
from .models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

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
    if request.GET.get('search'):
          print(request.GET.get('search'))
          reci=reci.filter(name__icontains=request.GET.get('search'))
    
    

    
                              
    
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


def login_page(request):
      if request.method=="POST":
            data=request.POST
            username=data.get('username')
            password=data.get('password')
            
            if  User.objects.filter(username=username).exists()==False:
                    messages.error(request,"Invalid Username And Password")
                    return redirect('/login/')
            user=authenticate(username=username,password=password)

            if user is None:
                  messages.error(request,'Invalid Password')
                  return redirect('/login/') 
            else:
                  login()
                  return redirect('/receipes/')
            
            

      
     


      return render(request,'login.html')
def register(request):
      if request.method=='POST':
           data=request.POST
           first_name=data.get('first_name')
           last_name=data.get('last_name')
           username=data.get('username')
           password=data.get('password')
          
           if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return  redirect('/register/')
            
           
           user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
           user.set_password(password)
           user.save()
           redirect('/register/')
           messages.success(request, "Account created succesfully") 
            


              
      return render(request,'register.html')