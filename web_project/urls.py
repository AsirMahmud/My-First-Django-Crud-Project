"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newton.views import home,about,contact
from vege.views import *
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='Home'),
    path('login/',login_page,name='Login'),
    path('register/',register,name='Register'),
    path ('about/',about,name='About'),
    path ('contact/',contact,name='Contact'),
    path('receipes/',receipes,name='Receipes'),
    path('delete/<id>/',delete,name='Delete'),
    path('update/<id>/',update,name="Update"),
    path('todo/',todos,name="Todo"),
    path('todo/tdelete/<id>/',todoDelete,name="TodoDelete"),
    path('todo/tupdate/<id>/',todoUpdate,name="ToUpdate"),
  
]
