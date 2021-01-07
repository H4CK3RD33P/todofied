"""todofied URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',views.home,name='home'),
    #Authorisation
    ##sign-up
    path('signup/',views.signupuser,name='signupuser'),
    ##sign-in
    path('login/',views.loginuser,name='loginuser'),
    ##log out
    path('logout/',views.logoutuser,name='logoutuser'),
    #create todos
    path('create/',views.create_todo,name='create_todo'),
    #view all todos
    path('current/',views.current_todos,name='current_todos'),
    #view completed todos only
    path('completed/',views.completed_todos,name='completed_todos'),
    #view,edit and save a todo
    path('todo/<int:todo_pk>',views.view_todo,name='view_todo'), #takes primary key of the todo object as an url argument
    #complete the todo
    path('todo/<int:todo_pk>/complete',views.complete_todo,name='complete_todo'),
    #delete the todo
    path('todo/<int:todo_pk>/delete',views.delete_todo,name='delete_todo'),
]
