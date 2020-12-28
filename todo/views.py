from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # this will include Django's built-in sign-up form template class.
from django.contrib.auth.models import User #this will import the built-in User model of Django
# Create your views here.
def signupuser(request): 
    if request.method == "GET": #this will happen when a user opens the signup/ path 
        #We are creating an instance of UserCreationForm (sign-up form) and passing it to the template
        return render(request,'todo/signupuser.html',{'form': UserCreationForm()})
    else: #this will happen when user submits the form
        if request.POST['password1'] == request.POST['password2']: #only if the rewritten password matches the previous password
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1']) #create a User object with the given username and password
            user.save() #save the user object in the database
        else: #if the two passwords do not match
            print("Error: Password not matched.")
