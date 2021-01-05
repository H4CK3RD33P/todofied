from django.shortcuts import render
from django.shortcuts import redirect #this will import Django's redirect function which will redirect to a different function
from django.contrib.auth.forms import UserCreationForm # this will include Django's built-in sign-up form template class.
from django.contrib.auth.forms import AuthenticationForm #this will include Django's built-in log-in form
from django.contrib.auth.models import User #this will import the built-in User model of Django
from django.db import IntegrityError #this will import Django's built-in DB exception which makes sure that usernames are unique
from django.contrib.auth import login #this will import Djnago's login function which will let the user log in
from django.contrib.auth import logout #this will import Django's redirect function which will log out the user.
from django.contrib.auth import authenticate #this will import Django's authenticate function which will let the user log in.
from .forms import TodoForm #this imports the TodoForm which will be passed to create/ through create_todo()
# Create your views here.

def home(request):
    return render(request,'todo/home.html')

def signupuser(request): 
    if request.method == "GET": #this will happen when a user opens the signup/ path 
        #We are creating an instance of UserCreationForm (sign-up form) and passing it to the template
        return render(request,'todo/signupuser.html',{'form': UserCreationForm()})
    else: #this will happen when user submits the form
        if request.POST['password1'] == request.POST['password2']: #only if the rewritten password matches the previous password
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1']) #create a User object with the given username and password
                user.save() #save the user object in the database
                login(request,user) #log the user in
                return redirect('current_todos') #redirecting to current_todos view (current/)
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Username already exists! Try again.'}) #if the username is not unique in the db then this error message is returned
        else: #if the two passwords do not match
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords do not match! Try again.'}) #we pass the 'password not matched' error to the page to display it

def create_todo(request):
    if request.method == 'GET':
        return render(request,'todo/create_todo.html',{'form':TodoForm()}) #pass the todo form
    else:
        try:
            form = TodoForm(request.POST) #stores all the info coming from the form posted.
            newtodo = form.save(commit=False) #saves it to the database WITHOUT COMMIT
            newtodo.user = request.user #adds the user (WHO IS CURRENTLY LOGGED IN)
            newtodo.save() #Again saves the object to the database WITH COMMIT! Final SAVE.
            return redirect('current_todos') #redirects the user to his/her todo list page. i.e current/
        except ValueError:
            return render(request,'todo/create_todo.html',{'form':TodoForm(),'error':'Bad Data Passed.'})

def current_todos(request):
    return render(request,'todo/current_todos.html')

def loginuser(request):
    if request.method=="GET":
        return render(request,'todo/loginuser.html',{'form':AuthenticationForm()}) #pass login form to the page.
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password']) #authenticating the user
        if user is None: #if the user does not exist or there if the credentials do not match then pass an error to display.
            return render(request,'todo/loginuser.html',{'form':AuthenticationForm(),'error':'Username and passwords do not match'})
        else:
            login(request,user) #if the authentication is successful however, log in the user
            return redirect('current_todos') ##and redirect him/her to the todo list page.

def logoutuser(request):
    if request.method=='POST': #if the method is POST then log out the user and redirect him/her to the home
        logout(request)
        return redirect('home')