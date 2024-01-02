from django.shortcuts import render
from django.http import HttpResponse

def home(request):


  people_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22},
    {'name': 'David', 'age': 35},
    {'name': 'Eva', 'age': 28}
  ]

  return render(request , 'index.html' ,context={'people_list':people_list})

def about(request):


    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
# Create your views here.
