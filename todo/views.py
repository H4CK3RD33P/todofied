from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # this will include Django's built-in sign-up form template class.
# Create your views here.
def signupuser(request):
    #We are creating an instance of UserCreationForm (sign-up form) and passing it to the template
    return render(request,'todo/signupuser.html',{'form': UserCreationForm()})