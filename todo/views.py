from django.shortcuts import render

# Create your views here.
def signupuser(request):
    return render(request,'todo/signupuser.html')