from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # this will include Django's built-in sign-up form template class.
from django.contrib.auth.models import User #this will import the built-in User model of Django
from django.db import IntegrityError #this will import Django's built-in DB exception which makes sure that usernames are unique
# Create your views here.
def signupuser(request): 
    if request.method == "GET": #this will happen when a user opens the signup/ path 
        #We are creating an instance of UserCreationForm (sign-up form) and passing it to the template
        return render(request,'todo/signupuser.html',{'form': UserCreationForm()})
    else: #this will happen when user submits the form
        if request.POST['password1'] == request.POST['password2']: #only if the rewritten password matches the previous password
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1']) #create a User object with the given username and password
                user.save() #save the user object in the database
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Username already exists! Try again.'}) #if the username is not unique in the db then this error message is returned
        else: #if the two passwords do not match
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords do not match! Try again.'}) #we pass the 'password not matched' error to the page to display it
            